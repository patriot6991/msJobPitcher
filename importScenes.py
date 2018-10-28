import maya.cmds as mc
import os.path
import logging
import maya.mel as mel


def importScenes():
    logging.debug('importScens')
    fPath = r''
    fPath = r"{}".format(fPath)
    ftype = ""

    fName = os.path.basename(fPath)
    root, ext = os.path.splitext(fPath)
    nSpace = fName.replace(ext, "")
    fbxFPath = fPath.replace("\\", "/")

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