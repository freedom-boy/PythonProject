#!/usr/bin/env python
#_*_coding:utf-8_*_
#作者:Paul哥
import urllib2,os,cookielib

class Login:

	def __init__(self):

		self.indexurl='https://kyfw.12306.cn/otn/login/init'
		self.accessHeaders={
			'Host': 'kyfw.12306.cn',
			'Connection': 'keep-alive',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
			'Referer': 'https://kyfw.12306.cn/otn/',
			#'Accept-Encoding': 'gzip, deflate, sdch',
			'Accept-Language': 'zh-CN,zh;q=0.8'

		}






		self.username='mymicheel'
		self.password='Hello123'
		self.cookie=cookielib.LWPCookieJar()
		self.cookieHandler=urllib2.HTTPCookieProcessor(self.cookie)
		self.opener=urllib2.build_opener(self.cookieHandler,urllib2.HTTPHandler)


	def GetUrl(self):
		request=urllib2.Request(self.indexurl,headers=self.accessHeaders)
		response=urllib2.urlopen(request)
		print response.read()



if __name__=='__main__':
	test=Login()
	test.GetUrl()
