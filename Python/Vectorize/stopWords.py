import re


def buildStopWords():
	with open('stop.txt','r') as infile:
		with open('frenchStopWords.txt','w') as outfile:
			for line in infile.readlines():
				line = line.split('|')
				line = line[0].rstrip()
				if len(line) > 0:
					outfile.write(line+'\n')


buildStopWords()