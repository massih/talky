#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""[The talkative one :|]"""

__appname__ = "[Talky]"
__author__  = "MassiV"
__version__ = "0.0pre0"

import logging
import pyvona
import configparser

log = logging.getLogger(__name__)
CONFIG_FILE = 'config.ini'

def get_voice_object():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    if 'credentials' not in config:
        return 0

    credientials = config['credentials']
    return  pyvona.create_voice(access_key=credentials['AccessKey'], secret_key=credentials['SecretKey'])

def main():
    v = get_voice_object()
    v.speak('Hello world!')


if __name__ == '__main__':
        main()
