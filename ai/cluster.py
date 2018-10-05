import csv
import scipy.cluster.hierarchy as hcluster
import scipy.spatial.distance as ssd
import numpy as np
from matplotlib import pyplot as plt

def readData():
	data = []
	f = open('output.csv', 'r', encoding='utf-8')
	rdr = csv.reader(f)
	lineNum = 0
	for line in rdr:
		if lineNum % 2 == 0:
			data.append(line)
		lineNum = lineNum + 1
	f.close()
	return data

def run():
	distanceData = readData()
	distanceMatrix = [[]]
	i = 0
	while(True):
		if(int(distanceData[i][0]) != 0):
			break
		distanceMatrix.append([])
		i = i+1

	for i in range(len(distanceData)):
		doc1 = int(distanceData[i][0])
		doc2 = int(distanceData[i][1])
		distance = float(distanceData[i][2])
		distanceMatrix[doc1].insert(doc2, 0.0)
		distanceMatrix[doc2].insert(doc1, distance)

	for i in range(len(distanceMatrix)):
		distanceMatrix[i].insert(i, 0.0)

	#print(distanceMatrix)
	'''
	newMatrix = ssd.squareform(distanceMatrix)
	Z = hcluster.linkage(newMatrix, method="complete")
	fig = plt.figure(figsize=(100,60))
	dn = hcluster.dendrogram(Z)
	plt.show()
	'''

	x = np.array(distanceMatrix)
	linkage_matrix = hcluster.linkage(x,method="complete",metric='euclidean')
	dendogram = hcluster.dendrogram(linkage_matrix,truncate_mode='none')
	plt.show()
