#-*-coding:utf-8-*-
import urllib,urllib2,cookielib,re,socket
# response=urllib2.urlopen('http://www.baidu.com')
# html=response.read()
# print html

# req=urllib2.Request('http://www.baidu.com')
# response=urllib2.urlopen(req)
# the_page=response.read()
# print the_page

# url='http://www.someserver.com/register.cgi'
# values={
# 	'name':'WHY',
#     'location':'SDU',
#     'language':'Python'
# }
#
# data=urllib.urlencode(values)
# req=urllib2.Request(url,data)
# response=urllib2.urlopen(req)
# the_page=response.read()


# old_url='https://login.taobao.com/member/login.jhtml?spm=1.7274553.1997563269.1.jgFny3&f=top&redirectURL=http%3A%2F%2Fwww.taobao.com%2F'
# req=urllib2.Request(old_url)
# response=urllib2.urlopen(req)
# print 'old_url:',old_url
# print 'read_url:',response.info()

# password_mgr=urllib2.HTTPPasswordMgrWithDefaultRealm()
# top_level_url='http://example.com/foo/'
# password_mgr.add_password(None,top_level_url,'why','1223')
#
# hander=urllib2.HTTPBasicAuthHandler(password_mgr)
# opener=urllib2.build_opener(hander)
# a_url='http://www.baidu.com'
# opener.open(a_url)
# urllib2.install_opener(opener)

# enable_proxy=True
# proxy_handler=urllib2.ProxyHandler({"http":'http://10.15.159.21:8080'})
# null_proxy_handler=urllib2.ProxyHandler({})
# if enable_proxy:
# 	opener=urllib2.build_opener(proxy_handler)
# else:
# 	opener=urllib2.build_opener(null_proxy_handler)
# urllib2.install_opener(opener)
#
# socket.setdefaulttimeout(10)#10秒钟后超时
# urllib2.socket.setdefaulttimeout(10)#PS:10秒超时
#
# response=urllib2.urlopen('http://www.google.com',timeout=10)

# request=urllib2.Request('http://www.baidu.com/')
# request.add_header('User-Agent','fake-client')
# response=urllib2.urlopen(request)
# print response.read()
#
# my_url='http://www.google.cn'
# response=urllib2.urlopen(my_url)
# redirected=response.geturl()==my_url
# print redirected
#
# my_url='http://rrurl.cn/b1UZuP'
# response=urllib2.urlopen(my_url)
# redirected=response.geturl()==my_url
# print redirected


# class RedirectHandler(urllib2.HTTPRedirectHandler):
# 	def http_error_302(self, req, fp, code, msg, headers):
# 		print '302'
# 		pass
#
# opener=urllib2.build_opener(RedirectHandler)
# opener.open('http://rrurl.cn/b1UZuP')

# cookie=cookielib.CookieJar()
# opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response=opener.open('http://www.baidu.com')
# for item in cookie:
# 	print 'Name='+item.name
# 	print 'Value='+item.value


# request=urllib2.Request(url,data=data)
# request.get_method=lambda :'PUT'# 'DELETE'
# response=urllib2.urlopen(request)

# try:
# 	response=urllib2.urlopen('http://www.baidu.com')
# 	print response.getcode()
# except urllib2.HTTPError,e:
# 	print e.code


# httpHandler=urllib2.HTTPHandler(debuglevel=1)
# httpsHandler=urllib2.HTTPHandler(debuglevel=1)
# opener=urllib2.build_opener(httpHandler,httpsHandler)
# urllib2.install_opener(opener)
# response=urllib2.urlopen('http://www.google.com')
# print response

# postdata=urllib.urlencode({
# 	'username':'汪小光',
#     'password':'why888',
#     'continueURL':'http://www.verycd.com/',
#     'fk':'',
# 	'login_submit':'登录'
#
# })
#
# req=urllib2.Request(
# 	url='http://secure.verycd.com/signin',
# 	data=postdata
# )
#
# result=urllib2.urlopen(req)
# print result


# pattern=re.compile(r'hello')
#
# match1=pattern.match('hello world!')
# match2=pattern.match('helloo world!')
# match3=pattern.match('helllo world!')
#
# if match1:
# 	print match1.group()
# else:
# 	print 'match1匹配失败！'
#
# if match2:
# 	print match2.group()
# else:
# 	print 'match2匹配失败！'
#
# if match3:
# 	print match3.group()
# else:
# 	print 'match3匹配失败！'
# a=re.compile(r"""\d + #the integral part
# 				 \.   #the decimal point
# 				 \d * #some fractianl""",re.X)
# b=re.compile(r"\d+\.\d*")
# match11=a.match('3.1415')
# match12=a.match('33')
# match21=b.match('3.1415')
# match22=b.match('33')
#
# if match11:
# 	print match11.group()
# else:
# 	print u'match11不是小数'
#
# if match12:
# 	print match12.group()
# else:
# 	print u'match12不是小数'
#
# if match21:
# 	print match21.group()
# else:
# 	print u'match21不是小数'
#
# if match22:
# 	print match22.group()
# else:
# 	print u'match22不是小数'

# m=re.match(r'hello','hello world!')
# print m.group()

# m=re.match(r'(\w+) (\w+)(?P<sign>.*)','hello world!')
#
# print "m.string:",m.string
# print "m.re:",m.re
# print "m.pos:",m.pos
# print "m.endpos:",m.endpos
# print "m.lastindex:",m.lastindex
# print "m.lastgroup:",m.lastgroup
#
# print "m.group():",m.group()
# print "m.group(1,2)",m.group(1,2)
# print "m.groups():",m.groups()
# print "m.groupdict:",m.groupdict()
# print "m.start(2):",m.start(2)
# print "m.end(2):",m.end(2)
# print "m.span(2)",m.span(2)
# print "m.expand(r'\g<2> \g<1>\g<3>'):",m.expand(r'\2 \1\3')


# p=re.compile(r'(\w+) (\w+)(?P<sign>.*)',re.DOTALL)
#
# print "p.pattern:",p.pattern
# print "p.flags:",p.flags
# print "p.groups:",p.groups
# print "p.groupindex",p.groupindex

# pattern=re.compile(r'hello')
# match=pattern.search('hello world! hello')
#
# if match:
# 	print match.group()
#
#
# p=re.compile(r'\d+')
# for m in p.finditer('one1two2three3four4'):
# 	print m.group(),


# p=re.compile(r'(\w+) (\w+)')
# s='I say,hello world!'
#
# print p.subn(r'\2 \1',s)
#
# def func(m):
# 	return m.group(1).title() + ' ' + m.group(2).title()
#
# print p.subn(func,s)







