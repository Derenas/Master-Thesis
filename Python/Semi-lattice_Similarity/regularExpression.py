# -*- coding: utf-8 -*-
'''
Created on 9 mars 2016

@author: virgilt
'''

import re
import filesGetter as fg

#retourne une expression régulière de disjonction des mots de la liste
def listToDisjonction(listOfWords):
	disjonction = '('
	for word in listOfWords:
		disjonction = disjonction+word+'|'
	disjonction = disjonction[:-1]+')'
	return disjonction

#enlève les accents sur chaque mot, le render lattice n'est pas en utf-8
def removeAccent(word):
	return re.sub('é','e',word)

#retourne l'expression reguliere des différents codes légaux
def expreReguliereCode():
	listecodes = ['général des collectivités', 'commerce', 'postes et télécommunications', 'procédure civile', 'sécurité sociale', 'marchés publics', 'communes', 'travail', 'tourisme', 'santé public']
	liens = r'(d(u|e|es))? (la )?'
	res = '(c|C)ode '
	res = res + liens
	discodes = listToDisjonction(listecodes)
	res = res + discodes
	return res

#retourne l'expression reguliere des articles des codes légaux
def expreReguliereArticle():
	romanNumbers = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV']
	disroman = listToDisjonction(romanNumbers)
	res = '((l|L)ivre '+disroman+'|'
	res = res + '(L|R|D).( )?[0-9]{1,4}((-| )[0-9]{1,3})?(-[0-9]{1,2})?(-[0-9]{1,2})?(, alinéa )?( et suivants)?( (I|II|III|IV|V))?)'
	res = res + ' du '
	return res

#Formate les articles retrouvés pour éviter les redondances
def formatArticle(article):
	res = article
	res = re.sub('C','c',res)
	res = re.sub(' et suivants ',' ',res)
	res = re.sub('Livre','livre',res)
	res = re.sub('\. ','.',res)
	res = re.sub(' ','.',res)
	res = re.sub('\.',' ',res)
	return res

# retourne l'expression reguliere d'une date : XX mois XXXX
def exprReguliereDate():
	listemois = ['janvier','février','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','décembre']
	expre = '([1-3][0-9]|1er) '
	dismois = listTiDisjonction(listemois)	
	expre = expre + dismois
	expre = expre +' [0-2][0-9]{3}'
	return expre

# retourne le code d'une décision ou d'un avis : XX-code-XX
def exprReguliereDecision():
	listeAcronyme = ['SOA', 'D', 'DA', 'A', 'DDC', 'DSA']
	expre = '((n|N)(°|0) )?[0-9]{2}-'
	disacr = listToDisjonction(listeAcronyme)
	expre = expre + disacr
	expre = expre +'-[0-9]{2}'
	return expre

# récupère le nom du document dans le chemin donné en paramètre
def nomDocument(file):
	filetxt = re.search(r'[0-9]{2}(a|d|mc|soa|da)[0-9]{2}',file)
	return filetxt.group(0)

#pas utilisée
def exprReguliereNumArticle():
	expre = 'article '
	expre = expre + '(L\. )?[0-9]{1,3}(-[0-9]{1,2})? (du|de)'
	return expre

# enlève le n° pour normaliser l'écriture
def supprNumero(texte):
	#recherche n° dans le texte
	m = re.search(r'(n|N)(°|0) ', texte)
	if m is not None:
		return texte[m.end():]
	else:
		return texte

#retourne la ligne sur laquelle le mot apparait
def rechercherMot(file, mot):
	ls = []
    	f = open(file,'r')
	for line in f.readlines():
		m = re.search(mot, line)
		if m is not None:
			ls.append(line[:-1]+" | "+nomDocument(file)+"\n")
    	f.close()
	return ls
	
#Pour chaque mot, retourne un fichier avec chaque ligne ou ce mot apparait
def rechercherMots(mots):
	i = 0
	for mot in mots:
		f = open(mot+'.txt','w')
		files = fg.getAllFiles()
		for file in files:
			lines = rechercherMot(file,mot)	
			for line in lines:
				f.write(line)
			i = i+1
			if i%10 == 0:
				print(str(i)+' fichiers lus sur '+str(len(files)))
		f.close()

