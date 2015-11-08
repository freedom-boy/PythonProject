#!/usr/bin/env python
#_*_coding:utf-8_*_
#作者:Paul哥
import urllib2,pickle,json,re,sys

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
reload(sys)
sys.setdefaultencoding('utf8')
from bs4 import BeautifulSoup
FullSeatTypeDict={'商务座':'9','二等座':'O','一等座':'M','特等座':'P','高级软卧':'6','软卧':'4','硬卧':'3','软座':'2','硬座':'1'}
# sinaheaders={
#     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     #'Accept-Encoding:gzip, deflate, sdch
#     'Accept-Language':'zh-CN,zh;q=0.8',
#     'Cache-Control':'max-age=0',
#     'Connection':'keep-alive',
#     #Cookie:SINAGLOBAL=123.138.189.187_1446297447.183981; Apache=123.138.189.187_1446297447.183984; UOR=www.baidu.com,blog.sina.com.cn,; ULV=1446306291783:1:1:1:123.138.189.187_1446297447.183984:; U_TRS1=0000001e.36487e32.5634e1f3.dbd7375c; U_TRS2=0000001e.36577e32.5634e1f3.e1032f6e; SUB=_2AkMhaG7Lf8NjqwJRmPoUy23nZY5yygHEiebDAH_sJxJjHn817GhuPCq_xGrKg_N1PyK4PTic07Q_; SUBP=0033WrSXqPxfM72-Ws9jqgMF55z29P9D9WWEMjGc_Zsr5h.KmPi_9j4U; SessionID=7pc07df26k6s0tdsp2n832bj26; vjuids=326975e12.150be935777.0.9604cb1d; SGUID=1446306402080_78832707; xystate=1; xytime=1446895642085; vjlast=1446895643; CoupletMedia-1409988133=0; lxlrttp=1446879719
#     'Host':'www.sina.com.cn',
#     'If-Modified-Since':'Sat, 07 Nov 2015 11:24:06 GMT',
#     'Referer':'http://www.sina.com/',
#     'Upgrade-Insecure-Requests':'1',
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36'
# }
# request=urllib2.Request('http://www.sina.com.cn',headers=sinaheaders)
# response=urllib2.urlopen(request)
# resp=response.read()
# #print resp.decode('utf8')
# findall=resp.decode('utf8')
# soup = BeautifulSoup(open('bookingrequest.html'),'lxml')
# print soup.prettify()
html=open('booking.html','rb')
html1=html.read()
html.close()

SeatType = re.search(r'var init_seatTypes\=\[\{(.*?)\}\]\;',html1,re.DOTALL)
b = re.search(r'var ticketInfoForPassengerForm\=(.*?)\;',html1,re.DOTALL)
c = re.search(r'var orderRequestDTO\=(.*?)\;',html1,re.DOTALL)
token= re.search(r'var globalRepeatSubmitToken = \'(.*?)\'\;',html1,re.DOTALL)
# print token.group(1)
#
# SeatTypeStr=SeatType.group(1)
# SeatTypelist=SeatTypeStr.split('},{')
# SeatTypeDict={}
# count=0
# for seat in SeatTypelist:
#     count+=1
#     seatjsonstr='{'+seat+'}'
#     JsonStr = seatjsonstr.replace("'","\"")
#     jsonstr1=JsonStr.replace("null","\"null\"")
#     jsonstr=json.loads(jsonstr1)
#     SeatTypeDict[str(count)]=jsonstr['value']
#
#
# print SeatTypeDict
#
# print FullSeatTypeDict[str(SeatTypeDict['2'])]
# #alist=json.loads(adict)
#print alist


# JsonStr = adict.replace("'","\"")
# jsonstr1=JsonStr.replace("null","\"null\"")
#print adict
# for i in adictlist:
#     print (json.loads(i))[]

#bdict= c.group(1)

#print json.loads(jsonstr1)

#print  c.group(1)
#print  d.group(1)
# for i in a.split('\n'):
#     if i=='':
#         continue
#     else:
#         n=re.search(r'var(.*?)\=\[(.*?)',i)
#         print n.group()

# font=ImageFont.truetype('arial.ttf',size=30)
#
# img=Image.open('code.jpg')
# draw = ImageDraw.Draw(img)
#
# draw.text((55, 55),"1",(255,0,0),font=font)
# draw.text((125, 55),"2",(255,0,0),font=font)
# draw.text((200, 55),"3",(255,0,0),font=font)
# draw.text((270, 55),"4",(255,0,0),font=font)
# draw.text((55, 120),"5",(255,0,0),font=font)
# draw.text((125, 120),"6",(255,0,0),font=font)
# draw.text((200, 120),"7",(255,0,0),font=font)
# draw.text((270, 120),"8",(255,0,0),font=font)
#
# #draw = ImageDraw.Draw(img)
# img.show()
# img.close()

