#!/usr/bin/env python
#_*_coding:utf-8_*_
#作者:Paul哥
import urllib2,cookielib,random,urllib,json
import LoginAccount,TrainNumQuery,BookingSeat
import ssl,sys
ssl._create_default_https_context = ssl._create_unverified_context
reload(sys)
sys.setdefaultencoding('utf8')
LoginRun=LoginAccount.Login()
TrainQuery=TrainNumQuery.QueryTrain()
SeatBooking=BookingSeat.Booking()

from bs4 import BeautifulSoup

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
        username=raw_input('请输入您的用户名:')
        password=raw_input('请输入您的密码:')
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
            codestrcookies=LoginRun.PostLoginInfo()
            if codestrcookies!='checkcodeFalse':
                print '验证码输入正确'
            else:
                print "不好意思，验证码错误，请重试"
                continue

            data={"loginUserDTO.user_name":userpass['user'],"userDTO.password":userpass['passwd'],"randCode":str(codestrcookies['checkcodeTrue'])}
            postdata=urllib.urlencode(data)
            request=urllib2.Request(self.checkloginurl,headers=self.accessHeaders,data=postdata)
            checkresponse=urllib2.urlopen(request)
            logincheck=json.loads(checkresponse.read())
            if logincheck["data"].has_key("loginCheck") and logincheck["data"]["loginCheck"]=='Y':
                print '用户名及密码正确'
                break
            else:
                print "不好意思，您用户名密码输入有误，请重新输入，如果输错次数超过4次，用户将被锁定"
                userpass=self.inputuserandpasswd()
                continue

        request2=urllib2.Request(self.loginurl,headers=self.accessHeaders)
        loginresponse=urllib2.urlopen(request2)
        html=loginresponse.read()
        # file=open('login.html','wb')
        # file.write(html)
        # file.close()
        soup=BeautifulSoup(html,'lxml')
        loginstatus=str(soup.p)

        if loginstatus[3:18]=='欢迎您登录':
            return 'LoginSuccess'


    def Query(self):
        FromST=raw_input('请输入您的出发站:')
        ToST=raw_input('请输入您的到达站:')
        Startdate=raw_input('请输入您的出发日期（8位数字）:')
        queryurl=TrainQuery.CreateUrl(FromST,ToST,Startdate)
        for i in range(3):
            trainnum=TrainQuery.GetTrainNumDate(queryurl)
            if trainnum!='GetError':
                trainnuminfo=TrainQuery.GetNumDict(trainnum)
                return trainnuminfo
            else:
                print "网络慢，请稍等。。。"
        else:
            print "无法获取到车次信息"



    def Booking(self,bookingcheck):
        print bookingcheck
        checkresult=SeatBooking.BookingCheck(bookingcheck)
        print checkresult




























    def ShopRun(self):
        print "欢迎您来到Paul哥的服务中心，请问有什么可以帮您？"
        print "1.火车票服务"
        print "2.跟老刘去大保健"
        print "3.跟油哥学欲女心经"
        ServiceNum=input('请输入服务数字:')
        if ServiceNum==1:
            Loginstatus=self.login()
            if Loginstatus=='LoginSuccess':
                print '恭喜您登陆成功,请选择您需要的服务：'
                print "1.车票预订  2.车次查询   3.余票查询  4.退票  5.改签  6.东莞直通车"
                service=raw_input('请输入服务数字:')
                if service=='1':
                    queryinfo=self.Query()
                    bookingnum=int(raw_input('请选择您要预订的车次:'))
                    self.Booking(queryinfo[bookingnum])






if __name__=="__main__":
    Service=ShopTicket()
    Service.ShopRun()


