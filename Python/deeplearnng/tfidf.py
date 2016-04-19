# -*- coding: utf-8 -*-

import nltk
import string
import os
import io

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import SnowballStemmer
from nltk.tokenize import WordPunctTokenizer

path = '../../../Avis_Decisions/pdftotext/Decisions'
path = 'echantillon'
token_dict = {}
stemmer = SnowballStemmer('french')

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text): 
    #wordtokenizer = WordPunctTokenizer()
    #tokens = wordtokenizer.tokenize(text)
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems

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
	
