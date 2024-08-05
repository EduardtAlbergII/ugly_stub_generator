import os
import inspect
from typing import List, Tuple, Type
import re


def __get_parameters_and_return_from_docstring(docstring: str, type_correction: dict[str, str] = {}) -> Tuple[List[str], str]:
    """
    Extrahiert Parameter und Rückgabetyp aus einem Docstring im Format:
    @param name: Description
    @type name: type
    @return: Description
    @rtype: type
    """
    params = []
    return_type = "None"

    if not docstring:
        return params, return_type

    param_pattern = re.compile(r'@param (\w+):')
    type_pattern = re.compile(r'@type (\w+): (\w+)')
    return_pattern = re.compile(r'@rtype: (\w+)')

    param_matches = param_pattern.findall(docstring)
    type_matches = type_pattern.findall(docstring)
    return_match = return_pattern.search(docstring)

    type_dict = {name: typ for name, typ in type_matches}
    for param in param_matches:
        param_type = type_dict.get(param, 'Any')
        param_type = type_correction.get(param_type, param_type)
        params.append(f"{param}: {param_type}")

    if return_match:
        return_type = return_match.group(1)
        return_type = type_correction.get(return_type, return_type)

    return params, return_type


def __generate_stub_for_class(cls, type_correction: dict[str, str] = {}) -> str:
    """
    Creates the stub content for the given class.
    """
    lines = [f"class {cls.__name__}:"]
    modulename = cls.__module__
    # Extract class attributes
    for name, value in cls.__dict__.items():
        if not callable(value):
            attr_type = type(value).__name__
            lines.append(f"    {name}: {attr_type}")

    # Extract method signatures
    for name, member in inspect.getmembers(cls):
        try:
            if not ".overload" in name:
                if callable(member):
                    if str(type(member)) == "<class 'method_descriptor'>":
                        signature: str = str(inspect.signature(member))
                        signature = signature.replace(f"{modulename}.", "")
                        lines.append(f"    def {name}{signature}: ...")
                    else:
                        docstring = member.__doc__
                        params, return_type = __get_parameters_and_return_from_docstring(docstring, type_correction)
                        param_list = ', '.join(["self"] + params)
                        param_list = param_list.replace(f"{modulename}.", "")
                        return_type = return_type.replace(f"{modulename}.", "")
                        lines.append(f"    def {name}({param_list}) -> {return_type}: ...")
        except Exception as e:
            print(f"Error in {name} with {member}")
            print(e)

    # Add a default implementation if no methods or attributes were found
    if len(lines) == 1:
        lines.append("    pass")

    return "\n".join(lines)


def __generate_stub_for_module(mdl, type_correction: dict[str, str] = {}) -> str:
    """
    Erzeugt den Stub-Inhalt für die gegebene Klasse.
    """
    lines = [f""]

    # Extract class attributes
    for name, value in mdl.__dict__.items():
        if not callable(value):
            attr_type = type(value).__name__
            lines.append(f"{name}: {attr_type}")

    # Extract method signatures
    for name, member in inspect.getmembers(mdl):
        try:
            if not ".overload" in name:
                if callable(member) and str(type(member)) != "<class 'Shiboken.ObjectType'>":
                    if str(type(member)) == "<class 'method_descriptor'>":
                        signature = str(inspect.signature(member))
                        signature = signature.replace(f"{mdl.__name__}.", "")
                        lines.append(f"def {name}{signature}: ...")
                    else:
                        docstring = member.__doc__
                        params, return_type = __get_parameters_and_return_from_docstring(docstring, type_correction)
                        param_list = ', '.join(["self"] + params)
                        param_list = param_list.replace(f"{mdl.__name__}.", "")
                        return_type = return_type.replace(f"{mdl.__name__}.", "")
                        lines.append(f"def {name}({param_list}) -> {return_type}: ...")
        except Exception as e:
            print(f"Error in {name} with {member}")
            print(e)

    return "\n".join(lines)


def generate_runtime_stubs(classes: List[Type], directory_path: str = "./typings", custom_type_correction: dict[str, str] = {}):
    os.makedirs(directory_path, exist_ok=True)

    type_correction = {
        "string": "str",
        "unsigned": "int",
        "boolean": "bool",
        "Bool": "bool",
        "integer": "int",
        "boost": "object",
        "Real32": "float",
        "Int32": "int",
        "std": "list",
        "double": "float",
        "short": "int",
        "floatf": "float",
        "UInt": "int",
        "vector": "list",
        "long": "int",
    }
    type_correction.update(custom_type_correction)

    module_classes = {}
    module_functions = {}

    for cls in classes:

        module_name = cls.__module__ if "__module__" in cls.__dict__ else cls.__name__
        if module_name not in module_classes:
            module_classes[module_name] = []
        module_classes[module_name].append(cls)

        # Add functions to the module
        module = inspect.getmodule(cls)
        if module is not None:
            if module_name not in module_functions:
                module_functions[module_name] = []
            for name, member in inspect.getmembers(module, inspect.isfunction):
                if member.__module__ == module_name:
                    module_functions[module_name].append(member)

    for module_name, cls_list in module_classes.items():
        lines = []

        # Generate stub for classes
        for cls in cls_list:
            try:
                if "__module__" in cls.__dict__:
                    stub_content = __generate_stub_for_class(cls, type_correction)
                else:
                    stub_content = __generate_stub_for_module(cls, type_correction)
                lines.append(stub_content)
            except Exception as e:
                print(e)

        destination_path = os.path.join(directory_path, f"{module_name}.pyi")
        with open(destination_path, 'w') as f:
            f.write("\n\n".join(lines))
        print(f'Stub-Datei wurde erstellt: {destination_path}')
