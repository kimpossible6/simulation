## sequence random variable
## 1 or -1
import math
import numpy as np
import random
import matplotlib.pyplot as plt
def run_experiment():
	n = 10000.0
	Yn = []
	# tn = dict()
	X_choice = [-1,1]
	Xi = []
	for i in range(int(n)):
		Xi.append(random.choice(X_choice))
	# print(len(Xi))

	for num in range(int(n)+1):
		t = num/n
		floor_value = int(math.floor(n*t))
		sum_Xi = 0
		for i in range(1, floor_value+1):
			sum_Xi = sum_Xi + Xi[i-1]
			# print(i,sum_Xi)
		Yi = sum_Xi/math.sqrt(n)
		Yn.append(Yi)
	return Yn




#######plot############

# a = run_experiment()
# print(a)
# Yn_list = []
# for val in a.values():
# 	Yn_list.append(val)
# plt.plot(Yn_list)
# plt.show()
# print(Yn)
# print(tn)
# print(Yn)
rep_list=[]
# a1 = run_experiment()
# print(a1)
for rep in range(400):
	a2 = run_experiment()
	plt.plot(a2)
# print(sum(rep_list)/len(rep_list))
# print(np.var(rep_list))
# print(rep_list)

# plt.figure()
# plt.hist(rep_list, bins=10)
plt.show()


# Yn_list = []
# tn_list = []
# for val in Yn.values():
# 	Yn_list.append(val)

# for val in tn.values():
# 	tn_list.append(val)
# plt.plot(Yn_list)
# print(Yn_list)
# plt.show()

