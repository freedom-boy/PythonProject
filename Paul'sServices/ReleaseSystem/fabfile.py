#!/usr/bin/env python
#_*_coding:utf-8_*_
#作者:Paul哥



from fabric.api import settings,run,cd,env,hosts
from fabric.colors import *

env.hosts=['192.168.75.130:22']
env.password='hello123'
env.user='root'
def test():
	with cd('/home'):
		print yellow(run('ls -l'))

test()
