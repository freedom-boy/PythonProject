#!/usr/bin/env python
#_*_coding:utf-8_*_
#作者:Paul哥
import urllib2,cookielib,random,urllib,json,time,re
import LoginAccount,TrainNumQuery,BookingSeat
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
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
        self.loginout='https://kyfw.12306.cn/otn/login/loginOut'
        self.accessHeaders={
            'Host': 'kyfw.12306.cn',
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
            'Referer': 'https://kyfw.12306.cn/otn/init',
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

        self.FullSeatTypeDict={'商务座':'9','二等座':'O','一等座':'M','特等座':'P','高级软卧':'6','软卧':'4','硬卧':'3','软座':'2','硬座':'1'}
        self.sixcodedict={'1':'40,75','2':'110,75','3':'180,75','4':'250,75','5':'40,150','6':'110,150','7':'180,150','8':'250,150'}
        self.eighteencodedict={'a':'25,30','b':'70,30','c':'120,30','d':'170,30','e':'220,30','f':'270,30','g':'25,80','h':'70,80','i':'120,80','j':'170,80','k':'220,80','l':'270,80','m':'25,130','n':'70,130','o':'120,130','p':'170,130','q':'220,130','r':'270,130'}
        #坐标对应数字

        self.cookie=cookielib.CookieJar()  #cookie制作器
        self.cookieHandler=urllib2.HTTPCookieProcessor(self.cookie)
        self.opener=urllib2.build_opener(self.cookieHandler)
        urllib2.install_opener(self.opener)
        self.Imagesuffix=random.random()
        self.ImageUrl='https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=login&rand=sjrand&'+str(self.Imagesuffix)
        self.BookingImageurl='https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=passenger&rand=randp&'+str(self.Imagesuffix)

    def LoginOut(self):
        request=urllib2.Request(self.loginout,headers=self.accessHeaders)
        try:
            response=urllib2.urlopen(request,timeout=2)
            print '退出登录成功'
        except:
            print "退出失败"

    def inputuserandpasswd(self):
        username=raw_input('请输入您的用户名:')
        password=raw_input('请输入您的密码:')
        userpassdict={'user':username,'passwd':password}
        return userpassdict

    def login(self): ##请用户输入用户名密码登录
        userpass=self.inputuserandpasswd()
        while True:
            for i in range(3):
                getimagestatus=LoginRun.GetCodeImage(self.accessHeaders,self.ImageUrl)
                if getimagestatus=='GetImageSuccess':
                    break
                else:
                    pass

            img=Image.open('code.jpg')
            font=ImageFont.truetype('arial.ttf',size=30)
            draw = ImageDraw.Draw(img)
            draw.text((55, 55),"1",(255,0,0),font=font)
            draw.text((125, 55),"2",(255,0,0),font=font)
            draw.text((200, 55),"3",(255,0,0),font=font)
            draw.text((270, 55),"4",(255,0,0),font=font)
            draw.text((55, 120),"5",(255,0,0),font=font)
            draw.text((125, 120),"6",(255,0,0),font=font)
            draw.text((200, 120),"7",(255,0,0),font=font)
            draw.text((270, 120),"8",(255,0,0),font=font)
            img.show()
            img.close()
            codestr=''
            Input=raw_input('请输入验证码数字:')
            # print "验证码类型：1.八码    2.十八码"
            # sixoreitht=raw_input('您输入的验证码类型是:')
            # if sixoreitht=='1':
            #     codedict=self.sixcodedict
            # else:
            #     codedict=self.eighteencodedict
            #     font=ImageFont.truetype('arial.ttf',size=20)
            #     img=Image.open('code.jpg')
            #     draw = ImageDraw.Draw(img)
            #     draw.text((45, 44),"a",(255,0,0),font=font)
            #     draw.text((95, 44),"b",(255,0,0),font=font)
            #     draw.text((140, 44),"c",(255,0,0),font=font)
            #     draw.text((185, 44),"d",(255,0,0),font=font)
            #     draw.text((235, 44),"e",(255,0,0),font=font)
            #     draw.text((280, 44),"f",(255,0,0),font=font)
            #     draw.text((44, 95),"g",(255,0,0),font=font)
            #     draw.text((95, 95),"h",(255,0,0),font=font)
            #     draw.text((140, 95),"i",(255,0,0),font=font)
            #     draw.text((185, 95),"j",(255,0,0),font=font)
            #     draw.text((235, 95),"k",(255,0,0),font=font)
            #     draw.text((280, 95),"l",(255,0,0),font=font)
            #     draw.text((44, 140),"m",(255,0,0),font=font)
            #     draw.text((95, 140),"n",(255,0,0),font=font)
            #     draw.text((140, 140),"o",(255,0,0),font=font)
            #     draw.text((185, 140),"p",(255,0,0),font=font)
            #     draw.text((235, 140),"q",(255,0,0),font=font)
            #     draw.text((280, 140),"r",(255,0,0),font=font)
            #     img.show()
            #     img.close()

            for i in Input:
                codestr=codestr + self.sixcodedict[i]+','

            coderesult=codestr[:-1]
            data={"randCode":str(coderesult),"rand":'sjrand'}
            data=urllib.urlencode(data)

            codestrcookies=LoginRun.PostLoginInfo(self.accessHeaders,data)
            if codestrcookies!='checkcodeFalse':
                print '验证码输入正确'
            else:
                print "不好意思，验证码错误，请重试"


            data={"loginUserDTO.user_name":userpass['user'],"userDTO.password":userpass['passwd'],"randCode":coderesult}
            postdata=urllib.urlencode(data)
            request=urllib2.Request(self.checkloginurl,headers=self.accessHeaders,data=postdata)
            try:
                checkresponse=urllib2.urlopen(request)
            except:
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
                trainnuminfo=TrainQuery.GetNumDict(trainnum)#查询车次信息，返回整个车次信息所有内容
                return trainnuminfo
            else:
                print "网络慢，请稍等。。。"
        else:
            print "无法获取到车次信息"

    def PrintNumInfo(self,traininfo): #打印出车次信息，返回车次预订检测data
        print "预订号"+"|"+" 车次号 "+"|"+"  出发站  "+"|"+"  到达站  "+"|"+"出发时间"+"|"+"到达时间"+"|"+"商务座"+"|"+"特等座"+"|"+"一等座"+"|"+"二等座"+"|"+"高级软卧"+"|"+"软卧"+"|"+"硬卧"+"|"+"软座"+"|"+"硬座"+"|"+"无座"+"|"+"预定状态"
        count=0
        TrainInfodict={}
        for Num in traininfo:
            count+=1
            NumInfo=Num["queryLeftNewDTO"]
            TraNum=(NumInfo["station_train_code"])
            From=(NumInfo["from_station_name"])
            To=(NumInfo["to_station_name"])
            starttime=(NumInfo["start_time"])
            arrivetime=(NumInfo["arrive_time"])
            swz=(NumInfo["swz_num"])
            tz=(NumInfo["tz_num"])
            zy=(NumInfo["zy_num"])
            ze=(NumInfo["ze_num"])
            gr=(NumInfo["gr_num"])
            rw=(NumInfo["rw_num"])
            yw=(NumInfo["yw_num"])
            rz=(NumInfo["rz_num"])
            yz=(NumInfo["yz_num"])
            wz=(NumInfo["wz_num"])
            startdate=str(NumInfo['start_train_date'])
            traindate=startdate[0:4]+'-'+startdate[4:6]+'-'+startdate[6:8]
            dateformat='%Y-%m-%d'
            backdate=time.strftime(dateformat, time.localtime())

            postdict={"secretStr":str(Num["secretStr"]),"train_date":traindate,"back_train_date":str(backdate),"tour_flag":"dc","purpose_codes":"ADULT","query_from_station_name":From,"query_to_station_name":To,"undefined":''}
            postdata=urllib.urlencode(postdict)
            TrainInfodict[count]=postdata
            #print (str(count)).ljust(5),'|',TraNum.ljust(6),'|',From.center(6),'|',To.center(6),'|',starttime.center(6),'|',arrivetime.center(6),'|',swz.center(4),'|',tz.center(4),'|',zy.center(4),'|',ze.center(4),'|',gr.center(6),'|',rw.center(2)
            print '-------------------------------------------------------------------------------------------'
            print "%-6d|%-8s|%-6s|%-7s|%-8s|%-8s|%-6s|%-6s|%-6s|%-6s|%-8s|%-4s|%-4s|%-4s|%-4s|%-4s|%-8s" % (count,TraNum,From,To,starttime,arrivetime,swz,tz,zy,ze,gr,rw,yw,rz,yz,wz,Num["buttonTextInfo"])

        return TrainInfodict



    def GetRequToken(self,checkresult):
        token= re.search(r'var globalRepeatSubmitToken = \'(.*?)\'\;',checkresult,re.DOTALL)
        return token.group(1)

    def GetSeatType(self,checkresult):
        seat_type=re.search(r'var init_seatTypes\=\[\{(.*?)\}\]\;',checkresult,re.DOTALL)
        SeatTypeStr=seat_type.group(1)
        SeatTypelist=SeatTypeStr.split('},{')
        SeatTypeDict={}
        count=0
        for seat in SeatTypelist:
            count+=1
            seatjsonstr='{'+seat+'}'
            JsonStr = seatjsonstr.replace("'","\"")
            jsonstr1=JsonStr.replace("null","\"null\"")
            jsonstr=json.loads(jsonstr1)
            SeatTypeDict[str(count)]=jsonstr['value']
        for k,v in SeatTypeDict.items():
            print k,'.',v
        return SeatTypeDict


    def BookingCheckCode(self,token):
        while True:
            for i in range(3):
                getimagestatus=LoginRun.GetCodeImage(self.getpassengerHeaders,self.BookingImageurl)
                if getimagestatus=='GetImageSuccess':
                    break
                else:
                    pass

            img=Image.open('code.jpg')
            img.show()
            img.close()
            print "验证码类型：1.八码    2.十八码"
            sixoreitht=raw_input('您输入的验证码类型是:')
            if sixoreitht=='1':
                codedict=self.sixcodedict
                img=Image.open('code.jpg')
                font=ImageFont.truetype('arial.ttf',size=30)
                draw = ImageDraw.Draw(img)
                draw.text((55, 55),"1",(255,0,0),font=font)
                draw.text((125, 55),"2",(255,0,0),font=font)
                draw.text((200, 55),"3",(255,0,0),font=font)
                draw.text((270, 55),"4",(255,0,0),font=font)
                draw.text((55, 120),"5",(255,0,0),font=font)
                draw.text((125, 120),"6",(255,0,0),font=font)
                draw.text((200, 120),"7",(255,0,0),font=font)
                draw.text((270, 120),"8",(255,0,0),font=font)
                img.show()
                img.close()
            else:
                codedict=self.eighteencodedict
                font=ImageFont.truetype('arial.ttf',size=20)
                img=Image.open('code.jpg')
                draw = ImageDraw.Draw(img)
                draw.text((45, 44),"a",(255,0,0),font=font)
                draw.text((95, 44),"b",(255,0,0),font=font)
                draw.text((140, 44),"c",(255,0,0),font=font)
                draw.text((185, 44),"d",(255,0,0),font=font)
                draw.text((235, 44),"e",(255,0,0),font=font)
                draw.text((280, 44),"f",(255,0,0),font=font)
                draw.text((44, 95),"g",(255,0,0),font=font)
                draw.text((95, 95),"h",(255,0,0),font=font)
                draw.text((140, 95),"i",(255,0,0),font=font)
                draw.text((185, 95),"j",(255,0,0),font=font)
                draw.text((235, 95),"k",(255,0,0),font=font)
                draw.text((280, 95),"l",(255,0,0),font=font)
                draw.text((44, 140),"m",(255,0,0),font=font)
                draw.text((95, 140),"n",(255,0,0),font=font)
                draw.text((140, 140),"o",(255,0,0),font=font)
                draw.text((185, 140),"p",(255,0,0),font=font)
                draw.text((235, 140),"q",(255,0,0),font=font)
                draw.text((280, 140),"r",(255,0,0),font=font)
                img.show()
                img.close()
            codestr=''
            Input=raw_input('请输入验证码:')
            for i in Input:
                codestr=codestr + codedict[i]+','

            coderesult=codestr[:-1]
            data={"randCode":str(coderesult),"rand":'randp',"REPEAT_SUBMIT_TOKEN":str(token),"_json_att":""}
            data=urllib.urlencode(data)
            codestrcookies=LoginRun.PostLoginInfo(self.getpassengerHeaders,data)
            if codestrcookies!='checkcodeFalse':
                print '验证码输入正确'
                return coderesult
            else:
                print "不好意思，验证码错误，请重试"
                continue

    def GetCheckOrderINfo(self,PassengerData,bookincodestr,seatstr,token):
        PassengerName=PassengerData['passenger_name']+','
        PassengerIdCode=PassengerData['passenger_id_type_code']+','
        PassengerIdNum=PassengerData['passenger_id_no']+','
        if PassengerData.has_key('mobile_no')==False:
            PassengerMobile=''
        else:
            PassengerMobile=PassengerData['mobile_no']+','
        passengerTicketStr=seatstr+','+'0,1,'+PassengerName+','+PassengerIdCode+','+PassengerIdNum+','+PassengerMobile+',N'
        oldPassengerStr=PassengerName+','+PassengerIdCode+','+PassengerIdNum+',1_'
        cancel_flag='2'
        bed_level_order_num='000000000000000000000000000000'
        tour_flag='dc'
        data={"cancel_flag":cancel_flag,"bed_level_order_num":bed_level_order_num,"passengerTicketStr":passengerTicketStr,"oldPassengerStr":oldPassengerStr,"tour_flag":tour_flag,"randCode":bookincodestr,"REPEAT_SUBMIT_TOKEN":token,"_json_att":""}
        postdata=json.dumps(data)
        return postdata

    def GetCheckQueueCountInfo(self):









    def ShopRun(self):
        print "欢迎您来到Paul哥的火车票服务中心，请问您需要什么服务？"
        print "1.火车票服务    2.跟老刘去大保健    3.跟油哥学洞玄子三十六散手"
        ServiceNum=input('请输入服务数字:')
        if ServiceNum==1:
            Loginstatus=self.login()
            if Loginstatus=='LoginSuccess':
                print '恭喜您登陆成功,请选择您需要的服务：'
                print "1.车票预订  2.车次查询   3.余票查询  4.退票  5.改签  6.东莞直通车"
                service=raw_input('请输入服务数字:')
                if service=='1':
                    queryinfo=self.Query()
                    bookingdata=self.PrintNumInfo(queryinfo)
                    bookingnum=int(raw_input('请选择您要预订的车次:'))
                    checkdata=bookingdata[bookingnum]
                    for i in range(3):
                        checkresult=SeatBooking.BookingCheck(checkdata)
                        if checkresult!='BookingCheckError':
                            break
                        else:
                            continue
                    else:
                        print '连续三次都获取失败，不是我程序问题，是网络问题哦！'

                    token=self.GetRequToken(checkresult)
                    for i in range(3):
                        Passinfo=SeatBooking.GetPassengerjson(token)
                        if Passinfo!='GetPassengerError':
                            break
                        else:
                            continue
                    else:
                        print '连续三次都获取失败，不是我程序问题，是网络问题哦！'

                    passinfodict=SeatBooking.ChoicePassenger(Passinfo)
                    choicePassenger=raw_input('请选择乘客:')
                    PassengerData=passinfodict[choicePassenger] #乘客的信息
                    SeatTypedict=self.GetSeatType(checkresult)
                    choiceSeatType=raw_input('请选择席别:')
                    SeatType=SeatTypedict[str(choiceSeatType)]
                    SeatTypeStr=self.FullSeatTypeDict[str(SeatType)] #座位编码
                    bookincodestr=self.BookingCheckCode(token) #扣位验证码字符
                    CheckOrderINfo=self.GetCheckOrderINfo(PassengerData,bookincodestr,SeatTypeStr,token)


                    self.LoginOut()





if __name__=="__main__":
    Service=ShopTicket()
    Service.ShopRun()


