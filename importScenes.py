import maya.cmds as mc
import os.path
import logging
import maya.mel as mel

def importScenes():
    logging.debug('importScens')
    fPath = mc.textField(text1, q=True, text=True)
    fPath = r"{}".format(fPath)
    ftype = ""

    fName = os.path.basename(fPath)
    root, ext = os.path.splitext(fPath)
    nSpace = fName.replace(ext, "")
    fbxFPath = fPath.replace("\\","/")

    if ext == ".ma":
        ftype = "mayaAscii"

    elif ext == ".mb":
        ftype = "mayaBinary"

    elif ext == ".fbx":
        mel.eval('FBXImport -f "{}" ;'.format(fbxFPath))
        return

    elif ext == ".obj":
        ftype = "OBJ"

    else:
        print "Please .ma,.mb,.obj,.fbx"

    mc.file("{}".format(fPath), i=True, typ="{}".format(ftype), iv=True, ra=True, ns="{}".format(nSpace), op="v=0;",
            pr=True)


if mc.window('testWin', exists=True):
    mc.deleteUI('testWin')
win = mc.window('testWin', t='testWin', widthHeight=(200,100))
mc.columnLayout(adj=True)

test1 = mc.textField('text1',w=130, pht='filepath')
mc.button(w=50, h=30, l='Run', c='importScenes()')

mc.showWindow(win)
