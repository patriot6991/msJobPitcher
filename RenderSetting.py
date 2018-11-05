import maya.cmds as mc
import maya.mel as mel
import json
import logging

path = r'\\172.29.44.4\cg\ms06\msJobPitcher\renderSettings\msTest.json'


def jsonRead():
    logging.debug('jsonRead')
    global dec
    get = open(path)
    a = json.load(get)
    b = a['arnold']

    dec = b['defaultNodes']
    c = b['defaultRendererNodes']
    dec.update(c)
    common()


def common():
    global dec
    # File output
    mc.setAttr('defaultRenderGlobals.imageFilePrefix', dec['defaultRenderGlobals.imageFilePrefix'], type='string')
    mc.setAttr('defaultArnoldDriver.aiTranslator', dec['defaultArnoldDriver.aiTranslator'], type='string')
    if 'jpeg' in dec['defaultRenderGlobals.imfPluginKey']:
        mc.setAttr('defaultArnoldDriver.quality', dec['defaultArnoldDriver.quality'])
        mc.setAttr('defaultArnoldDriver.outputPadded', dec['defaultArnoldDriver.outputPadded'])
        mc.setAttr('defaultArnoldDriver.dither', dec['defaultArnoldDriver.dither'])
        mc.setAttr('defaultArnoldDriver.colorManagement', dec['defaultArnoldDriver.colorManagement'])  #ColorSpace
        mel.eval('setMayaSoftwareFrameExt("6", 0)')  #F/A.
        mc.setAttr('defaultRenderGlobals.extensionPadding', dec['defaultRenderGlobals.extensionPadding'])
    elif 'png' in dec['defaultRenderGlobals.imfPluginKey']:
        mc.setAttr('defaultArnoldDriver.pngFormat', dec['defaultArnoldDriver.pngFormat'])
        mc.setAttr('defaultArnoldDriver.outputPadded', dec['defaultArnoldDriver.outputPadded'])
        mc.setAttr('defaultArnoldDriver.dither', dec['defaultArnoldDriver.dither'])
        mc.setAttr('defaultArnoldDriver.colorManagement', dec['defaultArnoldDriver.colorManagement'])
        mel.eval('setMayaSoftwareFrameExt("6", 0)')  #F/A.
        mc.setAttr('defaultRenderGlobals.extensionPadding', 'defaultRenderGlobals.extensionPadding')
    elif 'tif' in dec['defaultRenderGlobals.imfPluginKey']:
        mc.setAttr('defaultArnoldDriver.tiffCompression', dec['defaultArnoldDriver.tiffCompression'])
        mc.setAttr('defaultArnoldDriver.tiffFormat', dec['defaultArnoldDriver.tiffFormat'])
        mc.setAttr('defaultArnoldDriver.tiffTiled', dec['defaultArnoldDriver.tiffTiled'])
        mc.setAttr('defaultArnoldDriver.dither', dec['defaultArnoldDriver.dither'])
        mc.setAttr('defaultArnoldDriver.unpremultAlpha', dec['defaultArnoldDriver.unpremultAlpha'])
        mc.setAttr('defaultArnoldDriver.skipAlpha', dec['defaultArnoldDriver.skipAlpha'])
        mc.setAttr('defaultArnoldDriver.append', dec['defaultArnoldDriver.append'])
        mc.setAttr('defaultArnoldDriver.colorManagement', dec['defaultArnoldDriver.colorManagement'])
        mel.eval('setMayaSoftwareFrameExt("6", 0)')  #F/A.
        mc.setAttr('defaultRenderGlobals.extensionPadding', dec['defaultRenderGlobals.extensionPadding'])
    elif 'exr' in dec['defaultRenderGlobals.imfPluginKey']:
        mc.setAttr('defaultArnoldDriver.exrCompression', dec['defaultArnoldDriver.exrCompression'])
        mc.setAttr('defaultArnoldDriver.halfPrecision', dec['defaultArnoldDriver.halfPrecision'])
        mc.setAttr('defaultArnoldDriver.preserveLayerName', dec['defaultArnoldDriver.preserveLayerName'])
        mc.setAttr('defaultArnoldDriver.exrTiled', dec['defaultArnoldDriver.exrTiled'])
        mc.setAttr('defaultArnoldDriver.autocrop', dec['defaultArnoldDriver.autocrop'])
        mc.setAttr('defaultArnoldDriver.append', dec['defaultArnoldDriver.append'])
        mc.setAttr('defaultArnoldDriver.mergeAOVs', dec['defaultArnoldDriver.mergeAOVs'])
        mc.setAttr('defaultArnoldDriver.colorManagement', dec['defaultArnoldDriver.colorManagement'])
        mel.eval('setMayaSoftwareFrameExt("6", 0)')  #F/A.
        mc.setAttr('defaultRenderGlobals.extensionPadding', dec['defaultRenderGlobals.extensionPadding'])

    # Flame Range
    mc.setAttr('defaultRenderGlobals.byFrameStep', 1)
    mc.setAttr('defaultRenderGlobals.skipExistingFrames', dec['defaultRenderGlobals.skipExistingFrames'])
    mc.setAttr('defaultRenderGlobals.modifyExtension', 0)

    # renderableCamera
    mc.setAttr('perspShape.renderable', 1)
    mc.setAttr('topShape.renderable', 0)
    mc.setAttr('frontShape.renderable', 0)
    mc.setAttr('sideShape.renderable', 0)
    mc.setAttr('perspShape.renderable', 1)
    mc.setAttr('perspShape.mask', 1)
    mc.setAttr('perspShape.depth', 0)

    # imageSize
    mc.setAttr('defaultResolution.aspectLock', dec['defaultResolution.aspectLock'])
    mc.setAttr('defaultResolution.width', dec['defaultResolution.width'])
    mc.setAttr('defaultResolution.height', dec['defaultResolution.height'])
    mc.setAttr('defaultResolution.imageSizeUnits', dec['defaultResolution.imageSizeUnits'])
    mc.setAttr('defaultResolution.dotsPerInch', dec['defaultResolution.dotsPerInch'])
    mc.setAttr('defaultResolution.pixelDensityUnits', dec['defaultResolution.pixelDensityUnits'])

    arnoldRenderer()


