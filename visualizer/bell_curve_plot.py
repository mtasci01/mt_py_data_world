import numpy as np
import matplotlib.pyplot as plt

#drawing a set of randomly sampled points which will form a normal distribution

rawdata = np.random.randn(100000)
rawdata = list(map(lambda x: round(x,2), rawdata))
cntMap = {}
for x in rawdata:
    if x not in cntMap:
        cntMap[x] = 0
    cntMap[x] = cntMap[x] +1  
xs = list(cntMap.keys())
ys = list(map(lambda x: cntMap[x], xs)  )
xs = np.array(xs)
ys = np.array(ys)       

plt.scatter(xs, ys)
plt.show()