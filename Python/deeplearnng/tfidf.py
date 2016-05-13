# -*- coding: utf-8 -*-
<<<<<<< HEAD
import sys
=======

>>>>>>> 65731833ce47e4eeaa569bee2b4a190593f1e219
import nltk
import string
import os
import io
<<<<<<< HEAD
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import SnowballStemmer
from nltk.tokenize import WordPunctTokenizer
import operator
from sklearn.cluster import KMeans
import numpy

def loadStopWords():
	french_stop_words = []
	#Lire la liste des stopWords français
	with open('frenchStopWords.txt','r') as infile:
		for line in infile.readlines():
			line = line.rstrip()
			#ajoute les mots en unicode car plus simple à comparer par la suite
			french_stop_words.append(stemmer.stem(line.decode('unicode_escape')))
	return french_stop_words
=======

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import SnowballStemmer
from nltk.tokenize import WordPunctTokenizer

path = '../../../Avis_Decisions/pdftotext/Decisions'
path = 'echantillon'
token_dict = {}
stemmer = SnowballStemmer('french')
>>>>>>> 65731833ce47e4eeaa569bee2b4a190593f1e219

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text): 
<<<<<<< HEAD
=======
    #wordtokenizer = WordPunctTokenizer()
    #tokens = wordtokenizer.tokenize(text)
>>>>>>> 65731833ce47e4eeaa569bee2b4a190593f1e219
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems

<<<<<<< HEAD
def column(matrix, i):
    return [row[i] for row in matrix]

def tenMaxColumns(matrix,dico,features):
	#Liste des documents
	names = dico.keys()
	#Listes des abscisses/ordonnées des valeurs non nulles dans la matrice
	coupleList = matrix.nonzero()
	#Taille des listes
	lenght = len(coupleList[0])
	#Dictionnaire trié
	dicotri ={}
	#Créer un dictionnaire pour chaque texte
	for text in names:
		dicotri[text] = {}
	#Parcours de la liste des éléments non nuls
	for i in range(0,lenght):
		#Récupération de l'abscisse
		abscisse = coupleList[0][i]
		#Récupération de l'ordonnée
		ordonnee = coupleList[1][i]
		#Mise à jour du dictionnaire
		dicotri[names[abscisse]][features[ordonnee]] = matrix[abscisse, ordonnee]
		#Affichage de la progression
		if i%10000==0:
			print str(i/1000)+'k termes lus sur '+str(lenght/1000)+'k'

	listOfTerms = set()
	with io.open('restfidf/termesFrequency.txt','w',encoding='utf-8') as outfile:
		#Parcours du dictionnaire
		for key, var in dicotri.items():
			#Tri des valeurs du dictionnaire + conservation des 10 plus élevées
			newA = dict(sorted(var.iteritems(), key=operator.itemgetter(1), reverse=True)[:10])
			outfile.write(unicode(key+'\n'))
			#Sauvegarde des 10 termes les plus fréquents par texte
			for mot, freq in newA.items():
				listOfTerms.add(mot)
				outfile.write(unicode(mot)+':'+unicode(str(round(freq,3)))+' - ')
			outfile.write(u'\n')

	with io.open('wordWithHighFreq.txt','w',encoding='utf-8') as outfile:
		for terme in listOfTerms:
			outfile.write(unicode(terme+'\n'))
		

def writeFeatures(feature_names,name):
	with io.open(name,'w',encoding='utf-8') as outfile:
		for name in feature_names:
			outfile.write(name+'\n')

def saveMatrix(matrix,name):

	numpMatrix = numpy.matrix(matrix)

	numpMatrix.dump(name)

def writeMatrix(matrix,name):
	with io.open(name,'w',encoding='utf-8') as outfile:

		#print tfs.getnnz(), tfs.shape[0], tfs.shape[1]
		lines = matrix.shape[1]
		cols = matrix.shape[0]
		for name in feature_names:
			outfile.write(name+'\t')
			outfile.write(u'\n')
		for col in range(0,cols):
			if col%100==0:
					print str(col)+' fichiers lus sur '+str(cols)
			for line in range(0,lines):
				#print tfs[col,line]
				freq = matrix[col,line]
				outfile.write(unicode(round(freq,4))+'\t')
		outfile.write(u'\n')

