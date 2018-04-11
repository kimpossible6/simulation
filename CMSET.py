##CMSET Algorithm
##Z
import random
import numpy
import math
import matplotlib.pyplot as plt
# from __future__ import division
pk = [0.029,0.039,0.03,0.131,0.083,0.049,0.127,0.012,0.032,0.04,0.029,0.028,0.043,0.012,0.128,0.061,0.027,0.1]
# pk = [0.037,0.128,0.01,0.121,0.081,0.049,0.028,0.112,0.034,0.04,0.018,0.069,0.043,0.012,0.028,0.061,0.029,0.1]
qk = []
initial = 0
for i in pk:
	qk.append(initial+i)
	initial = initial+i
print (len(qk))
# a = 1 
# b = 18
# m = 18

I =[]
A =[]
m = 18
# A = 0 
for i in range(1,19):
	index = float(i)
	Ai = (index-1)/m
	A.append(Ai)
# print A
Ii = 0
for a in A: 
	i = 0
	while(qk[i] <= a):
		i = i+1
	I.append(i+1)
	# print(i+1)
I.append(18)
print(len(I))
print(I)

##partb#####
samples = []
# L = []
X = []
q_est =[]
for i in range(10000):
	num = random.uniform(0,1)
	samples.append(num)
# print(samples)

for i in samples:
	li = int(math.floor(m*i)+1)
	# if (li >18):
	# 	print("yes",li)
	x = li
	# print(x) ## x = 1......18
	# print(qk[x-1]) ## qk has 18 but starts from index 0 - 17, so call qk[x-1]
	while i > qk[x-1]:
		# if x >= 18:
		# 	print("yes")
		# 	break
		# else:
		i
		x = x+1

	X.append(x)
# 

# print(X)

pi_samples_keys =[]
pi_samples = dict()
qi_samples = dict()
i1 = 1 
initial1 = 0
for i in range(18) :
	pi_samples_keys.append(i1)
	i1 += 1

pi_samples = dict.fromkeys(pi_samples_keys,0)

for i in X:
	pi_samples[i] = pi_samples.get(i) + 1

for i in pi_samples.keys():
	qi_samples[i] = initial1 + pi_samples.get(i)
	initial1 = pi_samples.get(i) + initial1
print(qi_samples)


qi_est = dict()
qi_est = dict.fromkeys(pi_samples_keys,0)
for i in qi_samples.keys():
	qi_est[i] = float((qi_samples.get(i))/10000.0)

print(qi_est)

## plot 
Xi = []
for i in qi_est.values():
	Xi.append(i)
plt.plot(qk,Xi, linestyle='-', marker = '*')
plt.show()


# plt.plot(X)
# plt.ylabel('qi')
# for i in range(len(X)):
# 	plt.plot(X[i])
# plt.show()

