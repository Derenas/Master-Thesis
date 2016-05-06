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
import sys
import roman

#Ecrit la liste des attributs dans un fichier externe
def writeAttributes(liste,name):
	res = open('latticeEtContext/attributes'+name+'.txt','w')
	res.write("nombre d'attributs : "+str(len(liste))+'\n')
	for item in liste:
		res.write(item+'\n')
	res.close()

#Ecrit la liste des concepts et leur nombre dans un fichier externe
def writeConcepts(lattice,name):
	res = open('latticeEtContext/concepts'+name+'.txt','w')
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
# sert à rien pour l'instant
def correctSyntaxe(attribut):
	if attribut == 'code du commerce':
		return 'code de commerce'
	elif attribut == 'code de travail':
		return 'code du travail'
	else:
		return attribut

#Construit l'expression reguliere qui retrouve tous les attributs
def expreAttribute():
	expre = regex.expreReguliereArticle()+regex.expreReguliereCode()
	return expre	


#exporte le context en json pour pouvoir l'utiliser sur une application
def exportContext(objects,attributes,matrix,name):
	res = open('latticeEtContext/lattice'+name+'.json','w')
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
	#print json
	whatever = '([0-9]|[a-z]|[A-Z]|[, ".-])*'
	paramexpression = r'"Params":\{"AttrNames":\['+whatever+'\]\}'
	params = re.search(paramexpression,json)
	objnamesexpression = r'"ObjNames":\['+whatever+'\]'
	objnames = re.search(objnamesexpression,json)
	#print params.group(),objnames.group()
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
	#print res
	return res

def developAttribute(attribute):
	developpedList = []
	code = ""
	developpedList.append(attribute.lower())
	m = re.search('du code',attribute)
	if m is not None:
		art = attribute[:m.start()]
		code = attribute[m.start()+3:]
	developpedList.append(code.lower())
	if attribute[1] == " ":
		ind = art.rfind('-') 
		while(ind!=-1):
			art = art[:ind]
			developpedList.append(art+" du "+code)
			ind = art.rfind('-')
		#print attribute,code.lower()
		if attribute[2] == "0":
			livre = "Livre 0 du "+code
		else:
			livre = "Livre "+roman.toRoman(int(attribute[2]))+" du "+code
		developpedList.append(livre.lower())
		if attribute[3].isdigit():
			if attribute[3] == "0":
				titre = "Titre 0 du "+livre
			else:
				titre = "Titre "+roman.toRoman(int(attribute[3]))+" du "+livre
			developpedList.append(titre.lower())
	return developpedList

def buildAttributes(setOfAttributes):
	setRes = set()
	for attribute in setOfAttributes:
		setOfDeclension = developAttribute(attribute)
		for att in setOfDeclension:
			setRes.add(att)
	return setRes


