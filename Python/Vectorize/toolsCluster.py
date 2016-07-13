from sklearn.cluster import KMeans

def clusterToDico(cluster,name=False):
	if name == False:
		with open("listDoc.txt","r") as infile:
			nameDoc = [line.rstrip() for line in infile.readlines()]
	else:
		nameDoc = name
		print nameDoc
	nbClusters = max(cluster)
	size = len(cluster)
	dico = {}
	for i in range(0,nbClusters+1):
		dico[i] = []
	for i in range(0,size):
		dico[cluster[i]].append(nameDoc[i])

	return dico

def readDico(filename,typeRes):
	with open(filename,"r") as infile:
		lines = infile.readlines()
	if(typeRes == "list"):
		res = []
		for line in lines:
			line = line.split(':')[1]
			listLine = line[1:-2].split(', ')
			res.append(listLine)


	elif(typeRes == "dico"):
		res = {}
		for line in lines:
			line = line.split(':')
			res[line[0]] = line[1][1:-1].split(', ')

	else:
		res = None
	return res