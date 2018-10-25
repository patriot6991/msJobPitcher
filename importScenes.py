import maya.cmds as mc
import os.path


def importScenes():
    fPath = ''
    ftype = ""

    fName = os.path.basename(fPath)
    root, ext = os.path.splitext(fPath)
    nSpace = fName.replace(ext, "")

    if ext == ".ma":
        ftype = "mayaAscii"

    elif ext == ".mb":
        ftype = "mayaBinary"

    elif ext == ".fbx":
        ftype = "Fbx"

    elif ext == ".obj":
        ftype = "OBJ"

    else:
        print "Please .ma,.mb,.obj,.fbx"

    mc.file("{}".format(fPath), i=True, typ="{}".format(ftype), iv=True, ra=True, ns="{}".format(nSpace), op="v=0;",
            pr=True)


if mc.window('testWin', exists=True):
    mc.deleteUI('testWin')

