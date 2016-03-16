# -*- coding: utf-8 -*-
'''
Created on 9 mars 2016

@author: virgilt
'''

from concepts import Context
import graphviz

if __name__ == '__main__':
	animaux = ['Bat', 'Eagle', 'Monkey', 'Parrot Fish', 'Penguin', 'Shark','Lantern Fish']
	proprietes = ['breath in water','can fly','has beak','has hands','has skeleton','has wings', 'lives in water','is viviparous','produces light']
	matrix = [
		(False, True, False, False, True, True, False, True, False), # Bat
		(False, True, True, False, True, True, False, False, False), # Eagle
		(False, False, False, True, True, False, False, True, False), # Monkey
		(True, False, True, False, True, False, True, False, False), # Parrot Fish
		(False, False, True, False, True, True, True, False, False), # Penguin
		(True, False, False, False, True, False, True, False, False), # Shark
		(True, False, False, False, True, False, True, False, True)] # Lantern Fish
	c = Context(animaux, proprietes, matrix)  # doctest: +ELLIPSIS
	print c
	c.lattice.graphviz(view=True)
	for intent, extent in c.lattice:
		print intent, extent
	c.tofile('animaux.txt',frmat='cxt',encoding='utf-8')
