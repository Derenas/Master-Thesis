import csv

<<<<<<< HEAD

def second_largest(numbers):
    count = 0
    m1 = m2 = float('-inf')
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1            
            else:
                m2 = x
    return m2 if count >= 2 else None

=======
>>>>>>> 65731833ce47e4eeaa569bee2b4a190593f1e219
matrix = {}
for key, val in csv.reader(open("matrix.csv")):
    matrix[key] = val
#print dicL
count = 0
for item in matrix.items():
<<<<<<< HEAD
	if (count%100)==0:
		print count
=======
	print count
>>>>>>> 65731833ce47e4eeaa569bee2b4a190593f1e219
	dico ={}
	listkeysvalues = item[1][1:-1].split(', ')
	for couple in listkeysvalues:
		(key, value) = couple.split(': ')
		#print key,value
		dico[key[1:-1]] = float(value)
	matrix[item[0]] = dico
	count += 1

<<<<<<< HEAD
'''for doc in matrix.items():
	matrix[doc[0]][doc[0]] = 100'''

#print matrix['12d13.txt']
maxValue = 0
minValue = 100
with open("distanceMin.txt","w") as resMin:
	with open("distanceMax.txt","w") as resMax:
		for item in matrix.items():
			loin = max(item[1], key=item[1].get)
			resMax.write(item[0]+"\t"+loin+"\t"+str(round(matrix[item[0]][loin],4))+"\n")
			#print item[0], min(item[1], key=item[1].get)
			matrix[item[0]][item[0]] = 100
			proche = min(item[1], key=item[1].get)
			resMin.write(item[0]+"\t"+proche+"\t"+str(round(matrix[item[0]][proche],4))+"\n")
			minValue = min(minValue, matrix[item[0]][proche])
			maxValue = max(maxValue, matrix[item[0]][loin])
print maxValue, minValue
=======
for doc in matrix.items():
	matrix[doc[0]][doc[0]] = 100

#print matrix['12d13.txt']

with open("distance.txt","w") as res:
	for item in matrix.items():
		#print item[0], min(item[1], key=item[1].get)
		res.write(item[0]+"\t"+min(item[1], key=item[1].get)+"\n")

>>>>>>> 65731833ce47e4eeaa569bee2b4a190593f1e219

#print matrix['01d04.txt']
	