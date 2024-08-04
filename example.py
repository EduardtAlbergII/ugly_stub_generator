import sys
import os

sys.path.append(os.curdir)
from ugly_stub_generator import generate_runtime_stubs


def create_stub_files_vred_api_v1(path: str):
    import vrAEBase
    import vrAmbientOcclusion
    import vrAnimWidgets
    import vrAnimation
    import vrAnnotation
    import vrAnnotationPtr
    import vrAssetsModule
    import vrCamera
    import vrChunkPtr
    import vrClippingModule
    import vrCluster
    import vrCollision
    import vrColorDialog
    import vrConnector
    import vrConstraints
    import vrController
    import vrCubeImages
    import vrFade
    import vrFieldAccess
    import vrFileDialog
    import vrFileIO
    import vrFrame
    import vrGeometryEditor
    import vrImagePtr
    import vrInteraction
    import vrInteractionModule
    import vrInterpolator
    import vrJoystick
    import vrKey
    import vrLightLinkSetPtr
    import vrMain
    import vrMaterialEditor
    import vrMaterialPtr
    import vrMeasurement
    import vrMenu
    import vrMovieExport
    import vrMoviePlayer2
    import vrNodePtr
    import vrNodeUtils
    import vrOSGTypes
    import vrOSGWidget
    import vrOculusTouchController
    import vrOpenPDM
    import vrOpenVR
    import vrOptimize
    import vrQObject
    import vrRenderLayerModule
    import vrRenderQueue
    import vrRenderSettings
    import vrRoute
    import vrRuler
    import vrSHLChunkPtr
    import vrScenegraph
    import vrScript
    import vrSequencer
    import vrSpacemouseButton
    import vrSpeech
    import vrSurfaceAnalysis
    import vrSwitch
    import vrTextureChunkPtr
    import vrTimer
    import vrTouchSensor
    import vrTransform
    import vrTransformHelper
    import vrURManager
    import vrUVEditor
    import vrVRMLViewPoints
    import vrVariantSetPtr
    import vrVariantSets
    import vrVariants
    import vrVideoGrab
    import vrViewPoint
    import vrVirtualEye
    import vrVredUi
    import vrVrpnTracking
    import vrVrpnTrackingService
    import vrWebEngineObj
    import vrWebOverlay
    import vrWidget

    modules = [
        vrAEBase,
        vrAmbientOcclusion,
        vrAnimWidgets,
        vrAnimation,
        vrAnnotation,
        vrAnnotationPtr,
        vrAssetsModule,
        vrCamera,
        vrChunkPtr,
        vrClippingModule,
        vrCluster,
        vrCollision,
        vrColorDialog,
        vrConnector,
        vrConstraints,
        vrController,
        vrCubeImages,
        vrFade,
        vrFieldAccess,
        vrFileDialog,
        vrFileIO,
        vrFrame,
        vrGeometryEditor,
        vrImagePtr,
        vrInteraction,
        vrInteractionModule,
        vrInterpolator,
        vrJoystick,
        vrKey,
        vrLightLinkSetPtr,
        vrMain,
        vrMaterialEditor,
        vrMaterialPtr,
        vrMeasurement,
        vrMenu,
        vrMovieExport,
        vrMoviePlayer2,
        vrNodePtr,
        vrNodeUtils,
        vrOSGTypes,
        vrOSGWidget,
        vrOculusTouchController,
        vrOpenPDM,
        vrOpenVR,
        vrOptimize,
        vrQObject,
        vrRenderLayerModule,
        vrRenderQueue,
        vrRenderSettings,
        vrRoute,
        vrRuler,
        vrSHLChunkPtr,
        vrScenegraph,
        vrScript,
        vrSequencer,
        vrSpacemouseButton,
        vrSpeech,
        vrSurfaceAnalysis,
        vrSwitch,
        vrTextureChunkPtr,
        vrTimer,
        vrTouchSensor,
        vrTransform,
        vrTransformHelper,
        vrURManager,
        vrUVEditor,
        vrVRMLViewPoints,
        vrVariantSetPtr,
        vrVariantSets,
        vrVariants,
        vrVideoGrab,
        vrViewPoint,
        vrVirtualEye,
        vrVredUi,
        vrVrpnTracking,
        vrVrpnTrackingService,
        vrWebEngineObj,
        vrWebOverlay,
        vrWidget,
    ]

    classes = [
        object,
        vrAEBase.vrAEBase,
        vrAnnotationPtr.vrAnnotationPtr,
        vrChunkPtr.StateChunkPtr,
        vrChunkPtr.vrChunkPtr,
        vrCollision.vrCollision,
        vrFade.vrFade,
        vrFieldAccess.FieldContainerPtr,
        vrFieldAccess.vrFieldAccess,
        vrFrame.vrFrame,
        vrImagePtr.ImagePtr,
        vrImagePtr.vrImagePtr,
        vrInteraction.vrInteraction,
        vrInterpolator.vrInterpolator,
        vrInterpolator.vrRotationAxisSlide,
        vrInterpolator.vrRotationSlide,
        vrInterpolator.vrScaleSlide,
        vrInterpolator.vrSlide,
        vrInterpolator.vrTranslationSlide,
        vrJoystick.vrJoystick,
        vrKey.vrKey,
        vrLightLinkSetPtr.LightLinkSetPtr,
        vrLightLinkSetPtr.vrLightLinkSetPtr,
        vrMaterialPtr.MaterialPtr,
        vrMaterialPtr.vrMaterialPtr,
        vrMenu.vrMenu,
        vrMoviePlayer2.vrMoviePlayer2,
        vrNodePtr.NodePtr,
        vrNodePtr.vrNodePtr,
        vrOSGTypes.Color3f,
        vrOSGTypes.Color4f,
        vrOSGTypes.Pnt2f,
        vrOSGTypes.Pnt3f,
        vrOSGTypes.Pnt4f,
        vrOSGTypes.Vec2f,
        vrOSGTypes.Vec3f,
        vrOSGTypes.Vec4f,
        vrOculusTouchController.vrOculusTouchController,
        vrOpenVR.vrOpenVRController,
        vrOpenVR.vrOpenVRFrameTimings,
        vrQObject.vrQObject,
        vrSHLChunkPtr.SHLChunkPtr,
        vrSHLChunkPtr.vrSHLChunkPtr,
        vrSpacemouseButton.vrSpacemouseButton,
        vrSpeech.vrSpeech,
        vrSwitch.vrSwitch,
        vrTextureChunkPtr.TextureChunkPtr,
        vrTextureChunkPtr.vrTextureChunkPtr,
        vrTimer.vrTimer,
        vrTouchSensor.vrTouchSensor,
        vrVariantSetPtr.vrVariantSetPtr,
        vrVideoGrab.vrVideoGrab,
        vrViewPoint.vrViewPoint,
        vrVirtualEye.vrVirtualEye,
        vrVrpnTracking.vrSelection,
        vrVrpnTracking.vrTrackerAnalog,
        vrVrpnTracking.vrTrackerBody,
        vrVrpnTracking.vrTrackerButton,
        vrVrpnTracking.vrTrackerDial,
        vrVrpnTracking.vrTrackerSensor,
        vrWebOverlay.vrWebOverlay,
        vrWidget.vrWidget,
    ]

    generate_runtime_stubs(modules + classes, path)