#Construit la lattice à partir de documents
def buildLattice(pattern = True, inputFiles = "dec", inputAttributes = "arts"):
	if pattern == True:
		name = "WithPS"
	else:
		name = "WithoutPS"
	print inputFiles, inputAttributes, name
	#Le contexte a construire
	matrixAttribute = []
	#
	listFiles = []
	#Liste des fichiers lus pour construire le contexte
	if(inputFiles == "dec"):
		listAllFiles = fg.getAllDecisions()
	elif(inputFiles == "avis"):
		listAllFiles = fg.getAllAvis()
	elif(inputFiles == "all"):
		listAllFiles = fg.getAllFiles()
	else:
		print "choix non reconnu. Choix possibles : 'dec' 'avis' 'all'"
		listAllFiles = fg.getAllDecisions()
	#Nombre de fichiers lus
	lengthAllFiles = len(listAllFiles)
	#L'ensemble des attributs du contexte
	setOfAttributes = set()
	#L'ensemble des attributs modifiés du contexte
	setFormated = set()
	#L'expression régulière des attributs possibles des différents textes
	if (inputAttributes == "arts"):
		expre = expreAttribute()
	elif(inputAttributes == "artsdocs"):
		expre = expreAttribute()+'|'+regex.exprReguliereDecision()
	else:
		print "choix non reconnu. Choix possibles : 'arts' 'docs' 'artsdocs'"
		expre = expreAttribute()
	#Compteur de fichiers lus 
	i = 0
	#Lecture des fichiers pour lister les attributs
	for dfile in listAllFiles:
		f = open(dfile,'r')
		#Enlever les sauts de lignes dûs au copier/coller du pdf
		data = ' '.join([line.rstrip() for line in f])
		#Pour chaque expression trouvée dans le texte
		for m in re.finditer(expre, data):
			#Expression réguliere
			attributFormated = m.group(0)
			#Lissage de l'expression :
			#Enlever les accents
			attributFormated = regex.removeAccent(attributFormated)
			#Corriger les erreurs potentielles
			attributFormated = correctSyntaxe(attributFormated)
			attributFormated = regex.supprNumero(attributFormated)
			setOfAttributes.add(attributFormated)
		i = i + 0.5
		if i%100==0:
			print str(int(i))+' fichiers lus sur '+str(lengthAllFiles)
	#Modification des attributs pour éviter les doublons
	setOfAttributes = list(setOfAttributes)

	for item in setOfAttributes:
		setFormated.add(regex.formatArticle(item))
	if pattern == True:
		developAttributes = buildAttributes(setFormated)
		setFormated =  list(developAttributes)

	#Nombre d'attributs dans le contexte
	lenset = len(setFormated)
	print str(lenset)
	#Construction du contexte
	for dfile in listAllFiles:
		f = open(dfile, 'r')
		data = ' '.join([line.rstrip() for line in f])
		#Lister les documents pour la construction du contexte
		listFiles.append(regex.nomDocument(dfile))
		#Construction d'une ligne du contexte
		nuplet = (False,)*lenset
		listuple = list(nuplet)
		#Pour chaque expression
		for m in re.finditer(expre, data):
			attributFormated = m.group(0)
			#Formater l'expression régulière
			attributFormated = regex.removeAccent(attributFormated)
			attributFormated = correctSyntaxe(attributFormated)
			attributFormated = regex.supprNumero(attributFormated)
			attributFormated = regex.formatArticle(attributFormated)
			#Si pattern, on découpe chaque attribut
			if pattern == True:
				listAtt = developAttribute(attributFormated)
				for item in listAtt:
					#Trouver l'indice de l'attribut
					index = setFormated.index(item)
					#Mettre à jour la valeur
					listuple[index] = True
			#Sinon on cherche juste les attributs
			else:
				index = setFormated.index(attributFormated)
				listuple[index] = True

		i = i + 0.5
		if i%100==0:
			print str(int(i))+' fichiers lus sur '+str(lengthAllFiles)
		nuplet = tuple(listuple)
		#Ajoute le nouvel objet au contexte
		matrixAttribute.append(nuplet)
	print str(int(i))+' fichiers lus sur '+str(lengthAllFiles)
	#Sauvegarde les attributs dans un txt
	writeAttributes(setFormated,name)
	#sauvegarde le contexte dans un json
	exportContext(listFiles,setFormated,matrixAttribute,name)
	c = Context(listFiles,setFormated,matrixAttribute)
	print "construction de la lattice. Cela peut prendre quelques instants"
	c.lattice.graphviz(view=True)
	#Sauvegarde le contexte dans un txt
	writeConcepts(c.lattice,name)
	c.tofile('latticeEtContext/saveLatticeWithPS.txt',frmat='cxt',encoding='utf-8')

if(len(sys.argv)>=2):
	if(len(sys.argv)>=3):
		if(len(sys.argv)>=4):
			buildLattice(sys.argv[1],sys.argv[2],sys.argv[3])
		else:
			buildLattice(sys.argv[1],sys.argv[2])
	else:
		buildLattice(sys.argv[1])
else:
	buildLattice()
#print (regex.expreReguliereCode())



