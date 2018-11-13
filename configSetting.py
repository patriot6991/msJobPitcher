import logging
import json
import os

class ReadJson(object):
    def __init__(self):
        self.config_dict = []

    def read(self, *args):
        logging.debug('config reading')
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
        f =open(path)
        self.config_dict = json.load(f)