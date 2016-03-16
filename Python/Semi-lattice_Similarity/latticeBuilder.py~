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

def correctSyntaxe(attribut):
	if attribut == 'code du commerce':
		return 'code de commerce'
	elif attribut == 'code de travail':
		return 'code du travail'
	else:
		return attribut

def buildLattice():
	listavis = fg.getAllFiles()
	setOfAvis = set()
	expre = regex.expreReguliereArticle()+regex.expreReguliereCode()
	lengthAvis = len(listavis)
	i = 0
	for avis in listavis:
		f = open(avis,'r')
		data = ' '.join([line.rstrip() for line in f])
		for m in re.finditer(expre, data):
			attributFormated = m.group(0)
			attributFormated = regex.removeAccent(attributFormated)
			attributFormated = correctSyntaxe(attributFormated)
			setOfAvis.add(attributFormated)
		i = i + 1
		if i%100==0:
			print str(i)+' fichiers lus sur '+str(lengthAvis*2)
	print len(setOfAvis)
	matrixAttribute = []
	listFiles = []
	setOfAvis = list(setOfAvis)
	setFormated = set()
	for item in setOfAvis:
		if line[0]!='n':
			setFormated.add(regex.formatArticle(item))
	setFormated =  list(setFormated)
	print len(setFormated)
	lenset = len(setFormated)
	for avis in listavis:
		f = open(avis, 'r')
		data = ' '.join([line.rstrip() for line in f])
		listFiles.append(regex.nomDocument(avis))
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
			print str(i)+' fichiers lus sur '+str(lengthAvis*2)
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



