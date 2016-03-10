# -*- coding: utf-8 -*-
'''
Created on 9 mars 2016

@author: virgilt
'''

import re
import main

def exprReguliereDate():
	listemois = ['janvier','février','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','décembre']
	expre = '([1-3][0-9]|1er) '
	dismois = '('
	for mois in listemois:
		dismois = dismois+mois+'|'
	dismois = dismois[:-1]+')'	
	expre = expre + dismois
	expre = expre +' [0-2][0-9]{3}'
	return expre

def rechercherMot(file, mot):
	ls = []
	filetxt = re.search(r'[0-9]{2}(a|d|mc|soa|da)[0-9]{2}\.txt',file)
    	f = open(file,'r')
	for line in f.readlines():
		m = re.search(mot, line)
		if m is not None:
			ls.append(line[:-1]+" | "+filetxt.group(0)+"\n")
    	f.close()
	return ls
	

def rechercherMots(mots):
	i = 0
	for mot in mots:
		f = open(mot+'.txt','w')
		files = main.getAllFiles()
		for file in files:
			lines = rechercherMot(file,mot)	
			for line in lines:
				f.write(line)
			i = i+1
			if i%10 == 0:
				print(str(i)+' fichiers lus sur '+str(len(files)))
		f.close()
