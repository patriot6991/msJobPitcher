import logging


class MyLogger(object):
    def __init__(self, mc):
        logging.basicConfig(level=logging.INFO)
        self.my_logger = logging.getLogger()
        self.mc = mc


    def changeToInfo(self, *args):
        self.my_logger.setLevel(logging.INFO)
        logging.info('change to info mode')


    def changeToDebug(self, *args):
        self.my_logger.setLevel(logging.DEBUG)
        logging.info('change to debug mode')


    def createCheckbox(self, v, *args):
        return self.mc.checkBox(l='log Level', v=v, onc=self.changeToDebug, ofc=self.changeToInfo)