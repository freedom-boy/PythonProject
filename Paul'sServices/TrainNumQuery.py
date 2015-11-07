#!/usr/bin/env python
#_*_coding:utf-8_*_
#作者:Paul哥
import urllib2,pickle,json,time,urllib
import ssl,sys
ssl._create_default_https_context = ssl._create_unverified_context
reload(sys)
sys.setdefaultencoding('utf8')

Station=file('station.txt','r')
StationDict=pickle.load(Station)
Station.close()

class QueryTrain:

    def __init__(self):
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

        self.Satation=StationDict

    def CreateUrl(self,fromstation,tostation,querydate):
        FromCode=self.Satation[fromstation]
        ToCode=self.Satation[tostation]
        Querydate=querydate[0:4]+'-'+querydate[4:6]+'-'+querydate[6:8]
        Dateurl=self.mainurl+'leftTicket/query?leftTicketDTO.train_date=%s' % Querydate
        Fromurl='leftTicketDTO.from_station=%s' % FromCode
        Tourl='leftTicketDTO.to_station=%s' % ToCode
        Tailurl='purpose_codes=ADULT'
        GetQueryUrl=Dateurl+'&'+Fromurl+'&'+Tourl+'&'+Tailurl
        #print GetQueryUrl
        return GetQueryUrl

    def GetTrainNumDate(self,queryurl):
        request=urllib2.Request(queryurl,headers=self.accessHeaders)
        try:
            response=urllib2.urlopen(request,timeout=2)
            return response.read()
        except:
            return 'GetError'

    def GetNumDict(self,response):
        TrainDatalist=[]
        TrainData=json.loads(response)
        if TrainData.has_key('data')==True:
            if TrainData['data']=='':
                print '不好意思，无法查询到车次'
            else:
                for i in TrainData['data']:
                    TrainDatalist.append(i)


        print "预订号"+"|"+" 车次号 "+"|"+"  出发站  "+"|"+"  到达站  "+"|"+"出发时间"+"|"+"到达时间"+"|"+"商务座"+"|"+"特等座"+"|"+"一等座"+"|"+"二等座"+"|"+"高级软卧"+"|"+"软卧"+"|"+"硬卧"+"|"+"软座"+"|"+"硬座"+"|"+"无座"+"|"+"预定状态"
        count=0
        TrainInfodict={}
        for Num in TrainDatalist:
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
            #print '-------------------------------------------------------------------------------------------'
            print "%-6d|%-8s|%-6s|%-7s|%-8s|%-8s|%-6s|%-6s|%-6s|%-6s|%-8s|%-4s|%-4s|%-4s|%-4s|%-4s|%-8s" % (count,TraNum,From,To,starttime,arrivetime,swz,tz,zy,ze,gr,rw,yw,rz,yz,wz,Num["buttonTextInfo"])
        #print TrainInfodict
        return TrainInfodict


if __name__=="__main__":
    QueryTrainNum=QueryTrain()
    URL=QueryTrainNum.CreateUrl('上海','北京','20151116')
    RESP=QueryTrainNum.GetTrainNumDate(URL)
    QueryTrainNum.GetNumDict(RESP)







