#!/usr/bin/env python
#_*_coding:utf-8_*_
#作者:Paul哥
import urllib2,os,cookielib,urllib,re,webbrowser

class Login:

	def __init__(self):
		self.loginurl='https://login.taobao.com/member/login.jhtml'
		self.loginHeaders={
			'Host':'login.taobao.com',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Accept-Language': 'zh-CN,zh;q=0.8',
			'Upgrade-Insecure-Requests':'1',
		    'Referer': 'https://login.taobao.com/member/login.jhtml',
			'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36'
		}
		self.username='18610817561'
		self.ua='062UW5TcyMNYQwiAiwQRHhBfEF8QXtHcklnMWc=|Um5OcktySnJPdE14QHtBeS8=|U2xMHDJ7G2AHYg8hAS8WLQMjDVEwVjpdI1l3IXc=|VGhXd1llXGVdZVhjWm9WY1dtWmdFeUN2SHRAf0F8R31FfkpwTnBeCA==|VWldfS0QMA47BCQYIwMtXiQUcBp3Ci5HLRU1VCVcPxFHEQ==|VmNDbUMV|V2NDbUMV|WGRYeCgGZhtmH2VScVI2UT5fORtmD2gCawwuRSJHZAFsCWMOdVYyVTpbPR99HWAFYVMpUDUFbFNvBWJAekB/RnJNclBsWGxWblVrVG9beUVnXgVUF3kTOVdnGn0ELlU4VDVOI0g1azJ0RCRZJF0nDjEJN3xValJtIQg3DzB8AnwCIF00UzlQNxV+GXxValJtIQ8vAS95Lw==|WWdHFyoKNxcrECUYOA05ASEdJhMuDjIPNwoqFi0YJQU5BDgFUwU=|WmZbe1UFPgI6BTkZTmBcZVlhW2NWYl9qUGlWIx48CDQBNQA6ADQIMAw4Az8APGtFZVkPIXc=|W2dZeSkHWzpcMFcpU39Fa0tlOXo+Ei4aOgcnGjoFOgEveS8=|XGREFDoUNGRYZFxiQn1DfigINRU7FTUJMwc4AjxqPA==|XWdHFzlmPXsvUylEP1kwVThsUH5eYkJ+RHBOdU8ZTw==|XmVFFTtkP3ktUStGPVsyVzpuUnxcaFJyT29TaV1pUWg+aA==|X2REFDplPngsUCpHPFozVjtvU31dYVxlRXhYZFFsUWtVA1U=|QHtbCyV6IWczTzVYI0UsSSRwTGJCfkN8XGFBfUh1SXJMGkw=|QXpaCiR7IGYyTjRZIkQtSCVxTWNDd01tUHBMeUR9Qn8pfw==|QnlZCSd4I2UxTTdaIUcuSyZyTmBAdFRpSXVAfEV6QRdB|Q3lZCSd4I2UxTTdaIUcuSyZyTmBAfV1hVGhRb1IEUg==|RH5eDiB/JGI2TyZcJlg/RCh8QG5OclJuW2deYFUDVQ==|RX1dDSNjN28TeRx9AFglTDFQOxU1ZVllWWVFe053IQE8HDIcPAA1DzYCPmg+|RnxcDCJ9JmA0TSReJFo9Rip+QmxMcVFtWGJaZ1wKXA==|R31dDSNjN28TeRx9AFglTDFQOxU1CSkVIBoiHip8Kg==|SHFMcVFsTHNTb1ZqSnRMdlZuWnpAeFhkWGFBfV1pVXVJcUVlWWBAfkRkW2VFekVlWmZGeURkWGxMck5uUG1NdVVqX39Aeiw='
		self.password2='531ff7f43821019be2350d1d37fe38fffad13951adf7c25c7d1b7902c97bc997c81ca95e3412035b8df3a8710e3d74e2326abaee6ce2f4b4718623a362db402c7774ac5df8d9b92e000bf15ae890e1db9d408cba6fe6695dd124d6579a23226c77a6305ee13a16785c2b95bb92dc8bb099ffea64b1d96d58d62fd9cbf085d736'
		self.post=post={
			'ua':self.ua,
		    'TPL_username':self.username,
		    'TPL_password':'',
		    'TPL_checkcode':'',
		    'ncoSig':'',
		    'ncoSessionid':'',
		    'ncoToken':'',
			'useSlideCheckcode':'false',
		    'slideCodeShow':'false',
		    'loginsite':'0',
		    'newlogin':'0',
		    'TPL_redirect_url':'https://www.taobao.com/',
			'from':'tbTop',
			'fc':'default',
		    'style':'default',
			'css_style':'',
			'keyLogin':'false',
			'qrLogin':'true',
			'newMini':'false',
			'tid':'',
			'support':'000001',
			'CtrlVersion':	'1,0,0,7',
			'loginType'	:'3',
			'minititle':'',
			'minipara':'',
			'umto':'NaN',
			'pstrong':'',
			'sign':'',
			'need_sign':'',
			'isIgnore':'',
			'full_redirect':'',
			'popid':'',
			'callback':'',
			'guf':'',
			'not_duplite_str':'',
			'need_user_id':'',
			'poy':'',
			'gvfdcname':'10',
			'gvfdcre':'68747470733A2F2F7777772E74616F62616F2E636F6D2F',
			'from_encoding':'',
			'sub':'',
			'loginASR':'1',
			'loginASRSuc':'1',
			'allp':'',
			'oslanguage':'zh-CN',
			'sr':'1680*1050',
			'osVer':'windows|6.1',
			'naviVer':'chrome|46.0249071'

		}

		self.postData=urllib.urlencode(self.post)
		self.cookie=cookielib.LWPCookieJar()
		self.cookieHandler=urllib2.HTTPCookieProcessor(self.cookie)
		self.opener=urllib2.build_opener(self.cookieHandler,urllib2.HTTPHandler)

	def needIdenCode(self):
		request=urllib2.Request(self.loginurl,)










