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
        self.getPassengerurl='https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs'
        self.defaultdata=json.dumps({"_json_att=":""})
        self.accessHeaders={
            'Host': 'kyfw.12306.cn',
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
            'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init',
            #'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8'

        } #12306HTTP请求头
        self.getpassengerHeaders={
            'Host': 'kyfw.12306.cn',
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
            'Referer': 'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
            #'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8'

        }

    def BookingCheck(self,postdata):
        # checkuserrequest=urllib2.Request(self.checkuserurl,headers=self.accessHeaders,data=self.defaultdata)
        # try:
        #     response=urllib2.urlopen(checkuserrequest,timeout=2)
        #     print response.read()
        # except:
        #     print '车次预订第一次验证失败'

        request=urllib2.Request(self.checkbookingurl,headers=self.accessHeaders,data=postdata)
        try:
            response=urllib2.urlopen(request,timeout=2)
        except:
            print '车次预订第二次验证失败'
            return 'BookingCheckError'


        bookingrequest=urllib2.Request(self.bookingurl,headers=self.accessHeaders,data=self.defaultdata)
        try:
            bookingresponse=urllib2.urlopen(bookingrequest,timeout=2)
            #print bookingresponse.read()
            return bookingresponse.read()
        except:
            print "车次预订失败"
            return 'BookingCheckError'


    def GetPassengerjson(self,token):
        data=json.dumps({"REPEAT_SUBMIT_TOKEN":token,"_json_att=":""})
        request=urllib2.Request(self.getPassengerurl,headers=self.getpassengerHeaders,data=data)
        try:
            response=urllib2.urlopen(request,timeout=2)
            return response.read()
        except:
            print '获取常用联系人信息失败,重试中。。。'
            return 'GetPassengerError'


    def ChoicePassenger(self,passengerinfo):
        passengerdict=json.loads(passengerinfo)
        passengerlist=passengerdict["data"]["normal_passengers"]
        count=0
        PassengerInfodict={}
        for passcenger in passengerlist:
            count+=1
            PassengerInfodict[str(count)]=passcenger
            if passcenger.has_key('sex_name')==False:
                passcenger['sex_name']='未知'
            elif passcenger.has_key('passenger_type_name')==False:
                passcenger['passenger_type_name']='未知'
            print count,'--',passcenger['passenger_name'],'  ',passcenger['sex_name'],'  ',passcenger['passenger_id_type_name'],' ',passcenger['passenger_id_no'],'  ',passcenger['passenger_type_name']

        return PassengerInfodict








