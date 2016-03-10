# -*- coding: utf-8 -*-
'''
Created on 9 mars 2016

@author: virgilt
'''


import os
import regularExpression
import re
import sys

def getAllFiles():
	listfiles = []
	for dossier, sous_dossiers, fichiers in os.walk('./../../Avis_Decisions/pdftotext'):
     		#print('##### %s #####' % dossier)
     		#print("Sous dossiers : %s" % sous_dossiers)
     		#print("Fichiers : %s" % fichiers)
		for fichier in fichiers:
			listfiles.append(dossier+'/'+fichier)
	return listfiles

def printFiles():
	print getAllFiles()		

if __name__ == '__main__':
  	regularExpression.rechercherMots(sys.argv[1:])
