#	 -*- coding: utf-8 -*-
'''
Created on 9 mars 2016

@author: virgilt
'''

import os

#retourne tous les fichiers décisions et avis
def getAllFiles():
	listfiles = []
	#chemin pour acceder à tous les fichiers.
	#Le script doit etre lancé depuis le répertoire python
	for dossier, sous_dossiers, fichiers in os.walk('./../../Avis_Decisions/pdftotext'):
     		#print('##### %s #####' % dossier)
     		#print("Sous dossiers : %s" % sous_dossiers)
     		#print("Fichiers : %s" % fichiers)
		for fichier in fichiers:
			listfiles.append(dossier+'/'+fichier)
	return listfiles

#retourne tous les avis
def getAllAvis():
	listavis = []
	#chemin pour acceder à tous les fichiers.
	#Le script doit etre lancé depuis le répertoire python
	for fichier in os.listdir('./../../Avis_Decisions/pdftotext/Avis'):
		listavis.append('./../../Avis_Decisions/pdftotext/Avis/'+fichier)
	return listavis

#retourne toutes les décisions
def getAllDecisions():
	listdecis = []
	#chemin pour acceder à tous les fichiers.
	#Le script doit etre lancé depuis le répertoire python
	for fichier in os.listdir('./../../Avis_Decisions/pdftotext/Decisions'):
		listdecis.append('./../../Avis_Decisions/pdftotext/Decisions/'+fichier)
	return listdecis
