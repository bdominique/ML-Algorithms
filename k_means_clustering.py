"""
A Python Program thet performs K-Means Clustering, where
the user must specify the number of clusters or k that they desire.
"""
import sys
import random

datafile = sys.argv[1]
f = open(datafile)
data = []
i = 0
l = f.readline()

#Read Data

while (l != ''):
	a = l.split()
	l2 = []
	for j in range(0, len(a), 1):
		l2.append(float(a[j]))
	data.append(l2)
	l = f.readline()

rows = len(data)
cols = len(data[0])
f.close()

k = int(sys.argv[2])
"""
#Read labels

labelfile = sys.argv[2]
f = open(labelfile)
trainlabels = {}
n = [0,0]
l = f.readline()

while(l != ''):
	a = l.split()
	trainlabels[int(a[1])] = int(a[0])
	l = f.readline()
	n[int(a[0])] += 1
"""

###create a dictionary to store the cluster that each datapoint joins###
keys = []
for i in range (0,k,1):
	keys.append(i)
#cluster = {key: [] for key in keys}
#print(cluster)

###pick k random points to begin the clustering; do this outside the loop###

cluster_list = random.sample(data,k)
print("first cluster list: ",cluster_list)
#print(len(cluster_list))


min_dist_index = 0
converged = False

count = 0
old_cluster_list = []

while (converged == False and count < 500):
	count += 1
	
	cluster = {key: [] for key in keys}
#	old_cluster_list = cluster_list
	print("cluster list for round ", count,": ",cluster_list)



	for i in range(0,rows,1):
		#for each row of data, calculate the euclidean distance between it and each datapoint in the cluster_list###
		euclid_distances = [0]*k
		for h in range (0,len(cluster_list), 1):
			for j in range(0,cols,1):
				euclid_distances[h] +=  (data[i][j] - cluster_list[h][j])**2	
			euclid_distances[h] = euclid_distances[h]**0.5
		min_dist_index = euclid_distances.index(min(euclid_distances))
		cluster[min_dist_index].append(i)
		#print("cluster: ", cluster)



	index = -1
	cluster_list = [0]*k

	for value in cluster.values():
		index += 1
		m = [0]*cols
		size = len(value)
		for i in range (0,size, 1):
			for j in range(0,cols,1):
				m[j] += data[int(value[i])][j]
		for j in range (0,cols,1):
			if (m[j] != 0):
				m[j] = m[j]/size
			else:
				continue
		cluster_list[index] = m



#	print("clusters after this iteration: ", cluster_list)

	if (old_cluster_list != [] and cluster_list == old_cluster_list):
		converged = True
		print("converged")
	else:
		old_cluster_list = cluster_list
		continue

for i in range (0,rows,1):
	index = -1
	for value in cluster.values():
		index += 1
		size = len(value)
		for j in range(0,size,1):
			if (i == value[j]):
				print(index, value[j])
