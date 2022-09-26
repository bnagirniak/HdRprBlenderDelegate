bl_info = {
    "name": "USD Hydra HdRpr",
    "author": "AMD",
    "version": (1, 0, 0),
    "blender": (3, 2, 0),
    "location": "Info header > Render engine menu",
    "description": "USD Hydra renderer integration",
    "tracker_url": "",
    "doc_url": "",
    "community": "",
    "downloads": "",
    "main_web": "",
    "support": 'TESTING',
    "category": "Render"
}

# Support 'reload' case.
if "bpy" in locals():
    import importlib
    importlib.reload(engine)
    importlib.reload(properties)
    importlib.reload(ui)

else:
    from . import (
        engine,
        properties,
        ui,
    )

from bpy.utils import register_class, unregister_class, register_classes_factory


register_ui, unregister_ui = register_classes_factory(
    [
        ui.USDHYDRA_RENDER_PT_final,
        ui.USDHYDRA_RENDER_PT_viewport,
        ui.USDHYDRA_RENDER_PT_denoise_final,
        ui.USDHYDRA_RENDER_PT_denoise_viewport,
        ui.USDHYDRA_RENDER_PT_film_final,
        ui.USDHYDRA_RENDER_PT_pixel_filter_final,
        ui.USDHYDRA_RENDER_PT_pixel_filter_viewport,
        ui.USDHYDRA_RENDER_PT_quality_final,
        ui.USDHYDRA_RENDER_PT_quality_viewport,
        ui.USDHYDRA_RENDER_PT_samples_final,
        ui.USDHYDRA_RENDER_PT_samples_viewport,
    ]
)

register_properties, unregister_properties = register_classes_factory(
    [
        properties.ContourSettings,
        properties.DenoiseSettings,
        properties.InteractiveQualitySettings,
        properties.QualitySettings,
        properties.RenderSettings,
        # properties.ViewportRenderSettings,
        # properties.FinalRenderSettings,
        properties.SceneProperties,
    ]
)


def register():
    import addon_utils
    enabled, loaded = addon_utils.check('usdhydra')
    if enabled and loaded:
        register_class(engine.USDHydraHdRprEngine)
        register_properties()
        register_ui()
        engine.register()

    else:
        addon_utils.disable(engine.USDHydraHdRprEngine.bl_idname)


def unregister():
    try:
        unregister_class(engine.USDHydraHdRprEngine)
        unregister_ui()
        unregister_properties()
        engine.unregister()
    except Exception as err:
        from usdhydra import utils
        log = utils.loggin.Log("HdRprBlenderDelegate")
        log.warn("Delegate  Unregistering", err)

