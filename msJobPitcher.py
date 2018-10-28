# coding:UTF-8
import Ui
import logging
import maya.mel as mel


def develop():
    reload(Ui)


def execution():
    develop()
    logging.debug('excution msJobPitcher')

    mel.eval('setProject "//172.29.44.4/cg/ms06/renderProJ" ;')

    Ui.ui()
