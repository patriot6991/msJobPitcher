import maya.cmds as mc
import json
import logging

path = ''

def AOVsRead():
    logging.debug('AOVsRead')
    get = open(path)
    a = json.load(get)
    b = a['arnold']

    #AOVs
    for z  in b.keys():
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