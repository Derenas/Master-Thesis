import toolsCluster

wordToVec = toolsCluster.readDico("clusterWord2Vec.txt","list")
tfidf = toolsCluster.readDico("cluster49.txt","list")
listRes = []

for element in wordToVec:
	res = [filter(lambda x: x in element, sublist) for sublist in tfidf]
	listRes += res

listRes2 = []

for element in listRes:
	if len(element) > 4:
		element = [val[1:-1	] for val in element]
		listRes2.append(element)

with open("intersection.txt","w") as outfile:
	for element in listRes2:
		element.sort()
		outfile.write(str(element)+" - "+str(len(element))+'\n')