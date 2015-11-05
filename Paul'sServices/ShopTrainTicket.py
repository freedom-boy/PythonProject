#!/usr/bin/env python
#_*_coding:utf-8_*_
#作者:Paul哥
import urllib2,cookielib,random,urllib,thread
import LoginAccount
from time import sleep
LoginRun=LoginAccount.Login()
from PIL import Image

class ShopTicket:

	def __init__(self):
		self.Imagesuffix=random.random() #验证码请求尾部随机数字
		self.ImageUrl='https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=login&rand=sjrand&'+str(self.Imagesuffix) #验证码请求URL
		self.checkcodeurl='https://kyfw.12306.cn/otn/passcodeNew/checkRandCodeAnsyn' #12306检测验证码对错的url
		self.checkloginurl='https://kyfw.12306.cn/otn/login/loginAysnSuggest'#12306检测用户名密码验证码对错的url
		self.loginurl='https://kyfw.12306.cn/otn/index/initMy12306' #12306正式登陆页面URL
		self.mainurl='https://kyfw.12306.cn/otn/'#请求12306前半部分链接

		self.accessHeaders={
			'Host': 'kyfw.12306.cn',
			'Connection': 'keep-alive',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
			'Referer': 'https://kyfw.12306.cn/otn/',
			#'Accept-Encoding': 'gzip, deflate, sdch',
			'Accept-Language': 'zh-CN,zh;q=0.8'

		} #12306HTTP请求头

		self.codedict={'1':'40,75','2':'110,75','3':'180,75','4':'250,75','5':'40,150','6':'110,150','7':'180,150','8':'250,150'}
		#坐标对应数字

		self.cookie=cookielib.CookieJar()  #cookie制作器
		self.cookieHandler=urllib2.HTTPCookieProcessor(self.cookie)
		self.opener=urllib2.build_opener(self.cookieHandler)
		urllib2.install_opener(self.opener)

	def inputuserandpasswd(self):
		username=raw_input('Please input your username:')
		password=raw_input('Please input your password:')
		userpassdict={'user':username,'passwd':password}
		return userpassdict

	def login(self):
		userpass=self.inputuserandpasswd()
		while True:
			for i in range(3):
				getimagestatus=LoginRun.GetCodeImage()
				if getimagestatus=='GetImageSuccess':
					break
				else:
					pass
			coodestr=LoginRun.PostLoginInfo()
			if coodestr=='checkcodeTrue':
				print 'Checkcode is True'
				break
			elif coodestr=='checkcodeFalse':
				continue




		return userpass



















	def ShopRun(self):
		print "Welcome to Paul's service center,how can I help you?"
		print "1.Buy trainticket"
		print "2.With old liu goint to BigBaoJian "
		print "3.With oil brother going to learning ControlGirl'sThought"
		ServiceNum=input('Please input number:')
		if ServiceNum==1:
			a=self.login()




if __name__=="__main__":
	Service=ShopTicket()
	Service.ShopRun()


