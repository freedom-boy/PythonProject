#!/usr/bin/env python
#_*_coding:utf-8_*_
#作者:Paul哥
import urllib2,re,json,random

ranNum=random.random()
availableUrl='http://item.damai.cn/ajax/getPriceList.html?projectId=95181&performId=8740765&t='+str(ranNum)
loginHeaders={
			'Connection': 'keep-alive',
			'Content-Type':'text/html; charset=utf-8',
			#Upgrade-Insecure-Requests: 1
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36',
			'Referer': 'https://www.shanghaidisneyresort.com/',
			'Server':'Tengine',
			}

def GetFunction(geturl,headers,timeout):
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

def SendMessages(value):
		sendheaders={
			#'Host':'ws.messagegateway.ctripcorp.com',
			'Content-Type':'application/json'
			#'Content-Length': 'length',

		}
		#sendurl='http://ws.messagegateway.ctripcorp.com/messageplatformservice/api/SendMessage'
		sendurl='http://ws.messagegateway.ctripcorp.com/messageplatformservice/api/sendmessage'
		msgstring=value
		msgbody='{\"ChannelInfo\":{\"MobilePhone\":\"18610817561\",\"ScheduleTime\":\"2016-04-07T15:31:37.2139167+08:00\"},\"Content\":{\"Content\":\"%s\"}}' % msgstring
		msgbody=json.dumps(msgbody)
		data='{"MessageCode":290019,"MsgBody":%s,"UID":null,"OrderID":0,"EID":null,"ExpiredTime":null}' % msgbody


		request=urllib2.Request(url=sendurl,headers=sendheaders,data=data)
		try:
			response=urllib2.urlopen(request,timeout=2)
			#print response.read()
			return response.read()
		except:
			print 'SendErr'
			return 'SendError'


a=0
while True:
	a=a+1
	data=GetFunction(availableUrl,loginHeaders,3)
	if data=='GetError':
		continue
	else:
		try:
			dataDict=json.loads(data)
		except:
			print '转json失败，重试'
			continue
	if dataDict.has_key('Status') and dataDict.has_key('Data'):
		if dataDict['Status']==200:
			listData=dataDict['Data']['list']
			haveTicketDict=''
			for iDict in listData:
				if iDict['Status']==0:
					message=str(iDict['SellPrice'])+'的有票了; '
					haveTicketDict+=message
					print message

			else:
				if haveTicketDict!='':
					haveTicketDict='周杰伦上海演唱会'+haveTicketDict
					sendStatus=SendMessages(haveTicketDict)
					if sendStatus=='SendError':
						SendMessages(haveTicketDict)
					exit()
				else:
					print '无票，继续刷,第%d次' % a
		else:
			continue
	else:
		continue

