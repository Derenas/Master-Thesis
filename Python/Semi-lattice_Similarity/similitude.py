# -*- coding: utf-8 -*-
'''
Created on 9 mars 2016
	
@author: virgilt
'''

import re
import sys

def similitude(name, numberOfSim):
	f = open('latticeEtContext/concepts'+name+'.txt','r')
	res = open('latticeEtContext/similarite'+name+'.txt','w')
	expre = r"\((\'[0-9]{2}(a|d|mc|soa|da)[0-9]{2}\'(, )?){2,18}\)"
	for line in f.readlines():
		m = re.search(expre,line)
		if m is not None:
			newline = line[m.end():]
			count = newline.count(',')
			if count > numberOfSim-2:
				res.write(str(count+1)+'\n'+line)
	f.close()
	res.close()


if(len(sys.argv)>=2):
	if(len(sys.argv)>=3):
		similitude(sys.argv[1],int(sys.argv[2]))
	else:
		similitude(sys.argv[1],10)
else:
	similitude("WithoutPS",10)
