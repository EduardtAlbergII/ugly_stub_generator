# ugly_stub_generator
Stub Generator for classes only available in a specific environment (application)

## Getting started 
Open your target environment / application and import the function *create_stub_files_vred_api_v1* from *ugly_stub_generator* in the Python interface. To be able to import the module, you must add the parent folder of the module in *sys.path*.

```
import sys
sys.path.append("path/to/project")
from ugly_stub_generator import generate_runtime_stubs
```

Collect all modules and classes from which you need stub files in a list and add them to the function. You can specify the target directory as the second parameter. The third parameter allows you to specify type translations in a dict. By default, some c types like "string" are already translated to "str".

To be able to use the generated stub files in Visual Studio Code, they must be located in the project directory under the "typings" folder by default.

Just take a look at the [example.py](example.py)

You are invited to commit changes, extensions & corrections. You are also welcome to add a branch with a different version.

## ToDo
- Currently, all objects are analysed and mapped flat. It would be useful to map inheritances as well.
- Necessary imports are not written to the stub files.
- Classes are often represented in modules as a class and a method. (Bug)