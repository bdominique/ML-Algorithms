"""
Least Squares Gradient Descent Algorithm.
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
class_size = 0

while (l!= ''):
	a = l.split()
	trainlabels[int(a[1])] = int(a[0])
	if (trainlabels[int(a[1])] == 0):
		trainlabels[int(a[1])] = -1
	l = f.readline()

w = []

for j in range(0,cols,1):
	w.append(0)
for j in range(0, cols, 1):
	w[j] = 0.002*random.random() - 0.001

print("intial w = ", w)
max_count = 10000
prev_obj = 10000
obj = 0
eta = 0.0001
tol = 0.001
dp = 0
count = 0
def dotproduct(wi, xi):
	dp = 0
	for j in range(0,cols,1):
		dp += wi[j] * xi[j]
	return dp	

while (np.abs(prev_obj-obj) > tol and count<max_count):
	prev_obj = obj
	dellf = []
	for j in range(0,cols,1):
		dellf.append(0)
	for i in range(0,rows,1):
		if (trainlabels.get(i) != None):
			#print(trainlabels[i])
			dp = dotproduct(w, data[i])
			#print("dp = ", dp)
			#print(i, " ", dp)
			for j in range(0,cols,1):
				dellf[j] += (trainlabels[i] - dp)*data[i][j]
	print("gradient: ",dellf)
	#Update w
	for j in range(0,cols,1):
		w[j] = w[j] + eta*dellf[j]

	
	#compute error
	obj = 0
	for i in range(0,rows,1):
		if (trainlabels.get(i) != None):
			obj += (trainlabels[i] - dotproduct(w,data[i]))**2
	print(count, " " ,"Error = ", obj)
	

	count += 1
	
normw = 0
print("w = ")
for j in range(0,cols-1, 1):
	normw += w[j]**2
	print(w[j])

normw = np.sqrt(normw)
#print("||w|| = ", normw)

d_origin = np.abs(w[cols-1])
d_origin = d_origin / normw
print("distance to origin is ", d_origin)

for i in range(0,rows,1):
	if(trainlabels.get(i) == None):
		dp = np.dot(np.transpose(w),data[i])
		if(dp>0):
			print("1 ", i)
		else:
			print("0 ", i)	
