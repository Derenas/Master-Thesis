# -*- coding: utf-8 -*-
import gensim
import logging
import nltk
import string
import os
import io
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import SnowballStemmer
from nltk.tokenize import WordPunctTokenizer
#sentences = [['first', 'sentence'], ['second', 'sentence']]
# train word2vec on the two sentences
#model = gensim.models.Word2Vec(sentences, min_count=1)
path = 'echantillon'
path = '../../../Avis_Decisions/pdftotext/Decisions'
stemmer = SnowballStemmer('french')
texts = []
tokenizer = nltk.data.load('tokenizers/punkt/french.pickle')
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

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
	
i = 0
for subdir, dirs, files in os.walk(path):
    for file in files:
    	print i, file
        file_path = subdir + os.path.sep + file
        shakes = io.open(file_path, 'rU',encoding='utf-8')
        text = ' '.join([line.rstrip() for line in shakes])
        lowers = text.lower()
        texts.append(tokenize(lowers))
        i += 1

model = gensim.models.Word2Vec(texts, size=100, window=5, min_count=1)
model.save("model.txt")