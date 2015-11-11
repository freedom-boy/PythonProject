#!/usr/bin/env python
#_*_coding:utf-8_*_

import time,uuid,functools,logging
import threading
#This is a database engine object

class _Engine(object):

    def __init__(self,connect):
        self._connect=connect

    def connect(self):
        return self._connect()

engine=None

#Hold database connect

class _DbCtx(threading.local):
    def __init__(self):
        self.connection=None
        self.transactions=0
    def is_init(self):
        return not self.connection is None
    def init(self):
        self.connection=_LasyConnection()
        self.transactions=0

    def cleanup(self):
        self.connection.cleanup()
        self.connection=None