def arnoldRenderer():
    global dec

    # sampling
    mc.setAttr('defaultArnoldRenderOptions.AASamples', dec['defaultArnoldRenderOptions.AASamples'])
    mc.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples', dec['defaultArnoldRenderOptions.GIDiffuseSamples'])
    mc.setAttr('defaultArnoldRenderOptions.GISpecularSamples', dec['defaultArnoldRenderOptions.GISpecularSamples'])
    mc.setAttr('defaultArnoldRenderOptions.GITransmissionSamples', dec['defaultArnoldRenderOptions.GITransmissionSamples'])
    mc.setAttr('defaultArnoldRenderOptions.GISssSamples', dec['defaultArnoldRenderOptions.GISssSamples'])
    mc.setAttr('defaultArnoldRenderOptions.GIVolumeSamples', dec['defaultArnoldRenderOptions.GIVolumeSamples'])
    mc.setAttr('defaultArnoldRenderOptions.enableProgressiveRender', dec['defaultArnoldRenderOptions.enableProgressiveRender'])

    # Adaptive Sampling
    mc.setAttr('defaultArnoldRenderOptions.enableAdaptiveSampling', dec['defaultArnoldRenderOptions.enableAdaptiveSampling'])
    mc.setAttr('defaultArnoldRenderOptions.AASamplesMax', dec['defaultArnoldRenderOptions.AASamplesMax'])
    mc.setAttr('defaultArnoldRenderOptions.AAAdaptiveThreshold', dec['defaultArnoldRenderOptions.AAAdaptiveThreshold'])

    # Clamping
    mc.setAttr('defaultArnoldRenderOptions.use_sample_clamp', dec['defaultArnoldRenderOptions.use_sample_clamp'])
    mc.setAttr('defaultArnoldRenderOptions.use_sample_clamp_AOVs', dec['defaultArnoldRenderOptions.use_sample_clamp_AOVs'])
    mc.setAttr('defaultArnoldRenderOptions.AASampleClamp', dec['defaultArnoldRenderOptions.AASampleClamp'])
    mc.setAttr('defaultArnoldRenderOptions.indirectSampleClamp', dec['defaultArnoldRenderOptions.indirectSampleClamp'])

    # Filter
    mc.setAttr('defaultArnoldFilter.aiTranslator', dec['defaultArnoldFilter.aiTranslator'], type='string')
    mc.setAttr('defaultArnoldFilter.width', dec['defaultArnoldFilter.width'])
    mc.setAttr('defaultArnoldFilter.scalarMode', dec['defaultArnoldFilter.scalarMode'])
    mc.setAttr('defaultArnoldFilter.filterWeights', dec['defaultArnoldFilter.filterWeights'])

    # Advanced
    mc.setAttr('defaultArnoldRenderOptions.lock_sampling_noise', dec['defaultArnoldRenderOptions.lock_sampling_noise'])
    mc.setAttr('defaultArnoldRenderOptions.sssUseAutobump', dec['defaultArnoldRenderOptions.sssUseAutobump'])
    mc.setAttr('defaultArnoldRenderOptions.indirectSpecularBlur', dec['defaultArnoldRenderOptions.indirectSpecularBlur'])

    # Ray Depth
    mc.setAttr('defaultArnoldRenderOptions.GITotalDepth', dec['defaultArnoldRenderOptions.GITotalDepth'])
    mc.setAttr('defaultArnoldRenderOptions.GIDiffuseDepth', dec['defaultArnoldRenderOptions.GIDiffuseDepth'])
    mc.setAttr('defaultArnoldRenderOptions.GISpecularDepth', dec['defaultArnoldRenderOptions.GISpecularDepth'])
    mc.setAttr('defaultArnoldRenderOptions.GITransmissionDepth', dec['defaultArnoldRenderOptions.GITransmissionDepth'])
    mc.setAttr('defaultArnoldRenderOptions.GIVolumeDepth', dec['defaultArnoldRenderOptions.GIVolumeDepth'])
    mc.setAttr('defaultArnoldRenderOptions.autoTransparencyDepth', dec['defaultArnoldRenderOptions.autoTransparencyDepth'])

    # Motion blur
    mc.setAttr('defaultArnoldRenderOptions.motion_blur_enable', dec['defaultArnoldRenderOptions.motion_blur_enable'])
    mc.setAttr('defaultArnoldRenderOptions.mb_object_deform_enable', dec['defaultArnoldRenderOptions.mb_object_deform_enable'])
    mc.setAttr('defaultArnoldRenderOptions.mb_camera_enable', dec['defaultArnoldRenderOptions.mb_camera_enable'])
    mc.setAttr('defaultArnoldRenderOptions.motion_steps', dec['defaultArnoldRenderOptions.motion_steps'])
    mc.setAttr('defaultArnoldRenderOptions.range_type', dec['defaultArnoldRenderOptions.range_type'])
    mc.setAttr('defaultArnoldRenderOptions.motion_frames', dec['defaultArnoldRenderOptions.motion_frames'])
    mc.setAttr('defaultArnoldRenderOptions.motion_start', dec['defaultArnoldRenderOptions.motion_start'])
    mc.setAttr('defaultArnoldRenderOptions.motion_end', dec['defaultArnoldRenderOptions.motion_end'])

    # Lights
    mc.setAttr('defaultArnoldRenderOptions.lowLightThreshold', dec['defaultArnoldRenderOptions.lowLightThreshold'])
    mc.setAttr('defaultArnoldRenderOptions.lightLinking', dec['defaultArnoldRenderOptions.lightLinking'])
    mc.setAttr('defaultArnoldRenderOptions.shadowLinking', dec['defaultArnoldRenderOptions.shadowLinking'])

    # Texturs
    mc.setAttr('defaultArnoldRenderOptions.autotx', dec['defaultArnoldRenderOptions.autotx'])
    mc.setAttr('defaultArnoldRenderOptions.use_existing_tiled_textures', dec['defaultArnoldRenderOptions.use_existing_tiled_textures'])
    mc.setAttr('defaultArnoldRenderOptions.textureAcceptUnmipped', dec['defaultArnoldRenderOptions.textureAcceptUnmipped'])
    mc.setAttr('defaultArnoldRenderOptions.autotile', dec['defaultArnoldRenderOptions.autotile'])
    mc.setAttr('defaultArnoldRenderOptions.textureAutotile', dec['defaultArnoldRenderOptions.textureAutotile'])
    mc.setAttr('defaultArnoldRenderOptions.textureAcceptUntiled', dec['defaultArnoldRenderOptions.textureAcceptUntiled'])
    mc.setAttr('defaultArnoldRenderOptions.textureMaxMemoryMB', dec['defaultArnoldRenderOptions.textureMaxMemoryMB'])
    mc.setAttr('defaultArnoldRenderOptions.textureMaxOpenFiles', dec['defaultArnoldRenderOptions.textureMaxOpenFiles'])
    mc.setAttr('defaultArnoldRenderOptions.textureDiffuseBlur', dec['defaultArnoldRenderOptions.textureDiffuseBlur'])
    mc.setAttr('defaultArnoldRenderOptions.textureSpecularBlur', dec['defaultArnoldRenderOptions.textureSpecularBlur'])
