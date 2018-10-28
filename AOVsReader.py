import maya.cmds as mc
import json
import logging

path = r'\\172.29.44.4\cg\ms06\msJobPitcher\AOVs\aov.json'

def AOVsRead():
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
    
    logging.debug('AOVsRead')
    get = open(path)
    a = json.load(get)
    b = a['arnold']

    for z in b.keys():
        if z == 'outputs':
            y = b[z]
            cnt = len(y)
            for i in range(cnt):
                x = y[i]
                for w in x.keys():
                    v = x[w]
                    u = v[0]
                    mc.connectAttr('{}.message'.format(u['filter']), '{}.outputs[0].filter'.format(w))
                    mc.connectAttr('{}.message'.format(u['driver']), '{}.outputs[0].driver'.format(w))
                    mc.connectAttr('{}.message'.format(w), 'defaultArnoldRenderOptions.aovList[{}]'.format(i))
            break
        aovs = b[z]
        cnt = len(aovs)
        for i in range(cnt):
            c = aovs[i]
            for d in c.keys():
                e = c[d]
                if z == 'aovs':
                    mc.createNode('aiAOV', n='{}'.format(d))

                elif z == 'drivers':
                    if d != 'defaultArnoldDriver':
                        mc.createNode('aiAOVDriver', n='{}'.format(d))

                elif z == 'filters':
                    if d != 'defaultArnoldFilter':
                        mc.createNode('aiAOVFilter', n='{}'.format(d))

                for f in e.keys():
                    atr = mc.getAttr(f, typ=True)
                    if atr == 'string':
                        mc.setAttr(f, e[f], type='string')             
                    else:
                        if atr == 'message':
                            continue
                        mc.setAttr(f, e[f])
