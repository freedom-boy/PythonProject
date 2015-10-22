#-*-coding:utf-8-*-
import string,urllib2

def baidu_tieba(url,begin_page,end_page):
	for i in range(begin_page,end_page+1):
		sName=string.zfill(i,5)+'.html'#自动填充成六位的文件名
		print '正在下载第'+str(i)+'个网页，并将其存储为'+sName+'.....'
		f=open(sName,'w+')
		m=urllib2.urlopen(url+str(i)).read()
		f.write(m)
		f.close()

tiebaurl='http://tieba.baidu.com/p/3138733512?see_lz=1&pn='
begin_page=int(raw_input(u'请输入开始页数：\n'))
end_page=int(raw_input(u'请输入结束页数：\n'))


baidu_tieba(tiebaurl,begin_page,end_page)