def writeFrequencyByDocuments(matrix,dico,name):
	coupleList = matrix.nonzero()
	lenght = len(coupleList[1])
	texts =[]
	documentNames = dico.keys()
	numberOfDocs = len(set(coupleList[0]))
	if len(documentNames) == numberOfDocs:
		for i in range(0,numberOfDocs):
			texts.append("")

		for i in range(0,lenght):
			texts[coupleList[0][i]] += unicode(feature_names[coupleList[1][i]]+' - '+str(matrix[coupleList[0][i], coupleList[1][i]])+'\n')
		
		lentexts = len(texts)

		for i in range(0,lentexts):
			with io.open(name+documentNames[i],'w',encoding='utf-8') as outfile: 
				outfile.write(texts[i])

def buildDictionnary(path):
	dicoToken = {}
	for subdir, dirs, files in os.walk(path):
		for file in files:
			file_path = subdir + os.path.sep + file
			shakes = open(file_path, 'r')
			text = ' '.join([line.rstrip() for line in shakes])
			lowers = text.lower()
			no_punctuation = lowers.translate(None, string.punctuation)
			dicoToken[file] = no_punctuation
	with open('listDoc.txt','w') as outfile:
		for vals in dicoToken.keys():
			outfile.write(vals[:-4]+'\n')	
	return dicoToken

def clusteringTFIDf(matrix):
	kmeans = KMeans(n_clusters=2)
	print kmeans.fit_predict(matrix)

def tfidf(writeDoc=False,writeMatrix=False):
	path = '../../../Avis_Decisions/pdftotext/Decisions'
	token_dict = buildDictionnary(path)
	frStopWords = loadStopWords()
	tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words=frStopWords)
	tfs = tfidf.fit_transform(token_dict.values())

	features = tfidf.get_feature_names()

	writeFeatures(features,'features.txt')
	if writeMatrix == True:
		writeMatrix(tfs,'matrix.txt')

	if writeDoc == True:
		writeFrequencyByDocuments(tfs,token_dict,'restfidf/tfidf')

	tenMaxColumns(tfs,token_dict,features)

	clusteringTFIDf(tfs)

	saveMatrix(tfs,"tf_idf.dat")



#Programme
stemmer = SnowballStemmer('french')
if(len(sys.argv)>=2):
	if(len(sys.argv)>=3):
		tfidf(sys.argv[1],sys.argv[2])
	else:
		tfidf(sys.argv[1])
else:
	tfidf()
=======
for subdir, dirs, files in os.walk(path):
    for file in files:
		print file
        file_path = subdir + os.path.sep + file
        shakes = open(file_path, 'r')
        text = ' '.join([line.rstrip() for line in shakes])
        lowers = text.lower()
        no_punctuation = lowers.translate(None, string.punctuation)
        token_dict[file] = no_punctuation

#this can take some time
tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs = tfidf.fit_transform(token_dict.values())
feature_names = tfidf.get_feature_names()
f = io.open('features.txt','w',encoding='utf-8')
for name in feature_names:
	f.write(name+'\n')
f.close()
matrix = io.open('matrice.txt','w',encoding='utf-8')
print tfs.getnnz(), tfs.shape[0], tfs.shape[1]
lines = tfs.shape[1]
cols = tfs.shape[0]
for name in feature_names:
	matrix.write(name+'\t')
matrix.write(u'\n')
for col in range(0,cols):
	for line in range(0,lines):
		#print tfs[col,line]
		freq = tfs[col,line]
		matrix.write(unicode(round(freq,4))+'\t')
	matrix.write(u'\n')
matrix.close()
'''for col in tfs.nonzero()[1]:
	print feature_names[col], ' - ', tfs[1, col]'''
	
>>>>>>> 65731833ce47e4eeaa569bee2b4a190593f1e219
