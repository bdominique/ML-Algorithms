"""
a Python program for the logistic discrimination gradient
descent algorithm. Labels must remain 0 for the logistic 
regression gradient descent.

Use eta=.01 and stopping condition of .0000001.
"""
import sys
import random
import numpy as np
import math
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
	l2.append(1)
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

while (l!= ''):
	a = l.split()
	trainlabels[int(a[1])] = int(a[0])
	#if(trainlabels[int(a[1])] == 0):
	#	trainlabels[int(a[1])] = -1
	l = f.readline()

w = []
for j in range(0,cols,1):
	w.append(0)
for j in range(0, cols, 1):
	w[j] = 0.002*random.random() - 0.001

print("intial w = ", w)
max_count = 100000
prev_obj = 10000
obj = 0
eta = 0.01
tol = 0.0000001
dp = 0
count = 0
#def dotproduct(wi, xi):
#	dp = 0
#	for j in range(0,cols,1):
#		dp += wi[j] * xi[j]
#	return dp	

while (np.abs(prev_obj-obj) > tol and count<max_count):
	prev_obj = obj
	dellf = []
	for j in range(0,cols,1):
		dellf.append(0)
	for i in range(0,rows,1):
		if (trainlabels.get(i) != None):
			dp = np.dot(np.transpose(w), data[i])
			#print(i, " ", dp)
			ex = (trainlabels[i]) - (1/(1+ (math.exp(-1*dp))))
			for j in range(0,cols,1):
				if (j == cols-1):
					dellf[j] += ex
				else:
					dellf[j] += (ex)*data[i][j]
	print("gradient: ",dellf)

	#Update w
	for j in range(0,cols,1):
		w[j] = w[j] + eta*dellf[j]

	
	#compute error
	obj = 0
	for i in range(0,rows,1):
		if (trainlabels.get(i) != None):
			dp = np.dot(np.transpose(w), data[i])
			if (trainlabels[i] == 1):
				obj += -1*trainlabels[i]*math.log(1/(1+math.exp(-1*dp))) 
			else:
				obj += -1*math.log(math.exp(-1*dp)/(1+math.exp(-1*dp)))
	print(count, " " ,"Error = ", obj)
	

	count += 1
	
normw = 0
print("w = ")
for j in range(0,cols-1, 1):
	normw += w[j]**2
	print(w[j])

normw = np.sqrt(normw)
print("||w|| = ", normw)

d_origin = w[cols-1]
d_origin = d_origin / normw
print("distance to origin is ", d_origin)



for i in range(0,rows,1):
	if(trainlabels.get(i) == None):
		dp = np.dot(np.transpose(w),data[i])
		if(dp>0):
			print("1 ", i)
		else:
			print("0 ", i)	
