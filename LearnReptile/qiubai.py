#-*-coding:utf-8-*-
import urllib,urllib2,re,thread,time
#-------加载处理qiubai-------------
class Spider_Model:
	def __int__(self):
		self.page = 1
		self.pages = []
		self.enable = False

	#将所有的duanzi都扣出来，添加到列表中并且返回列表
	def GetPage(self,page):
		myUrl="http://www.qiushibaike.com/hot/page" + page
		user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36'
		headers = {'User-Agent':user_agent}
		req=urllib2.Request(myUrl,headers=headers)
		myResponse=urllib2.urlopen(req)
		myPage=myResponse.read()
		unicodePage=myPage.decode("utf-8") #decode作用将其他编码字符串转换成Unicode编码



