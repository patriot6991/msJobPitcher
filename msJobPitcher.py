# coding:UTF-8
import Ui
import logging
import maya.mel as mel
import myLogger
import maya.cmds as mc


def develop():
    reload(Ui)
    reload(myLogger)


def execution():
    develop()

    a = myLogger.MyLogger(mc=mc)
    a.changeToDebug()

    logging.debug('excution msJobPitcher')

    mel.eval('setProject "//172.29.44.4/cg/ms06/renderProJ" ;')

    b = Ui.UiClass()
    b.ui()
