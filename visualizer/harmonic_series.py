from matplotlib import pyplot as plt

N_ITER = 100000
xs=[]
ys=[]
sum = 0
for i in range(1,N_ITER):
    xs.append(i)
    ys.append(sum)
    sum = sum + 1/i

plt.scatter(xs,ys, color='red')
plt.show()     