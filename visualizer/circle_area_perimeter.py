import math

from matplotlib import pyplot as plt

#the greater the area of our knowledge, the greater the perimeter of our ignorance

xs2=[]
ys2=[]



for r in range(2,20):
    a=math.pi*math.pow(r,2)
    p=2*math.pi*r
    xs2.append(a)
    ys2.append(p)
    print(str(p) + " " + str(a))

plt.scatter(xs2, ys2)    

xs3=[]
ys3=[]

for r in range(2,20):
    v=(4/3)*math.pi*math.pow(r,3)
    s=4*math.pi*math.pow(r,2)
    xs3.append(v)
    ys3.append(s)
    print(str(s) + " " + str(v))    

plt.scatter(xs3, ys3)
plt.show()

