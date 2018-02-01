#Monte Carlo Method Integral 1
import math 
import random
import statistics as s
from scipy import stats
from scipy import integrate
from decimal import *
# Define function
def f(x):
	return math.log(1+math.sqrt(abs(x)))

#Define interval
a = -1
b = 3
n = 100

##Store variable in list
xs = []
ys = []
fraction=0
#Generate random x, and compute y
#recalculate for 100 times 
for k in range(100):
    for i in range(n):
        u = random.uniform(0,1)
        x = a + (b-a)*u
        xs.append(x)
        y = (b-a)*f(x)
        ys.append(y)
    sample_mean = s.mean(ys)
    sample_stdev = s.stdev(ys)
    ##student, n=100 calculate 95%
    t_quantile = stats.t.ppf(1-0.025,99)
    Hn0 = t_quantile * sample_stdev/math.sqrt(n)
    lower_CI = sample_mean - Hn0
    upper_CI = sample_mean + Hn0
    ##assume 0.1 half length
    sample_size_n = math.ceil(n*math.pow(Hn0/0.1,2))
    actual_val= integrate.quad(lambda x: f(x), -1, 3)
#    print("HN0",Hn0)
    print ("sample size needed for 0.1 half length = ", sample_size_n)
    print ("95% Confidence Interval", lower_CI, ",", upper_CI)
    print ("the actual integrate value is ", actual_val[0])
    ##check if fulfill 95% CI
    if lower_CI <= actual_val[0]<=upper_CI:
        fraction = fraction + 1
        print("In the CI, all good!",fraction)
    else:
        print("Not in the CI, bad!")
print("the fraction of 95% CI contain the mu is: ", fraction/n)

