import math
import random
import matplotlib.pyplot as plt

n = 100000.0
Yn = []
# tn = dict()
X_choice = [-1,1]
Xi = []
for i in range(int(n)):
	Xi.append(random.choice(X_choice))
print(len(Xi))

for num in range(int(n)+1):
	t = num/n
	floor_value = int(math.floor(n*t))
	sum_Xi = 0
	for i in range(1, floor_value+1):
		sum_Xi = sum_Xi + Xi[i-1]
		# print(i,sum_Xi)
	Yi = sum_Xi/math.sqrt(n)
	Yn.append(Yi)

#######plot############
plt.plot(Yn)
plt.show()