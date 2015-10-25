#!/usr/bin/env python
#_*_coding:utf-8_*_
#作者:Paul哥
import urllib2,os,cookielib,ssl
from PIL import Image


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
        self.ImageUrl='https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=login&rand=sjrand&0.31362101156262356'

    def GetUrl(self):
        request=urllib2.Request(self.ImageUrl,headers=self.accessHeaders)
        response=self.opener.open(request)
        print response.read()
        codeimage=response.read()
        file=open('12306code.jpg','wb')
        file.write(codeimage)
        file.close()

        return self.cookie

    def GetcodeImage(self,cookie):
        newopener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))




if __name__=='__main__':
    test=Login()
    test.GetUrl()