def create_stub_files_vred_api_v2(path: str):

    import vrKernelServices

    modules = [vrKernelServices]

    classes = [
        vrKernelServices.vrdNode,
        vrKernelServices.vrAnnotationService,
        vrKernelServices.vrAnnotationTypes,
        vrKernelServices.vrAssetsService,
        vrKernelServices.vrBakeService,
        vrKernelServices.vrBakeTypes,
        vrKernelServices.vrCADFileTypes,
        vrKernelServices.vrCameraFromAtUp,
        vrKernelServices.vrCameraService,
        vrKernelServices.vrCameraTypes,
        vrKernelServices.vrClusterManagerService,
        vrKernelServices.vrClusterService,
        vrKernelServices.vrClusterTypes,
        vrKernelServices.vrConstraintService,
        vrKernelServices.vrDecoreService,
        vrKernelServices.vrDeviceService,
        vrKernelServices.vrFileIOService,
        vrKernelServices.vrFileTypes,
        vrKernelServices.vrGPUService,
        vrKernelServices.vrGPUTypes,
        vrKernelServices.vrGUIService,
        vrKernelServices.vrGeometryService,
        vrKernelServices.vrGeometryTypes,
        vrKernelServices.vrHMDService,
        vrKernelServices.vrHandTypes,
        vrKernelServices.vrImageService,
        vrKernelServices.vrImageTypes,
        vrKernelServices.vrImmersiveInteractionService,
        vrKernelServices.vrImmersiveInteractionTypes,
        vrKernelServices.vrImmersiveUiService,
        vrKernelServices.vrLensFlareTypes,
        vrKernelServices.vrLightService,
        vrKernelServices.vrLightTypes,
        vrKernelServices.vrMaterialEntryId,
        vrKernelServices.vrMaterialService,
        vrKernelServices.vrMaterialTypes,
        vrKernelServices.vrMathService,
        vrKernelServices.vrMetadataService,
        vrKernelServices.vrMetadataTypes,
        vrKernelServices.vrNodeService,
        vrKernelServices.vrObjectService,
        vrKernelServices.vrProgressService,
        vrKernelServices.vrQueryService,
        vrKernelServices.vrReferenceService,
        vrKernelServices.vrReferenceTypes,
        vrKernelServices.vrRenderTypes,
        vrKernelServices.vrRoughnessTextureTypes,
        vrKernelServices.vrScenegraphService,
        vrKernelServices.vrScenegraphTypes,
        vrKernelServices.vrSceneplateService,
        vrKernelServices.vrSceneplateTypes,
        vrKernelServices.vrSessionService,
        vrKernelServices.vrSpectrum,
        vrKernelServices.vrStyleTypes,
        vrKernelServices.vrSubstanceTypes,
        vrKernelServices.vrTextureTypes,
        vrKernelServices.vrTransformTypes,
        vrKernelServices.vrUVService,
        vrKernelServices.vrUVTypes,
        vrKernelServices.vrUndoService,
        vrKernelServices.vrVRInputDeviceTypes,
        vrKernelServices.vrWebEngineService,
        vrKernelServices.vrXRealityTypes,
        vrKernelServices.vrdAimConstraintNode,
        vrKernelServices.vrdAnalyticSettings,
        vrKernelServices.vrdAnnotationNode,
        vrKernelServices.vrdAreaLightCone,
        vrKernelServices.vrdAreaLightNode,
        vrKernelServices.vrdAtfSettings,
        vrKernelServices.vrdBRDFCommonSettings,
        vrKernelServices.vrdBRDFMaterial,
        vrKernelServices.vrdBaseLightNode,
        vrKernelServices.vrdBaseLightProfile,
        vrKernelServices.vrdBillboardNode,
        vrKernelServices.vrdBlendChunk,
        vrKernelServices.vrdBoundingBox,
        vrKernelServices.vrdBrushOrientation,
        vrKernelServices.vrdBrushedMetalMaterial,
        vrKernelServices.vrdBsdfMeasurement,
        vrKernelServices.vrdBumpTexture,
        vrKernelServices.vrdButtonState,
        vrKernelServices.vrdCameraBaseNode,
        vrKernelServices.vrdCameraCollider,
        vrKernelServices.vrdCameraNode,
        vrKernelServices.vrdCameraTrackNode,
        vrKernelServices.vrdCarbon2DMaterial,
        vrKernelServices.vrdCarbonMaterial,
        vrKernelServices.vrdCarbonPattern,
        vrKernelServices.vrdCarbonPattern2D,
        vrKernelServices.vrdCarbonPattern3D,
        vrKernelServices.vrdChromeMaterial,
        vrKernelServices.vrdChunkMaterial,
        vrKernelServices.vrdClearcoat,
        vrKernelServices.vrdClipPlaneNode,
        vrKernelServices.vrdColorCorrection,
        vrKernelServices.vrdConstraintNode,
        vrKernelServices.vrdCubeTextureChunk,
        vrKernelServices.vrdDecoreSettings,
        vrKernelServices.vrdDeltaLightNode,
        vrKernelServices.vrdDepthTestChunk,
        vrKernelServices.vrdDeviceAction,
        vrKernelServices.vrdDeviceActionSignal,
        vrKernelServices.vrdDeviceInteraction,
        vrKernelServices.vrdDeviceMessageData,
        vrKernelServices.vrdDirectionalLightNode,
        vrKernelServices.vrdDiskLightNode,
        vrKernelServices.vrdDisplacement,
        vrKernelServices.vrdDisplacementTexture,
        vrKernelServices.vrdDistanceLODNode,
        vrKernelServices.vrdEnvironmentColorCorrection,
        vrKernelServices.vrdEnvironmentMaterial,
        vrKernelServices.vrdEnvironmentNode,
        vrKernelServices.vrdEnvironmentRaytracingSettings,
        vrKernelServices.vrdEnvironmentShadowsAndIllumination,
        vrKernelServices.vrdEnvironmentSwitchMaterial,
        vrKernelServices.vrdEnvironmentTransformation,
        vrKernelServices.vrdEyeGaze,
        vrKernelServices.vrdFileExportSettings,
        vrKernelServices.vrdFindOptions,
        vrKernelServices.vrdFlakeLayer,
        vrKernelServices.vrdFlipflopCarpaintMaterial,
        vrKernelServices.vrdFlipflopFlakeLayer,
        vrKernelServices.vrdFoveatedQuality,
        vrKernelServices.vrdGLSLShaderChunk,
        vrKernelServices.vrdGLSLShaderParameter,
        vrKernelServices.vrdGLSLShaderParameterInt,
        vrKernelServices.vrdGLSLShaderParameterList,
        vrKernelServices.vrdGLSLShaderParameterMatrix,
        vrKernelServices.vrdGLSLShaderParameterReal,
        vrKernelServices.vrdGLSLShaderParameterVec2f,
        vrKernelServices.vrdGLSLShaderParameterVec3f,
        vrKernelServices.vrdGLSLShaderParameterVec4f,
        vrKernelServices.vrdGeometryNode,
        vrKernelServices.vrdGlassMaterial,
        vrKernelServices.vrdGpuStateInfo,
        vrKernelServices.vrdHDRLightStudio,
        vrKernelServices.vrdHostSwitchNode,
        vrKernelServices.vrdIlluminationBakeSettings,
        vrKernelServices.vrdImage,
        vrKernelServices.vrdImmersiveMenu,
        vrKernelServices.vrdImmersiveTool,
        vrKernelServices.vrdImmersiveToolSignal,
        vrKernelServices.vrdIncandescence,
        vrKernelServices.vrdLayeredMaterial,
        vrKernelServices.vrdLensFlareEffect,
        vrKernelServices.vrdLensFlareElement,
        vrKernelServices.vrdLensFlareFxElement,
        vrKernelServices.vrdLensFlareGhost,
        vrKernelServices.vrdLensFlareGhostLine,
        vrKernelServices.vrdLensFlareGlow,
        vrKernelServices.vrdLensFlareRing,
        vrKernelServices.vrdLensFlareStar,
        vrKernelServices.vrdLensFlareStreak,
        vrKernelServices.vrdLightLinkSetNode,
        vrKernelServices.vrdLightPortalMaterial,
        vrKernelServices.vrdLightProfile,
        vrKernelServices.vrdLightTexture,
        vrKernelServices.vrdLightTransform,
        vrKernelServices.vrdLightmap,
        vrKernelServices.vrdLineChromeMaterial,
        vrKernelServices.vrdLineChunk,
        vrKernelServices.vrdMDLMaterial,
        vrKernelServices.vrdMDLProperties,
        vrKernelServices.vrdMarker,
        vrKernelServices.vrdMaterial,
        vrKernelServices.vrdMaterialChunk,
        vrKernelServices.vrdMaterialChunkList,
        vrKernelServices.vrdMaterialList,
        vrKernelServices.vrdMaterialNode,
        vrKernelServices.vrdMaterialPoolNode,
        vrKernelServices.vrdMaterialRaytracingSettings,
        vrKernelServices.vrdMaterialXMaterial,
        vrKernelServices.vrdMaterialXProperties,
        vrKernelServices.vrdMatrixTransformNode,
        vrKernelServices.vrdMeasuredCarpaintMaterial,
        vrKernelServices.vrdMeasuredMaterial,
        vrKernelServices.vrdMetadata,
        vrKernelServices.vrdMetadataEntry,
        vrKernelServices.vrdMetadataEntryList,
        vrKernelServices.vrdMetadataSet,
        vrKernelServices.vrdMetallicCarpaintMaterial,
        vrKernelServices.vrdMultiMarker,
        vrKernelServices.vrdMultiMaterial,
        vrKernelServices.vrdMultiPassMaterial,
        vrKernelServices.vrdNPRSettings,
        vrKernelServices.vrdNode,
        vrKernelServices.vrdNodeInfo,
        vrKernelServices.vrdNodeList,
        vrKernelServices.vrdOCSMaterial,
        vrKernelServices.vrdObject,
        vrKernelServices.vrdObjectList,
        vrKernelServices.vrdObjectSignal,
        vrKernelServices.vrdOpenGLInfo,
        vrKernelServices.vrdOrientationConstraintNode,
        vrKernelServices.vrdParentConstraintNode,
        vrKernelServices.vrdPerspectiveMatch,
        vrKernelServices.vrdPhongMaterial,
        vrKernelServices.vrdPlasticMaterial,
        vrKernelServices.vrdPointLightNode,
        vrKernelServices.vrdPolygonChunk,
        vrKernelServices.vrdPositionConstraintNode,
        vrKernelServices.vrdProjectMergeSettings,
        vrKernelServices.vrdRayFile,
        vrKernelServices.vrdRayFileInfo,
        vrKernelServices.vrdRayIntersection,
        vrKernelServices.vrdRayLightNode,
        vrKernelServices.vrdRaytracingInfo,
        vrKernelServices.vrdRectangularLightNode,
        vrKernelServices.vrdReferenceNode,
        vrKernelServices.vrdReflectivePlasticMaterial,
        vrKernelServices.vrdRoughnessTexture,
        vrKernelServices.vrdRoundedEdges,
        vrKernelServices.vrdSVBRDFMaterial,
        vrKernelServices.vrdSceneImportSettings,
        vrKernelServices.vrdSceneItemInfo,
        vrKernelServices.vrdSceneObject,
        vrKernelServices.vrdSceneplateNode,
        vrKernelServices.vrdSessionUser,
        vrKernelServices.vrdShadowMap,
        vrKernelServices.vrdShadowMaterial,
        vrKernelServices.vrdSkylightLocation,
        vrKernelServices.vrdSkylightMaterial,
        vrKernelServices.vrdSkylightSkyAndSun,
        vrKernelServices.vrdSoundNode,
        vrKernelServices.vrdSoundObstructorNode,
        vrKernelServices.vrdSphereEnvironmentMaterial,
        vrKernelServices.vrdSphericalLightNode,
        vrKernelServices.vrdSpotLightNode,
        vrKernelServices.vrdStereoSwitchNode,
        vrKernelServices.vrdSubstanceEnvironmentMaterial,
        vrKernelServices.vrdSubstanceMaterial,
        vrKernelServices.vrdSubstancePreset,
        vrKernelServices.vrdSubstanceProperties,
        vrKernelServices.vrdSubsurfaceScattering,
        vrKernelServices.vrdSurfaceNode,
        vrKernelServices.vrdSwitchMaterial,
        vrKernelServices.vrdSwitchNode,
        vrKernelServices.vrdTessellationSettings,
        vrKernelServices.vrdTexture,
        vrKernelServices.vrdTextureBake,
        vrKernelServices.vrdTextureBakeSettings,
        vrKernelServices.vrdTextureChunk,
        vrKernelServices.vrdTextureSettings,
        vrKernelServices.vrdTireMaterial,
        vrKernelServices.vrdTireTextureSettings,
        vrKernelServices.vrdTonemapper,
        vrKernelServices.vrdTrackedHand,
        vrKernelServices.vrdTransformNode,
        vrKernelServices.vrdTransformNodeVariant,
        vrKernelServices.vrdTransparency,
        vrKernelServices.vrdTurntable,
        vrKernelServices.vrdUVBaseProjectionSettings,
        vrKernelServices.vrdUVCylindricalProjectionSettings,
        vrKernelServices.vrdUVLayoutSettings,
        vrKernelServices.vrdUVOptimizeSettings,
        vrKernelServices.vrdUVPlanarProjectionSettings,
        vrKernelServices.vrdUVSeamSettings,
        vrKernelServices.vrdUVTriplanarProjectionSettings,
        vrKernelServices.vrdUVUnfoldSettings,
        vrKernelServices.vrdUiEngine,
        vrKernelServices.vrdUnicolorCarpaintMaterial,
        vrKernelServices.vrdVRDevice,
        vrKernelServices.vrdVRDeviceSignal,
        vrKernelServices.vrdVarjoRenderSettings,
        vrKernelServices.vrdVelvetMaterial,
        vrKernelServices.vrdVertexBake,
        vrKernelServices.vrdVertexBakeSettings,
        vrKernelServices.vrdViewpointNode,
        vrKernelServices.vrdVirtualTouchpadButton,
        vrKernelServices.vrdWebEngine,
        vrKernelServices.vrdWovenClothMaterial,
        vrKernelServices.vrdXRayMaterial,
        vrKernelServices.vrdXRiteMeasuredMaterial,
    ]

    generate_runtime_stubs(modules + classes, path)


if __name__ == "__main__":
    create_stub_files_vred_api_v1("./typings")
    create_stub_files_vred_api_v2("./typings")
    print("Stubs generated successfully.")
