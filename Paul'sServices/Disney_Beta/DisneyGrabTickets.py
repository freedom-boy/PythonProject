#!/usr/bin/env python
#_*_coding:utf-8_*_
#作者:Paul哥
import urllib2,cookielib,random,urllib,json,re
import RequestFunctions
ReqFunc=RequestFunctions.Functions()
import webbrowser

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Disney:

	def __init__(self):
		self.availableUrl='https://www.shanghaidisneyresort.com/tickets/'
		self.loginUrl='https://www.shanghaidisneyresort.com/login/'
		self.processdUrl='https://www.shanghaidisneyresort.com/checkout/proceed/'
		self.expressUrl='https://www.shanghaidisneyresort.com/checkout/express/'
		self.confirmationUrl='https://www.shanghaidisneyresort.com/checkout/confirmation/'
		self.jumpAlipayUrl='https://mapi.alipay.com/gateway.do?_input_charset=utf-8'
		self.cookie=cookielib.CookieJar()
		self.cookieHandler=urllib2.HTTPCookieProcessor(self.cookie)
		self.opener=urllib2.build_opener(self.cookieHandler)
		urllib2.install_opener(self.opener)
		self.disneyHeaders={
			'Host': 'www.shanghaidisneyresort.com',
			'Connection': 'keep-alive',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			#Upgrade-Insecure-Requests: 1
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36',
			'Referer': 'https://www.shanghaidisneyresort.com/',
			#Accept-Encoding: gzip, deflate, sdch
			'Accept-Language': 'zh-CN,zh;q=0.8'
			}

	def CheckHaveTicket(self):
		try:
			haveTicketData=ReqFunc.GetFunction(geturl=self.availableUrl,headers=self.disneyHeaders,timeout=5)
			return haveTicketData
		except:
			return 'GetError'

	def GetLoginUrl(self):    #获取登录pep_csrf key
		resp=ReqFunc.GetFunction(geturl=self.loginUrl,headers=self.disneyHeaders,timeout=3)
		pep_csrf= re.search(r'value=\"(.*?)\"',str(resp),re.DOTALL)
		pepstr=pep_csrf.group(1)
		return pepstr

	def Login(self,pep_csrf,username,passwd):  #登录
		data={'pep_csrf':pep_csrf,'returnUrl':'/','username':username,'password':passwd,'rememberMe':'0','&lid=Submit_Link':''}
		postdata=urllib.urlencode(data)
		resp=ReqFunc.PostFunction(posturl=self.loginUrl,header=self.disneyHeaders,postdata=postdata)
		return resp

	def Booking(self,pepstr,adultTotal,childTotal,seniorTotal,selectedDate,daysTotal,lastName,firstName,email):
		numDaysElementId='shdr-theme-park-'+daysTotal
		numDays='shdr-theme-park-'+daysTotal
		ticketProducts=[]
		if int(adultTotal)>0:
			aStatusCode='A'
			ticketProducts.append({"quantity":adultTotal,"ticketProduct":"/api/wdpro/lexicon-view-assembler-service/product-instances/shdr-theme-park_%s_%s_0_0_RF_AF_SOF?view=web&storeId=shdr" % (daysTotal,aStatusCode)})
		if int(childTotal)>0:
			cStatusCode='C'
			ticketProducts.append({"quantity":adultTotal,"ticketProduct":"/api/wdpro/lexicon-view-assembler-service/product-instances/shdr-theme-park_%s_%s_0_0_RF_AF_SOF?view=web&storeId=shdr" % (daysTotal,cStatusCode)})
		if int(seniorTotal)>0:
			sStatusCode='S'
			ticketProducts.append({"quantity":adultTotal,"ticketProduct":"/api/wdpro/lexicon-view-assembler-service/product-instances/shdr-theme-park_%s_%s_0_0_RF_AF_SOF?view=web&storeId=shdr" % (daysTotal,sStatusCode)})
		processdDataDict={'pep_csrf':pepstr,'adultTotal':adultTotal,'childTotal':childTotal,'seniorTotal':seniorTotal,'selectedDate':selectedDate,'daysTotal':daysTotal,'numDaysElementId':numDaysElementId,'numDays':numDays,'ticketBuilderId':'MYW','productTypeId':'shdr-theme-park','productCategory':'themepark','addToCart':'','ticketProducts':ticketProducts}
		processdData=urllib.urlencode(processdDataDict)
		proceedResp=ReqFunc.PostFunction(posturl=self.processdUrl,header=self.disneyHeaders,postdata=processdData)
		if proceedResp=='PostError':
			return 'PostError'
		expressDataDict={
		'pep_csrf'	:pepstr,
		'hiddenAction':'purchase',
		'lastName'	:lastName,
		'firstName'	:firstName,
		'acceptedTermsAndConditions':	'1',
		'deliveryPhone'	:'',
		'deliveryConfirmPhone':	'',
		'deliveryMethod':	'email',
		'deliveryEmail':	email,
		'deliveryConfirmEmail':email,#'eros.tany@gmail.com'
		'addToGovernmentId':	'0',
		'idNumber':	'',
		'confirmIdNumber':''	,
		'paymentMethod':	'ALIPAY',
		'doneButton':	''
		}
		expressData=urllib.urlencode(expressDataDict)
		expressData=expressData+'&acceptedTermsAndConditions=0'
		expressResp=ReqFunc.PostFunction(posturl=self.expressUrl,header=self.disneyHeaders,postdata=expressData)
		if expressResp=='PostError':
			return 'PostError'
		return proceedResp+expressResp

	def GotoPay(self,pepstr):
		confirUrl='https://www.shanghaidisneyresort.com/checkout/confirmation/payment/?csrf='+pepstr
		jumpPayResult=ReqFunc.GetFunction(geturl=confirUrl,headers=self.disneyHeaders,timeout=5)
		return jumpPayResult

	def Run(self,bookingDate,lastName,firstName,email,username,passwd,payname):
		#print '请全部输入数字'
		# adultTotal=raw_input('您需要几张成人票:')
		# childTotal=raw_input('您需要几张儿童票:')
		# seniorTotal=raw_input('您需要几张老人票:')
		# selectedDate=raw_input('请输入您的到访日期(格式xxxx-xx-xx):')
		# daysTotal=raw_input('您选择一日游还是两日游:')
		adultTotal='1'
		childTotal='0'
		seniorTotal='0'
		selectedDate=bookingDate
		daysTotal='1'
		pepstr=self.GetLoginUrl()
		if pepstr=='GetError':
			print u'获取登录pepkey失败'
			return 'GetError'
		loginResult=self.Login(pepstr,username,passwd)
		if loginResult=='PostError':
			print u'登录失败，重试。。。'
			return 'PostError'
		bookingResult=self.Booking(pepstr,adultTotal,childTotal,seniorTotal,selectedDate,daysTotal,lastName,firstName,email)
		if bookingResult=='PostError':
			print u'预定失败，重试。。。'
			return 'PostError'
		if '很抱歉，您所要求的门票目前无法购买。请重新选择' or '很抱歉，您所要求的门票目前无法购买' in bookingResult:
			return 'BookingError'
		else:
			jumpPayParameter=self.GotoPay(pepstr)
			if jumpPayParameter=='GetError':
				return 'BookingError'
			else:
				PayPage=open(payname,'wb')
				PayPage.write(jumpPayParameter)
				PayPage.close()
				webbrowser.open(payname)
				print u'请在打开的支付宝页面支付，三十分钟内有效！'
				return 'BookingOK'

	def SendMessages(self,value):
		sendheaders={
			#'Host':'ws.messagegateway.ctripcorp.com',
			'Content-Type':'application/json'
			#'Content-Length': 'length',

		}
		#sendurl='http://ws.messagegateway.ctripcorp.com/messageplatformservice/api/SendMessage'
		sendurl='http://ws.messagegateway.ctripcorp.com/messageplatformservice/api/sendmessage'
		msgstring='141.205，您预定的'+str(value)+'张迪士尼门票已抢到，请在25分钟内扫码支付！'
		msgbody='{\"ChannelInfo\":{\"MobilePhone\":\"18610817561\",\"ScheduleTime\":\"2016-04-07T15:31:37.2139167+08:00\"},\"Content\":{\"Content\":\"%s\"}}' % msgstring
		msgbody=json.dumps(msgbody)
		data='{"MessageCode":290019,"MsgBody":%s,"UID":null,"OrderID":0,"EID":null,"ExpiredTime":null}' % msgbody

		request=urllib2.Request(url=sendurl,headers=sendheaders,data=data)
		try:
			response=urllib2.urlopen(request,timeout=2)
			return response.read()
		except:
			print 'SendErr'
			return 'SendError'



	def MainRun(self):
		count=0
		while True:
			count+=1
			lastName=u'谈'
			firstName=u'寅'
			email='eros.tany@gmail.com'
			username='844988963@qq.com'
			passwd='Lenovo456'
			bookingDate='2016-06-16'
			payname='pay%s.html' % str(count)
			haveTicket=self.CheckHaveTicket()
			if haveTicket=='GetError':
				continue
			allAvailable=re.search(r'availableDates\&quot\;\:\[(.*?)\;\]',haveTicket,re.DOTALL)
			try:
				allAvailableDate=allAvailable.group(1)
			except:
				continue

			if bookingDate in allAvailableDate:
				print bookingDate,u'有票啦'
				BookingResult=self.Run(bookingDate,lastName,firstName,email,username,passwd,payname)
				if BookingResult in ['BookingError','GetError','PostError']:
					print u'有票，扣位失败，重试。。。'
					continue
				elif BookingResult=='BookingOK':
					sendStatus=self.SendMessages('1')
					if sendStatus=='SendError':
						self.SendMessages('1')
				else:
					continue
			else:
				print u'无票，继续刷,第%d次' % count



if __name__ == '__main__':
	TestRun=Disney()
	TestRun.MainRun()



