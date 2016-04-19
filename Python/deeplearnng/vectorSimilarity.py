import csv
from scipy.spatial import distance

vectors = {}
for key, val in csv.reader(open("vectors.csv")):
    vectors[key] = val

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
		dist = distance.euclidean(list1,list2)
		matrix[doc1][item2[0]] = dist
	print str(j)+" fichiers sur "+str(size)
	
with open('matrix.csv','w') as outfile:
	writer = csv.writer(outfile)
	for key, val in matrix.items():
		writer.writerow([key,val])

for item in matrix.items():
	print item[0], max(item[1], key=item[1].get)