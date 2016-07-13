import csv
import math
from scipy.spatial import distance

def euclidianDistance(vectors):
	size = len(vectors)
	matrix = {}
	maxDist = 0
	j = 0
	for item1 in vectors.items():
		doc1 = item1[0]
		matrix[doc1] = {}
		j = j + 1
		for item2 in vectors.items():
			list1 = item1[1][1:-1].split(', ')
			list2 = item2[1][1:-1].split(', ')
			list1 = [float(i) for i in list1]
			list2 = [float(i) for i in list2]
			dist = distance.euclidean(list1,list2)
			matrix[doc1][item2[0]] = dist
			maxDist = max(dist,maxDist)
		print str(j)+" fichiers sur "+str(size)
	print maxDist
	return matrix

def dotproduct(v1, v2):
	return sum((a*b) for a, b in zip(v1, v2))

def length(v):
	return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
	cos = dotproduct(v1, v2) / (length(v1) * length(v2))
	if cos > 1:
		cos = 1
	return math.degrees(math.acos(cos))

def angularDistance(vectors):
	maxAngle = 0
	size = len(vectors)
	matrix = {}
	j = 0
	for item1 in vectors.items():
		doc1 = item1[0]
		matrix[doc1] = {}
		j = j + 1
		for item2 in vectors.items():
			list1 = item1[1][1:-1].split(', ')
			list2 = item2[1][1:-1].split(', ')
			list1 = [float(i) for i in list1]			
			list2 = [float(i) for i in list2]
			angular = angle(list1,list2)
			matrix[doc1][item2[0]] = angular
			maxAngle = max(angular, maxAngle)
		print str(j)+" fichiers sur "+str(size)
	print maxAngle
	return matrix

vectors = {}
for key, val in csv.reader(open("vectors.csv")):
    vectors[key] = val

# matrixAngul = angularDistance(vectors)
# with open('matrixAngul.csv','w') as outfile:
# 	writer = csv.writer(outfile)
# 	for key, val in matrixAngul.items():
# 		writer.writerow([key,val])

matrixEucl = euclidianDistance(vectors)
with open('matrixEucli.csv','w') as outfile:
	writer = csv.writer(outfile)
	for key, val in matrixEucl.items():
		writer.writerow([key,val])



'''for item in matrix.items():
	print item[0], max(item[1], key=item[1].get)'''