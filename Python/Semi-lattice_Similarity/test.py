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

def printFiles():
	print fg.getAllFiles()		

if __name__ == '__main__':
	f = open('concepts.txt','r')
	doc = sys.argv[1]+".txt"
	expre = r"((.)*'"+sys.argv[1]+".txt"+"'(.)*)"
	dico = {}
	expreArticle = regex.expreReguliereArticle()+regex.expreReguliereCode()
	expreDoc = r'[0-9]{2}(a|d|mc|soa|da)[0-9]{2}\.txt'
	maxValue = 0
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
			if i > 1:
				for item in listDico:
					if item not in dico or dico[item]<i:
						dico[item] = i
			maxValue = max(i, maxValue)
	res = open('test_similitude/similitude'+doc,'w')
	for key, value in dico.iteritems():
		if value >= maxValue-1:
			res.write(key+" "+str(value)+'\n')
	res.close()


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

