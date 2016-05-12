import numpy

with open("listDoc.txt","r") as infile:
	nameDoc = [line.rstrip() for line in infile.readlines()]

matrix = numpy.load("clusterMatrix.dat")

print matrix

listOfCluster = []

size = 2

for cluster in matrix:
	elements = list(numpy.array(cluster).reshape(-1,))
	dico = {}
	for i in range(0,size):
		dico[i] = []
	for i in range(0,len(elements)):
		dico[elements[i]].append(nameDoc[i])

	listOfCluster.append(dico)
	size += 1

print listOfCluster[-1]
