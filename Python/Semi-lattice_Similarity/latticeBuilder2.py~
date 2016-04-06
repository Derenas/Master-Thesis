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
import files



def buildLattice():
	res = open('allavis.txt','w')
	listavis = getAllAvis()
	expre = regex.exprReguliereDecision()
	setOfAvis = set()
	for avis in listavis:
		f = open(avis, 'r')
		data = ' '.join([line.rstrip() for line in f])
		filetxt = re.search(r'[0-9]{2}(a|d|mc|soa|da)[0-9]{2}\.txt',avis)
		for m in re.finditer(expre, data):
			numavis = regex.supprNumero(m.group(0))
			setOfAvis.add(numavis)
	        	#print(regularExpression.supprNumero(m.group(0)), m.start(), m.end())
			#res.write(regularExpression.supprNumero(m.group(0))+"\n")		
	print len(setOfAvis)
	lenset = len(setOfAvis)
	for avis in setOfAvis:
		res.write(avis+'\t')
	res.close()
	matrixAttribute = []
	listFiles = []
	setOfAvis = list(setOfAvis)
	for avis in listavis:
		f = open(avis, 'r')
		data = ' '.join([line.rstrip() for line in f])
		filetxt = re.search(r'[0-9]{2}(a|d|mc|soa|da)[0-9]{2}\.txt',avis)
		listFiles.append(filetxt.group(0))
		nuplet = (False,)*lenset
		listuple = list(nuplet)
		for m in re.finditer(expre, data):
			numavis = regex.supprNumero(m.group(0))
			index = setOfAvis.index(numavis)
			listuple[index] = True
		nuplet = tuple(listuple)
		matrixAttribute.append(nuplet)
	c = Context(listFiles,setOfAvis,matrixAttribute)
	c.lattice.graphviz(view=True)
	i = 0	
	for extent, intent in c.lattice:
		i = i + 1
	#	print('%r %r' % (extent, intent))
	print("nombre de concepts "+str(i))
buildLattice()

