#!/usr/bin/env python
#_*_coding:utf-8_*_
#author=Paul

import json,urllib,urllib2,cookielib,datetime

class BookingTicket:

	def __init__(self):
		self.keepLoginStatusUrl='http://xunlongferry.weixin.swiftpass.cn/xunlong/pc/user/isLogin'
		self.loginUrl='http://xunlongferry.weixin.swiftpass.cn/xunlong/pc/user/login'
		self.queryUrl='http://xunlongferry.weixin.swiftpass.cn/xunlong/pc/sailingsJson'
		self.goqueryUrl=''
		self.bookingUrl='http://xunlongferry.weixin.swiftpass.cn/xunlong/pc/submitOrder'
		self.goSubmitOrderUrl='http://xunlongferry.weixin.swiftpass.cn/xunlong/pc/goSubmitOrder'
		self.checkPayUrl='http://xunlongferry.weixin.swiftpass.cn/xunlong/pc/personCenter/orderList?currentPage=0&statusNo=0'
		self.loginHeaders={
			'Host': 'xunlongferry.weixin.swiftpass.cn',
			'Connection': 'keep-alive',
			'Accept': 'application/json, text/javascript, */*; q=0.01',
			'Origin': 'http://xunlongferry.weixin.swiftpass.cn',
			'X-Requested-With': 'XMLHttpRequest',
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36',
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Referer': 'http://xunlongferry.weixin.swiftpass.cn/xunlong/pc/user/login?user=member',
			#Accept-Encoding: gzip, deflate
			'Accept-Language': 'zh-CN,zh;q=0.8'
		}


		self.startSiteDict={"珠海九洲":"ZH","深圳蛇口":"SK","香港港澳":"HKM","香港机场":"HKA","深圳机场":"FY","澳门氹仔":"MAC","澳门外港":"MMF"}
		self.arriveSiteDict={"珠海九洲":"ZH","香港港澳":"HKM","香港机场":"HKA","澳门氹仔":"MAC","澳门外港":"MMF"}
		self.week_day_dict = {
			    '0' : '周日',
			    '1' : '周一',
			    '2' : '周二',
			    '3' : '周三',
			    '4' : '周四',
			    '5' : '周五',
			    '6' : '周六',
			  }
		self.cookie=cookielib.CookieJar()  #cookie制作器
		self.cookieHandler=urllib2.HTTPCookieProcessor(self.cookie)
		self.opener=urllib2.build_opener(self.cookieHandler)
		urllib2.install_opener(self.opener)

	def KeepLoginStatus(self,head):
		keeploginRequest=urllib2.Request(url=self.keepLoginStatusUrl,data="",headers=head)
		keepResponse=urllib2.urlopen(keeploginRequest)
		print keepResponse.read()

	def Login(self,userName,passWord):
		loginDataDict={"user":"member","username":userName,"password":passWord,"auto":"0"}
		loginData=urllib.urlencode(loginDataDict)
		loginRequest=urllib2.Request(url=self.loginUrl,headers=self.loginHeaders,data=loginData)
		try:
			response=urllib2.urlopen(loginRequest,timeout=3)
			return response.read()

		except:
			return "Login Error"

	def Query(self,startSite,arriveSite,toDate,backDate=""):
		toDateValue=toDate[0:4]+'-'+toDate[4:6]+'-'+toDate[6:8]
		toDate2=toDate[4:6]+'月'+toDate[6:8]+'日'
		toWeek=self.week_day_dict[str(datetime.datetime(int(toDate[0:4]),int(toDate[4:6]),int(toDate[6:8])).strftime("%w"))]
		startSiteStr=self.startSiteDict[startSite]
		arriveSiteStr=self.arriveSiteDict[arriveSite]
		lindID=startSiteStr+'-'+arriveSiteStr
		if backDate!="":
			backDateValue=toDate[0:4]+'-'+toDate[4:6]+'-'+toDate[6:8]
			backDate2=toDate[4:6]+'月'+toDate[6:8]+'日'
			backWeek=self.week_day_dict[str(datetime.datetime(int(toDate[0:4]),int(toDate[4:6]),int(toDate[6:8])).strftime("%w"))]
		else:
			backDateValue=""
			backDate2=""
			backWeek=""
		queryDataDict={"userType":"member","startSite":startSiteStr,"endSite":arriveSiteStr,"toDate":toDateValue,"toDate2":toDate2,"toWeek":toWeek,"backDate":backDateValue,"backDate2":backDate2,"backWeek":backWeek,"endSiteName":startSite,"startSiteName":arriveSite,"sailingType":"0","lineId":lindID,"airportTime":"","toTime":"","lineType":"LTP001"}
		queryData=urllib.urlencode({"siteResJson":queryDataDict})

		queryRequest=urllib2.Request(url=self.queryUrl,headers=self.loginHeaders,data=queryData)
		response=urllib2.urlopen(queryRequest)
		return  queryData

	def Booking(self,querydreferer):
		gosubmitReferer='http://xunlongferry.weixin.swiftpass.cn/xunlong/pc/sailings?'+str(querydreferer)
		gosubmitHeaders={
			'Host': 'xunlongferry.weixin.swiftpass.cn',
			'Connection': 'keep-alive',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36',
			'Referer':gosubmitReferer,
			#Accept-Encoding: gzip, deflate, sdch
			'Accept-Language': 'zh-CN,zh;q=0.8'
		}

		submitHeader={
			'Host': 'xunlongferry.weixin.swiftpass.cn',
			'Connection': 'keep-alive',
			'Content-Length': '167',
			'Accept': 'application/json, text/javascript, */*; q=0.01',
			'Origin': 'http://xunlongferry.weixin.swiftpass.cn',
			'X-Requested-With': 'XMLHttpRequest',
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36',
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Referer': 'http://xunlongferry.weixin.swiftpass.cn/xunlong/pc/goSubmitOrder',
			#Accept-Encoding: gzip, deflate
			'Accept-Language': 'zh-CN,zh;q=0.8'
		}
		#self.KeepLoginStatus(gosubmitHeaders)
		goSubMitOrderRequest=urllib2.Request(self.goSubmitOrderUrl,headers=gosubmitHeaders)
		goSubresponse=urllib2.urlopen(goSubMitOrderRequest)

		#self.KeepLoginStatus(gosubmitHeaders)
		goPricelist='[{"userType":"URT001","userTypeName":"成人票","price":"120","priceId":"42122877","discountId":"1"}]'
		bookingDataDict={"vouchersCode":"","goPriceList":goPricelist,"backPriceList":"[]","userPhone":"18610817561"}
		bookingData=urllib.urlencode(bookingDataDict)
		bookingRequest=urllib2.Request(url=self.bookingUrl,headers=submitHeader,data=bookingData)
		response=urllib2.urlopen(bookingRequest)
		return response.read()



	def StartRun(self):
		userName=raw_input('please input your username:')
		passWord=raw_input("please input your password:")
		loginResult=self.Login(userName,passWord)
		print '以下为出发站:'
		for k,v in self.startSiteDict.items():
			print k
		startSite=raw_input('please input your startSite:')
		print '以下为到达站:'
		for k,v in self.arriveSiteDict.items():
			print k
		endSite=raw_input('please input your endSite:')
		arrivedate=raw_input('please input your arrive date:')
		queryResult=self.Query(startSite=startSite,arriveSite=endSite,toDate=arrivedate)
		bookingResult=self.Booking(queryResult)
		print bookingResult
		payRequest=urllib2.Request(url=self.checkPayUrl,headers=self.loginHeaders)
		PayList=urllib2.urlopen(payRequest)
		print PayList.read()





if __name__=="__main__":
	MainPro=BookingTicket()
	MainPro.StartRun()