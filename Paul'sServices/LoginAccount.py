#!/usr/bin/env python
#_*_coding:utf-8_*_
#作者:Paul哥
import urllib2,cookielib,random,urllib
from PIL import Image

class Login:

	def __init__(self):

		self.indexurl='https://kyfw.12306.cn/otn/login/init'
		self.checkcodeurl='https://kyfw.12306.cn/otn/passcodeNew/checkRandCodeAnsyn'
		self.loginurl='https://kyfw.12306.cn/otn/login/loginAysnSuggest'
		self.userlogin='https://kyfw.12306.cn/otn/login/userLogin'
		self.mainurl='https://kyfw.12306.cn/otn/'
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

		self.codedict={'1':'40,75','2':'110,75','3':'180,75','4':'250,75','5':'40,150','6':'110,150','7':'180,150','8':'250,150'}

		self.cookie=cookielib.CookieJar()
		self.cookieHandler=urllib2.HTTPCookieProcessor(self.cookie)
		self.opener=urllib2.build_opener(self.cookieHandler)
		urllib2.install_opener(self.opener)
		self.Imagesuffix=random.random()
		self.ImageUrl='https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=login&rand=sjrand&'+str(self.Imagesuffix)

	def GetCodeImage(self):
		request=urllib2.Request(self.ImageUrl,headers=self.accessHeaders)
		response=urllib2.urlopen(request)
		codeimage=response.read()
		file=open('code.jpg','wb')
		file.write(codeimage)
		file.flush()
		file.close()
		img=Image.open('code.jpg')
		img.show()

		return self.cookie


	def PostLoginInfo(self):
		codestr=''
		Input=raw_input('Please input code number:')
		for i in Input:
			codestr=codestr + self.codedict[i]+','

		codestr=codestr[:-1]

		data={"randCode":str(codestr),"rand":'sjrand'}
		data=urllib.urlencode(data)
		print data
		request=urllib2.Request(self.checkcodeurl,headers=self.accessHeaders,data=data)
		response=urllib2.urlopen(request)
		print response.read()
		return str(codestr)

	def StartLogin(self,codestr):
		username=raw_input('Please input your username:')
		password=raw_input('Please input your password:')
		data={"loginUserDTO.user_name":username,"userDTO.password":password,"randCode":codestr}
		postdata=urllib.urlencode(data)
		print postdata
		request=urllib2.Request(self.loginurl,headers=self.accessHeaders,data=postdata)
		response=urllib2.urlopen(request)

		request1=urllib2.Request(self.userlogin,headers=self.accessHeaders,data='{"_json_att":''}')
		response1=urllib2.urlopen(request1)
		request2=urllib2.Request('https://kyfw.12306.cn/otn/index/initMy12306',headers=self.accessHeaders)
		response3=urllib2.urlopen(request2)
		print response3.read()

	def access12306(self,halfurl):
		request=urllib2.Request(url=self.mainurl+halfurl,headers=self.accessHeaders)
		response=urllib2.urlopen(request)
		return response















if __name__=='__main__':
	test=Login()
	test.GetCodeImage()
	codestr=test.PostLoginInfo()
	test.StartLogin(codestr)
