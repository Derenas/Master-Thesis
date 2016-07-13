import csv
from sklearn.cluster import KMeans
import toolsCluster


matrix = []
name = []
for key, val in csv.reader(open("vectors.csv")):
    name.append(key[:-4])
    list1 = val[1:-1].split(', ')
    list1 = [float(i) for i in list1]
    matrix.append(list1)



kmeans = KMeans(n_clusters=50)
res = kmeans.fit_predict(matrix)


with open("clusterWord2Vec.txt","w") as outfile:
	dico = toolsCluster.clusterToDico(res,name)
	for key, val in dico.items():
		outfile.write(str(key)+" : "+str(val)+'\n')


#print matrix['01d04.txt']