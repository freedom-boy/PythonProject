#-*-coding:utf-8-*-
import urllib,urllib2,re

class Tool:
	removeImg=re.compile('<img.*?>| {7}|')
	removeAddr=re.compile('<a.*?>.*?</a>')
	replaceLine=re.compile('<tr>|<div>|</div>|</p>')
	replaceTD=re.compile('<td>')
	replacePara=re.compile('<p.*?>')
	replaceBR=re.compile('<br><br>|<br>')
	removeExtraTag=re.compile('<.*?>')
	def replace(self,x):
		x = re.sub(self.removeImg,"",x)
		x = re.sub(self.removeAddr,"",x)
		x = re.sub(self.replaceLine,"\n",x)
		x = re.sub(self.replaceTD,"\t",x)
		x = re.sub(self.replacePara,"\n  ",x)
		x = re.sub(self.replaceBR,"\n",x)
		x = re.sub(self.removeExtraTag,"",x)
		return x.strip()


class BDTB:
	def __init__(self,baseurl,seeLZ,floorTag):
		self.baseurl=baseurl
		self.seeLZ='?see_lz'+str(seeLZ)
		self.Tool=Tool()
		self.file=None
		self.floor=1 #楼层标号，初始为1
		self.defaultTitle=u"百度贴吧" #默认标题，如果没有获取到标题，则采用此标题
		self.floorTag=floorTag #是否写入楼分隔符的标记

	def getPage(self,pageNum):
		try:
			url=self.baseurl+self.seeLZ+'&pn='+str(pageNum)
			request=urllib2.Request(url)
			response=urllib2.urlopen(request)
			return response.read().decode('utf-8')
			#print response.read()

		except urllib2.URLError,e:
			if hasattr(e,'reason'):
				print u'连接百度贴吧失败，原因为:',e.reason
				return None

	def getTitle(self,page):
		#pattern=re.compile('<h1 class="core_title_txt".*?>(.*?)</h1>',re.S)
		pattern=re.compile('<h1 class="core_title_txt".*?>(.*?)</h1>',re.S)
		result=re.search(pattern,page)
		if result:
			#print result.group(1)
			return result.group(1).strip()
		else:
			return None

	def getPageNum(self,page):
		pattern=re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
		result=re.search(pattern,page)
		if result:
			#print  result.group(1).strip()
			return result.group(1).strip()
		else:
			return None

	def getContent(self,page):
		pattern=re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
		items=re.findall(pattern,page)
		contents=[]
		for i in items:
			content="\n"+self.Tool.replace(i)+"\n"
			contents.append(content.encode('utf-8'))
		return contents

	def setFileTitle(self,title):
		if title is not None:
			self.file=open(title + ".txt","w+")
		else:
			self.file=open(self.defaultTitle+ ".txt","w+")

	def writeData(self,contents):
		for item in contents:
			if self.floorTag=='1':
				floorLine='\n'+str(self.floor)+u"楼--------------------------------------------\n"
				self.file.write(floorLine)
			self.file.write(item)
			self.floor+=1

	def start(self):
		indexPage=self.getPage(1)
		pageNum=self.getPageNum(indexPage)
		#pageNum='5'
		title=self.getTitle(indexPage)
		self.setFileTitle(title)
		if pageNum==None:
			print 'URL已失效，请重试'
			return
		try:
			print '该帖子共有'+str(pageNum)+'页'
			for i in range(1,int(pageNum)+1):
				print "正在写入第"+str(i)+"页数据"
				page=self.getTitle(i)
				contents=self.getContent(page)
				self.writeData(contents)
		except IOError,e:
			print "写入异常，原因："+e.message
		finally:
			print '写入任务完成！'

baseURL='http://tieba.baidu.com/p/'+str(raw_input(u"http://tieba.baidu.com/p/"))
seeLZ=raw_input('是否只获取楼主发言，是输入1，否输入0\n')
floorTag=raw_input('是否写入楼层信息，是输入1，否输入0\n')
bdtb=BDTB(baseURL,seeLZ,floorTag)
bdtb.start()

