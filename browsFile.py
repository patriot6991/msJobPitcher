import logging
import maya.cmds as mc


basicFiles = "MayaFiles(*.ma *.mb);;Maya Ascii(*.ma);;Maya Binary(*.mb);;OBJ(*.obj);;FBX(*.fbx);;All Files(*.*)"

def search(defPath=''):
    selectFiles = mc.fileDialog2(ff=basicFiles,fm=1,ds=1,dir=defPath,caption="selectFiles")
    selectFiles = r"{}".format(selectFiles)
    return selectFiles