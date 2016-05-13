# -*- coding: utf-8 -*-

import nltk
import io
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import WordPunctTokenizer

f = io.open('00d10.txt','rU',encoding='utf-8')
text = ' '.join([line.rstrip() for line in f])

tokenizer = nltk.data.load('tokenizers/punkt/french.pickle')

tokens = tokenizer.tokenize(text)
<<<<<<< HEAD
print tokens
#wordtokenizer = TreebankWordTokenizer()
wordtokenizer = WordPunctTokenizer()
=======

#wordtokenizer = TreebankWordTokenizer()
wordtokenizer = WordPunctTokenizer()

>>>>>>> 65731833ce47e4eeaa569bee2b4a190593f1e219
wlist =[]
for token in tokens:
	wtoken = wordtokenizer.tokenize(token)
	print wtoken
	wlist.append(wtoken)
	
res = io.open('res.txt','w',encoding='utf-8')
for sentence in wlist:
	for word in sentence:
		res.write(word)
		res.write(u' ')
	res.write(u'\n')
'''nltk.data.load('tokenizers/punkt/french.pickle')
tokens = [french_tokenizer.tokenize(s) for s in sentences]'''

'''from nltk.tokenize import TreebankWordTokenizer
import io
# On instancie notre tokenizer
tokenizer = TreebankWordTokenizer()

f = open('00d10.txt','r')
text = ' '.join([line.rstrip() for line in f])

tokens = tokenizer.tokenize(text)

print(tokens)  '''
