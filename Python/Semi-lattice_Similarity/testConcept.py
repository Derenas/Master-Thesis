# -*- coding: utf-8 -*-
'''
Created on 9 mars 2016

@author: virgilt
'''

from concepts import Context	
import graphviz
import re
import collections

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

#exporte le context en json pour pouvoir l'utiliser sur une application
def exportContext(objects,attributes,matrix):
	res = open('test.json','w')
	#creation d'une liste de dictionnaire
	json = []
	#creation du premier dictionnaire de json
	parametre = {}
	parametre["ObjNames"] = objects
	attribut = {}
	attribut["AttrNames"] = attributes
	parametre["Params"] = attribut
	#creation du deuxieme dictionnaire de json
	data = {}
	data["Count"] = len(matrix)
	listAttributes = []
	for element in matrix:
		dico = {}
		attr = getAllTrue(element)
		dico["Count"] = len(attr)
		dico["Inds"] = attr
		listAttributes.append(dico)	
	data["Data"] = listAttributes
	#parametre = OrderedDict(sorted(parametre.items(), key=lambda t: t[0]))
	#data = OrderedDict(sorted(data.items(), key=lambda t: t[0]))
	json.append(parametre)
	json.append(data)
	json = str(json)
	json = re.sub("'",'"',json)
	json = re.sub(", ",",",json)
	json = re.sub(": ",":",json)
	print json
	whatever = '([0-9]|[a-z]|[A-Z]|[, "])*'
	paramexpression = r'"Params":\{"AttrNames":\['+whatever+'\]\}'
	params = re.search(paramexpression,json)
	objnamesexpression = r'"ObjNames":\['+whatever+'\]'
	objnames = re.search(objnamesexpression,json)
	print params.group(),objnames.group()
	if params.start() < objnames.start():
		newjson = json[:params.start()]
		newjson += objnames.group()+','+params.group()+json[objnames.end():]
		json = newjson
	res.write(json)
	res.close()

def getAllTrue(objet):
	res = []
	i = 0
	length = len(objet)
	for i in range(0,length):
		if objet[i] == True:
			res.append(i)
	print res
	return res
		

if __name__ == '__main__':
	animaux = ["Bat","Eagle","Monkey","Parrot fish","Penguin","Shark","Lantern fish"]
	proprietes = ["breathes in water","can fly","has beak","has hands","has skeleton","has wings","lives in water","is viviparous","produces light"]
	matrix = [
		(False, True, False, False, True, True, False, True, False), # Bat
		(False, True, True, False, True, True, False, False, False), # Eagle
		(False, False, False, True, True, False, False, True, False), # Monkey
		(True, False, True, False, True, False, True, False, False), # Parrot Fish
		(False, False, True, False, True, True, True, False, False), # Penguin
		(True, False, False, False, True, False, True, False, False), # Shark
		(True, False, False, False, True, False, True, False, True)] # Lantern Fish
	exportContext(animaux,proprietes,matrix)
	c = Context(animaux, proprietes, matrix)  # doctest: +ELLIPSIS
	'''clients = ['Anne','Basile','Carole']
	articles = ['fromage','vin','lait','lessive']
	matrix = [
		(True, False, True, False), #A
		(True, True, False, True), #B
		(True,False,True,True)] #C
	c = Context(clients, articles, matrix)'''
	#print c
	#c.lattice.graphviz(view=True)
	#for intent, extent in c.lattice:
		#print intent, extent
	c.tofile('animaux.txt',frmat='cxt',encoding='utf-8')
	writeConcepts(c.lattice)
