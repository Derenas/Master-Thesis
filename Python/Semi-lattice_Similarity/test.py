# -*- coding: utf-8 -*-
'''
Created on 9 mars 2016

@author: virgilt
'''


import os
import regularExpression
import re

def printFiles():
	print getAllFiles()		

if __name__ == '__main__':
	date = regularExpression.exprReguliereDate()
	f = open('article.txt','r')
	res = open('articleL.txt', 'w')
	resdate = open('date.txt', 'w')
	print date
	for line in f.readlines():
		for m in re.finditer(date, line):
			print(m.group(0))
			resdate.write(m.group(0)+"\n")
		for m in re.finditer(r'L\. [0-9]{1,3}(-| )[0-9]', line):
	        	print(m.group(0), m.start(), m.end())
			res.write(m.group(0)+"\n")
	res.close()
	f.close()
	resdate.close()

