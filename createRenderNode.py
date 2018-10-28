import maya.cmds as mc
import logging

def create():
    logging.debug('create Render Node')
    caov = mc.ls(typ='aiAOV')
    cnt = len(caov)
    if cnt >= 1:
        for i in range(cnt):
            mc.delete(caov[i])

    caof = mc.ls(typ='aiAOVFilter')
    cnt = len(caof)
    if cnt >= 1:
        for i in range(cnt):
            if caof[i] != 'defaultArnoldFilter':
                mc.delete(caof[i])

    caod = mc.ls(typ='aiAOVDriver')
    cnt = len(caod)
    if cnt >= 1:
        for i in range(cnt):
            if caod[i] != 'defaultArnoldDriver':
                mc.delete(caod[i])

    caro = mc.ls(typ='aiOptions')
    if 'defaultArnoldRenderOptions' not in caro:
        mc.createNode('aiOptions', n='defaultArnoldRenderOptions')
        mc.createNode('aiAOVDriver', n='defaultArnoldDisplayDriver')
        mc.connectAttr('defaultArnoldDisplayDriver.message', 'defaultArnoldRenderOptions.drivers[0]')
    if 'defaultArnoldFilter' not in caof:
        mc.createNode('aiAOVFilter', n='defaultArnoldFilter')
    if 'defaultArnoldDriver' not in caod:
        mc.createNode('aiAOVDriver', n='defaultArnoldDriver')