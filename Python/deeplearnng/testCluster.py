from sklearn.cluster import KMeans
import numpy
from scipy import sparse


matrix = numpy.load("tf_idf.dat")

print " -------------------------------------------------- "

#numpMatrix = numpy.matrix(matrix)

test = list(numpy.array(matrix).reshape(-1,))

clusterMatrix = []

with open('cluster.txt','w') as outfile:
	for i in range(2,50):
		kmeans = KMeans(n_clusters=i)
		res = kmeans.fit_predict(test[0])
		outfile.write('[')
		for val in res:
			outfile.write(str(val)+' ')
		outfile.write(']'+'\n')
		print str(i)
		clusterMatrix.append(res)

numpMatrix = numpy.matrix(clusterMatrix)

numpMatrix.dump("clusterMatrix.dat")
# print kmeans.transform(matrix)
# print kmeans.predict(matrix)
