# -*- coding: utf-8 -*-
'''
Created on 9 mars 2016

@author: virgilt
'''

import regularExpression as regex

res = regex.expreReguliereArticle()+regex.expreReguliereCode()
print res

'''import os
import regularExpression as regex
import re
import filesGetter as fg
import sys
import roman

def printFiles():
	print fg.getAllFiles()		

def developAttribute(attribute):
	developpedList = []
	code = ""
	developpedList.append(attribute)
	m = re.search('du code',attribute)
	if m is not None:
		art = attribute[:m.start()]
		code = attribute[m.start()+3:]
	if attribute[1] == " ":
		ind = art.rfind('-') 
		while(ind!=-1):
			art = art[:ind]
			print art
			developpedList.append(art+" du "+code)
			ind = art.rfind('-') 
		developpedList.append(code)
		livre = "Livre "+roman.toRoman(int(attribute[2]))+" du "+code
		developpedList.append(livre)
		if attribute[3].isdigit():
			titre = "Titre "+roman.toRoman(int(attribute[3]))+" du "+livre
			developpedList.append(titre)
	return developpedList

def buildAttributes(setOfAttributes):
	setRes = set()
	for attribute in setOfAttributes:
		setOfDeclension = developAttribute(attribute)
		for att in setOfDeclension:
			setRes.add(att)
	return setRes

with open('developTest.txt','w') as res:
	attList = ['livre III du code des marches publics','L 920-5-3 du code du travail','L 4 du code de la securite sociale','L 441-6 du code de commerce','L 138-9 du code de securite sociale','R 162-52 du code de la securite sociale','L 621-63 du code de commerce','L 410-1 du code de commerce']
	attSet = set(attList)
	developpedList = buildAttributes(attSet)
	for item in developpedList:
		res.write(item+'\n')'''
