import maya.cmds as mc
import logging
import searchFiles


def saveScene(shotID, path):
    logging.debug('save scene')
    path = path + r'\scenes'
    fileName = "{}.render".format(shotID)
    mc.file(rename=r"%s\{}.ma".format(fileName) %(path))
    mc.file(save=True, type="mayaAscii")

