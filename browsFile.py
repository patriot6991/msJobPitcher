import logging
import maya.cmds as mc


basicFiles = "All Files(*.*);;MayaFiles(*.ma *.mb);;Maya Ascii(*.ma);;Maya Binary(*.mb);;OBJ(*.obj);;FBX(*.fbx)"

def search(defPath=''):
    selectFiles = mc.fileDialog2(ff=basicFiles,fm=1,ds=1,dir=defPath,caption="selectFiles")
    selectFiles = r"{}".format(selectFiles[0])
    return selectFiles