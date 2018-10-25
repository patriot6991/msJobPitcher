# coding:UTF-8
import Ui
import logging

def develop():
    reload(Ui)


def execution():
    develop()
    logging.debug('excution msJobPitcher')

    Ui.ui()
