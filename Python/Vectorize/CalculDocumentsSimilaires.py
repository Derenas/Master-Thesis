with open("distanceMinEucli.txt","r") as eucli:
	with open("distanceMinAngular.txt","r") as angular:
		linesE = eucli.readlines()
		linesA = angular.readlines()
		count = 0
		for i in range(0,len(linesA)):
			linA = linesA[i].split("\t")
			linE = linesE[i].split("\t")
			if (linE[1] == linA[1]):
				count += 1
			count = float(count)
		print count/len(linesA)