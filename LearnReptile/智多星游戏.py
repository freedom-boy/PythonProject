#_*_coding:utf-8_*_
import string
import random
IndexString=random.sample('ABCDEF',4)
for i in range(12):
	hei=0
	bai=0
	str1=raw_input('Please input str1:')
	str2=raw_input('Please input str2:')
	str3=raw_input('Please input str3:')
	str4=raw_input('Please input str4:')
	while not str1.isalpha() or not str2.isalpha() or not\
	str3.isalpha() or not str4.isalpha():
		if not str1.isalpha():
			str1=raw_input('Input error!!!Please input str1:')
		if not str2.isalpha():
			str2=raw_input('Input error!!!Please input str2:')
		if not str3.isalpha():
			str3=raw_input('Input error!!!Please input str3:')
		if not str4.isalpha():
			str4=raw_input('Input error!!!Please input str4:')
	else:
		if str1 == IndexString[0]:
			hei+=1
		elif str1 in IndexString:
			bai+=1
		if str2 == IndexString[1]:
			hei+=1
		elif str2 in IndexString:
			bai+=1
		if str3 == IndexString[2]:
			hei+=1
		elif str3 in IndexString:
			bai+=1
		if str4 == IndexString[3]:
			hei+=1
		elif str4 in IndexString:
			bai+=1
		print 'Black is',hei,';','While is',bai
		if str1 == IndexString[0] and str2 == IndexString[1] and str3 == IndexString[2] and str4 == IndexString[3]:
			print 'Yeah!恭喜你猜测正确！'
			break
		else:
			if i==11:
				print '不好意思，您已经超过12次未猜测正确！'




