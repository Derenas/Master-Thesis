import csv

matrix = {}
for key, val in csv.reader(open("matrix.csv")):
    matrix[key] = val
#print dicL
count = 0
for item in matrix.items():
	print count
	dico ={}
	listkeysvalues = item[1][1:-1].split(', ')
	for couple in listkeysvalues:
		(key, value) = couple.split(': ')
		#print key,value
		dico[key[1:-1]] = float(value)
	matrix[item[0]] = dico
	count += 1

for doc in matrix.items():
	matrix[doc[0]][doc[0]] = 100

#print matrix['12d13.txt']

with open("distance.txt","w") as res:
	for item in matrix.items():
		#print item[0], min(item[1], key=item[1].get)
		res.write(item[0]+"\t"+min(item[1], key=item[1].get)+"\n")


#print matrix['01d04.txt']
	