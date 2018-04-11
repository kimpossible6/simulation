## sequence random variable
## 1 or -1
import math
import random
import matplotlib.pyplot as plt
n = 10000.0

Yn = dict()
tn = dict()
X_choice = [-1,1]
for num in range(int(n)):
	t = num/n
	floor_value = int(math.floor(n*t))
	sum_Xi = 0
	for i in range(1, floor_value+1):
		Xi = random.choice(X_choice)
		sum_Xi = sum_Xi + Xi
		# print(i,sum_Xi)
	Yi = (1/math.sqrt(n))*sum_Xi
	Yn[num] = Yi
	tn[num] = t
print(Yn)
print(tn)
# print(Yn)
Yn_list = []
tn_list = []
for val in Yn.values():
	Yn_list.append(val)

for val in tn.values():
	tn_list.append(val)
plt.plot(tn_list, Yn_list)
plt.show()

