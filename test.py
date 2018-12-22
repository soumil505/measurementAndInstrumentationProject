import filter
import numpy as np
import matplotlib.pyplot as plt

f = filter.Filter(3)
t = np.arange(-10, 10, 0.1)
#l = np.arange(-10,10,0.1) >= 0
#l = np.arange(-10,10) == 0
l = np.sin(t)+np.random.rand(len(t))/2
list = []


for i in l:
    list = np.append(list, i)
    list = f.real_time(list)

plt.plot(t,list)
plt.plot(t,l)
plt.show()
