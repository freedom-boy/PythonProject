#!/usr/bin/env python
#_*_coding:utf-8_*_
#author=Paul

import urllib,urllib2,base64,StringIO,gzip

class Functions:


	def GetFunction(self,geturl,headers,timeout):
		request=urllib2.Request(geturl,headers=headers)
		try:
			response=urllib2.urlopen(request,timeout=timeout)
			return response.read()
		except urllib2.HTTPError,e:
			print 'error code',e.code
			return 'GetError'
		except urllib2.URLError,e:
			print 'Reason',e.reason
			return 'GetError'
		except:
			return 'GetError'

	def PostFunction(self,posturl,header,postdata,timeout=5):
		request=urllib2.Request(url=posturl,headers=header,data=postdata)
		try:
			response=urllib2.urlopen(request,timeout=timeout)
			return response.read()
		except urllib2.HTTPError,e:
			print 'error code',e.code
			return 'PostError'
		except urllib2.URLError,e:
			print 'Reason',e.reason
			return 'PostError'
		except:
			return 'PostError'


	def DatatoBase64(self,obj):
		try:
			basestring=base64.b64encode(obj)
			return basestring
		except:
			return 'Tobase64Error'

	def GzipDeco(self,flow):
		try:
			buf=StringIO.StringIO(flow)
			f=gzip.GzipFile(fileobj=buf)
			data=f.read()
			f.close()
			return data
		except:
			return 'GzipFileError'

