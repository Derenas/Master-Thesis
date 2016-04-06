# -*- coding: utf-8 -*-
'''
Created on 9 mars 2016

@author: virgilt
'''

import re

def similitude():
	f = open('Semi-lattice_Similarity/concepts.txt','r')
	res = open('similarite.txt','w')
	expre = r"\((\'[0-9]{2}(a|d|mc|soa|da)[0-9]{2}\.txt\'(, )?){2,15}\)"
	print expre
	for line in f.readlines():
		#print line
		m = re.search(expre,line)
		if m is not None:
			newline = line[m.end():]
			#print newline
			count = newline.count(',')
			if count > 6:
				res.write(str(count+1)+'\n'+line)
	f.close()
	res.close()


similitude()
