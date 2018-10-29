import logging
import json
import os

class ReadJson(object):
    def __init__(self):
        self.config_dict = []

    def read(self, *args):
        logging.debug('config reading')
        f =open('C:\Users\user\PycharmProjects\msJobPitcher\config.json')
        self.config_dict = json.load(f)