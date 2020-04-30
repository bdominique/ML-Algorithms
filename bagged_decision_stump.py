"""
a Python program to perform bagging on the decision 
stump that I wrote in decision_tree.py.

This program will create a bootstrapped dataset and then run
my decision stump on it and obtain predictions labels.
It will repeat this a 100 times and output the majority vote of 
the predictions. 
"""
import sys
import random
import numpy as np
datafile = sys.argv[1]


f = open(datafile)
data = []
i = 0
l = f.readline()

#Read data
while(l != ''):
	a = l.split()
	l2 = []
	for j in range(0,len(a),1):
		l2.append(float(a[j]))
#	l2.append(1)
	data.append(l2)
	l = f.readline()

rows = len(data)
cols = len(data[0])
f.close()

#Read labels

labelfile = sys.argv[2]
f = open(labelfile)
trainlabels = {}
l = f.readline()
class_size = 0

while (l!= ''):
	a = l.split()
	trainlabels[int(a[1])] = int(a[0])
	if (trainlabels[int(a[1])] == 0):
		trainlabels[int(a[1])] = -1
	l = f.readline()

ginivals = []
split = 0
l3 = [0, 0]
for j in range(0, cols, 1):
    ginivals.append(l3)
temp = 0
col = 0
decision_value = []
for j in range (0,rows,1):
	decision_value.append(0)



# Create a bagged dataset with replacement:
def subsample(dataset = data, row_length = rows, ratio=1.0):
	sample = list()
	num_sample = round(row_length * ratio)
	while len(sample) < num_sample:
		index = random.randrange(row_length)
		sample.append(dataset[index])
	return sample


iter = 100

for i in range(0,iter,1): 
	new_data = subsample()
	print("bagged data for this round: ",new_data)
	for j in range(0, cols, 1):
		
		column_list = [item[j] for item in new_data]
		keys = sorted(range(len(column_list)), key=lambda k: 
column_list[k])
	    
		column_list.sort()
	#	print("j: ", j, "column: ", column_list)
		prevgini = 0
		prevrow = 0
		ginival = []
		for s in range(1, rows, 1):
			lsize = s
			rsize = rows - s
			lp = 0
			rp = 0
		
			for l in range(0, s, 1):
				if (trainlabels.get(l) == -1):
					lp += 1
			for l in range(s,rows,1):
				if (trainlabels.get(l) == -1):
					rp += 1
		
			gini = (lsize / rows) * (lp / lsize) * (1 - lp / lsize) + (rsize / rows) * (rp / rsize) * (1 - rp / rsize)
	
			ginival.append(gini)
	
			prevgini = min(ginival)
		
			if (ginival[s-1] == float(prevgini)):
				ginivals[j][0] = ginival[s-1]
				ginivals[j][1] = s
		if (j ==0):
			temp = ginivals[j][0]
		if (ginivals[j][0] <= temp):
			temp = ginivals[j][0]
			column = j
			split = ginivals[j][1]
			if (split != 0):
				split = (column_list[split] + column_list[split - 
1]) / 2
	#print("col: ", column, "split: ", split)
	
	for p in range(0,rows,1):
		if (trainlabels.get(p) == None):
			if (data[p][column] < split):
				decision_value[p] += 1
			else:
				decision_value[p] -= 1
	

for p in range (0,rows,1):
	if(trainlabels.get(p) == None):
		if (decision_value[p] < 0):
			print("0", p)
		else:
			print("1", p) 
