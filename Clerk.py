# coding: utf-8

import time
import pickle
import socket
import random
import logging
import argparse
import threading


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M:%S')
logger = logging.getLogger('Clerk')


class Clerk(threading.Thread):
    def __init__(self, port=5003, ide=3):
        threading.Thread.__init__(self)
        self.id = ide
        self.port = port
    def run(self):
        pass
