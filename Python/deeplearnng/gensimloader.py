import gensim
import logging
import nltk
import string
import os
import io
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import SnowballStemmer
from nltk.tokenize import WordPunctTokenizer
import csv

stemmer = SnowballStemmer('french')
tokenizer = nltk.data.load('tokenizers/punkt/french.pickle')

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text): 
	tokens = tokenizer.tokenize(text)
	wordtokenizer = WordPunctTokenizer()
	wlist =[]
	for token in tokens:
		wtoken = wordtokenizer.tokenize(token)
		wlist = wlist+wtoken

	stems = stem_tokens(wlist, stemmer)
	return stems


model = gensim.models.Word2Vec.load("model.txt")
# print model
# print model.similarity('cod','argent')
# print model.most_similar(['cod'])
# print model['articl']
path = '../../../Avis_Decisions/pdftotext/Decisions'
vectors = {}
count = 0
for subdir, dirs, files in os.walk(path):
    for file in files:
    	print count, file
    	tvecteur = (0,)*100
    	vecteur = list(tvecteur)
        file_path = subdir + os.path.sep + file
        shakes = io.open(file_path, 'rU',encoding='utf-8')
        text = ' '.join([line.rstrip() for line in shakes])
        lowers = text.lower()
        tokens = tokenize(lowers)
        length = len(tokens)
        for token in tokens:
        	#print token
        	if token in model:
	        	vectorToken = model[token]
	        	for i in range(0,len(vectorToken)):
	        		vecteur[i] = vecteur[i] + vectorToken[i]
        newVec = [x / length for x in vecteur]
        vectors[file] = newVec
        count += 1

with open('vectors.csv','w') as outfile:
	writer = csv.writer(outfile)
	for key, val in vectors.items():
		writer.writerow([key,val])

'''res = open('vectors.txt','w')		
for item in vectors.items():
	res.write(item[0]+'\t'+str(item[1])+'\n')
res.close()'''
