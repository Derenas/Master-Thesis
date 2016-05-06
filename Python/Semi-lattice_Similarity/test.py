# -*- coding: utf-8 -*-
'''
Created on 9 mars 2016

@author: virgilt
'''


import os
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
		res.write(item+'\n')


	'''if __name__ == '__main__':
	f = open('concepts.txt','r')
	doc = sys.argv[1]+".txt"
	expre = r"((.)*'"+sys.argv[1]+".txt"+"'(.)*)"
	dico = {}
	expreArticle = regex.expreReguliereArticle()+regex.expreReguliereCode()
	expreDoc = r'[0-9]{2}(a|d|mc|soa|da)[0-9]{2}\.txt'
	maxValue = 0
	secondMaxValue = 0
	for line in f.readlines():
		lineSplitted = re.split("'", line)
		#print lineSplitted
		if doc in lineSplitted:
			i = 0
			listDico = []
			for item in lineSplitted:
				m = re.match(expreDoc,item)
				if m is not None:
					listDico.append(m.group(0))
				else:
					m = re.search('code', item)
					if m is not None:
						i = i + 1
			if i > 1 :
				for item in listDico:
					print item
					if item not in dico or dico[item]<i:
						dico[item] = i
			if i > maxValue:
				secondMaxValue = maxValue
				maxValue = i
			else:
				if i > secondMaxValue:
					secondMaxValue = i
	res = open('test_similitude/sim'+doc,'w')
	#del dico[doc]
	#print dico[doc]
	print dico, maxValue, secondMaxValue
	for key, value in dico.iteritems():
		if value >= secondMaxValue-1:
			res.write(key+" "+str(value)+'\n')
	res.close()'''


	'''f = open('Semi-lattice_Similarity/attributes_sans_simpification.txt','r')
	res = open('formatage.txt','w')
	setAttribute = set()
	for line in f.readlines():
		if line[0]!='n':
			res.write(regex.formatArticle(line))
			setAttribute.add(regex.formatArticle(line))
	print len(list(setAttribute))
	res.close()
	f.close()
	
	f = open('du code.txt','r')
	res = open('result.txt','w')
	expre = regex.expreReguliereArticle()
	print expre
	i = 0
	for line in f.readlines():
		m = re.search(expre,line)
		if m is not None:
			i = i + 1
			res.write(m.group(0)+'\n')
		else:
			res.write(line)
	print str(i)
	i = 0
	texte = "salut ca va bien ?"
	m = re.search("salut", texte)
	num = "n° 3457-2"
	print regex.supprNumero(num)
	print m.group(0), m.start(), m.end()
	date = regularExpression.exprReguliereDate()
	avis = regularExpression.exprReguliereDecision()
	print date, avis'''
	'''f = open('article.txt','r')
	numarticle = regex.exprReguliereNumArticle()
	for line in f.readlines():
		pipe = re.search('|', line)
		if pipe is not None:
			print pipe.start()
		else:
			print "pas trouvé"
		for m in re.finditer(numarticle, line):
			#print(m.group(0), m.start(), m.end())
			#	print line[m.start():]
			i = i + 1
	print i
	#print numarticle
	f = open('article.txt','r')
	res = open('articleL.txt', 'w')
	resdate = open('date.txt', 'w')
	resavis = open('decision.txt','w')
	for line in f.readlines():
		for m in re.finditer(date, line):
			print(m.group(0))
			resdate.write(m.group(0)+"\n")
		for m in re.finditer(r'L\. [0-9]{1,3}(-| )[0-9]', line):
	        	print(m.group(0), m.start(), m.end())
			res.write(m.group(0)+"\n")
		
		for m in re.finditer(avis, line):
	        	print(m.group(0), m.start(), m.end())
			resavis.write(m.group(0)+"\n")
	res.close()
	f.close()
	resdate.close()
	resavis.close()'''

