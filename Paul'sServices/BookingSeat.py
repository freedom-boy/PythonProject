#!/usr/bin/env python
#_*_coding:utf-8_*_
#作者:Paul哥
import urllib2,pickle,json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class Booking:

    def __init__(self):
        self.checkuserurl='https://kyfw.12306.cn/otn/login/checkUser'
        self.checkbookingurl='https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest'#扣位验证链接
        self.bookingurl='https://kyfw.12306.cn/otn/confirmPassenger/initDc'
        self.defaultdata=json.dumps({"_json_att=":""})
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

    def BookingCheck(self,postdata):
        checkuserrequest=urllib2.Request(self.checkuserurl,headers=self.accessHeaders,data=self.defaultdata)
        try:
            response=urllib2.urlopen(checkuserrequest,timeout=2)
            print response.read()
        except:
            print '车次预订第一次验证失败'

        request=urllib2.Request(self.checkbookingurl,headers=self.accessHeaders,data=postdata)
        try:
            response=urllib2.urlopen(request,timeout=2)
            print response.read()
        except:
            print '车次预订第二次验证失败'


        bookingrequest=urllib2.Request(self.bookingurl,headers=self.accessHeaders,data=self.defaultdata)
        try:
            bookingresponse=urllib2.urlopen(bookingrequest,timeout=2)
            print bookingresponse.read()
            return bookingresponse.read()
        except:
            print "车次预订失败"




