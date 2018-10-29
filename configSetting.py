import logging
import json
import os

class ReadJson(object):
    def __init__(self):
        self.projectPath = ''
        self.stagePath = ''
        self.renderSettingPath = ''
        self.AOVsSettingPath = ''
        self.deadlineSettingPath = ''

    def read(self, *args):
        logging.debug('config reading')
        f =open('C:\Users\user\PycharmProjects\msJobPitcher\config.json')
        a = json.load(f)
        for k, v in a.items():
            self.k = v
            logging.debug('%s --> %s' %(k, self.k))