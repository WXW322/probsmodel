import random
import math
from scipy.stats import norm
import matplotlib.pyplot as plt


def norm_dist_prob(data):
    return norm.pdf(data,loc = 0,scale = 8)

T = 20000
pi = [0 for i in range(T)]
sigma = 1
t = 0
while(t < T - 1):
    t = t + 1
    t_num = norm.rvs(loc=pi[t - 1], scale=sigma, size=1, random_state=None)
    print(t_num)
    alpha = min(1,norm_dist_prob(t_num[0])/(norm_dist_prob(pi[t - 1])))
    t_u = random.uniform(0,1)
    if t_u < alpha:
        pi[t] = t_num[0]
    else:
        pi[t] = pi[t - 1]
f_pi = pi[10000:]
plt.scatter(f_pi,norm.pdf(f_pi,loc = 0,scale = 8))
num_bins = 50
plt.hist(f_pi,num_bins,normed = 1,facecolor = 'blue',alpha = 0.8)
plt.show()