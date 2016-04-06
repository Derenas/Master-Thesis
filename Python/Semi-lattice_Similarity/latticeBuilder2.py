# -*- coding: utf-8 -*-
'''
Created on 9 mars 2016

@author: virgilt
'''

import os
import regularExpression as regex
import re
from concepts import Context
import graphviz
import filesGetter as fg

#Ecrit la liste des attributs dans un fichier externe
def writeAttributes(liste):
	res = open('attributes.txt','w')
	res.write("nombre d'attributs : "+str(len(liste))+'\n')
	for item in liste:
		res.write(item+'\n')
	res.close()

#Ecrit la liste des concepts et leur nombre dans un fichier externe
def writeConcepts(lattice):
	res = open('concepts.txt','w')
	i = 0
	listeconcepts = []
	for extent, intent in lattice:
		i = i + 1
		listeconcepts.append('%r %r' % (extent, intent)+'\n')
	res.write("nombre de concepts : "+str(i)+'\n')
	for concept in listeconcepts:
		res.write(concept)
	res.close()	

#Corrige les fautes faites par les rédacteurs des décisions
#sert à formater les attributs
def correctSyntaxe(attribut):
	if attribut == 'code du commerce':
		return 'code de commerce'
	elif attribut == 'code de travail':
		return 'code du travail'
	else:
		return attribut

#Construit l'expression reguliere qui retrouve tous les attributs
def expreAttribtute():
	expre = regex.expreReguliereArticle()+regex.expreReguliereCode()
	return expre	


#Construit la lattice à partir de documents
def buildLattice():
	listAllFiles = fg.getAllFiles()
	setOfAllFiles = set()
	expre = expreAttribute()
	lengthAllFiles = len(listAllFiles)
	i = 0
	for dfile in listAllFiles:
		f = open(dfile,'r')
		data = ' '.join([line.rstrip() for line in f])
		for m in re.finditer(expre, data):
			attributFormated = m.group(0)
			attributFormated = regex.removeAccent(attributFormated)
			attributFormated = correctSyntaxe(attributFormated)
			setOfAllFiles.add(attributFormated)
		i = i + 1
		if i%100==0:
			print str(i)+' fichiers lus sur '+str(lengthAllFiles*2)
	print len(setOfAllFiles)
	matrixAttribute = []
	listFiles = []
	setOfAllFiles = list(setOfAllFiles)
	setFormated = set()
	for item in setOfAllFiles:
		if line[0]!='n':
			setFormated.add(regex.formatArticle(item))
	setFormated =  list(setFormated)
	print len(setFormated)
	lenset = len(setFormated)
	for dfile in listAllFiles:
		f = open(dfile, 'r')
		data = ' '.join([line.rstrip() for line in f])
		listFiles.append(regex.nomDocument(dfile))
		nuplet = (False,)*lenset
		listuple = list(nuplet)
		for m in re.finditer(expre, data):
			attributFormated = m.group(0)
			attributFormated = regex.removeAccent(attributFormated)
			attributFormated = correctSyntaxe(attributFormated)
			index = setFormated.index(regex.formatArticle(attributFormated))
			listuple[index] = True
		i = i + 1
		if i%100==0:
			print str(i)+' fichiers lus sur '+str(lengthAllFiles*2)
		nuplet = tuple(listuple)
		matrixAttribute.append(nuplet)
	writeAttributes(setFormated)
	c = Context(listFiles,setFormated,matrixAttribute)
	print "construction de la lattice. Cela peut prendre quelques instants"
	#c.lattice.graphviz(view=True)
	writeConcepts(c.lattice)
	c.tofile('saveLattice.txt',frmat='cxt',encoding='utf-8')

buildLattice()
#print (regex.expreReguliereCode())



