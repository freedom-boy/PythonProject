#!/usr/bin/env python
#_*_coding:utf-8_*_
#作者:Paul哥
import urllib2,cookielib,random,urllib,json
from PIL import Image
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
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
            'Referer': 'https://kyfw.12306.cn/otn/init',
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

    def GetCodeImage(self,header,loginimageurl): #获取验证码并取得cookie
        request=urllib2.Request(loginimageurl,headers=header)
        try:
            response=urllib2.urlopen(request)
            codeimage=response.read()
            file=open('code.jpg','wb')
            file.write(codeimage)
            file.flush()
            file.close()
            return 'GetImageSuccess'
        except:
            return 'GetImageError'


    def PostLoginInfo(self,header,data): #检测验证码是否正确
        # img=Image.open('code.jpg')
        # img.show()
        # img.close()
        # codestr=''
        # Input=raw_input('请输入验证码数字:')
        # for i in Input:
        #     codestr=codestr + self.codedict[i]+','
        #
        # coderesult=codestr[:-1]
        # data={"randCode":str(coderesult),"rand":'sjrand'}
        # data=urllib.urlencode(data)
        #print data
        request=urllib2.Request(self.checkcodeurl,headers=header,data=data)
        try:
            response=urllib2.urlopen(request)


        except:
            return "checkcodeFalse"


        responsedict=json.loads(response.read())

        if responsedict["data"]["result"]=='1':

            return "checkcodeTrue"
        else:

            return 'checkcodeFalse'




    # def StartLogin(self): #检测用户名密码和验证码对错
    #     username=raw_input('Please input your username:')
    #     password=raw_input('Please input your password:')
    #     data={"loginUserDTO.user_name":username,"userDTO.password":password,"randCode":str(self.PostLoginInfo()['checkcodeTrue'])}
    #     postdata=urllib.urlencode(data)
    #     #print postdata
    #     request=urllib2.Request(self.loginurl,headers=self.accessHeaders,data=postdata)
    #     response=urllib2.urlopen(request)
    #     print response.read()

        # request2=urllib2.Request('https://kyfw.12306.cn/otn/index/initMy12306',headers=self.accessHeaders)
        # response3=urllib2.urlopen(request2)
        # print response3.read()


if __name__=='__main__':
    test=Login()
    Imagesuffix=random.random()
    ImageUrl='https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=login&rand=sjrand&'+str(Imagesuffix)
    test.GetCodeImage(ImageUrl)
    #test.PostLoginInfo()
    #test.StartLogin()
