# -*- coding: utf-8 -*-

'''import nltk
import io
from nltk.tokenize import TreebankWordTokenizer

f = io.open('00d10.txt','rU',encoding='utf-8')
text = ' '.join([line.rstrip() for line in f])

tokenizer = nltk.data.load('tokenizers/punkt/french.pickle')

tokens = tokenizer.tokenize(text)

wordtokenizer = TreebankWordTokenizer()


wlist =[]
for token in tokens:
	wtoken = wordtokenizer.tokenize(token)
	wlist.append(wtoken)
	
for i in range(0,10):
	print wlist[i]'''

'''nltk.data.load('tokenizers/punkt/french.pickle')
tokens = [french_tokenizer.tokenize(s) for s in sentences]'''

from nltk.tokenize import TreebankWordTokenizer
import io
# On instancie notre tokenizer
tokenizer = TreebankWordTokenizer()

f = open('00d10.txt','r')
text = ' '.join([line.rstrip() for line in f])

tokens = tokenizer.tokenize(text)

print(tokens)  
