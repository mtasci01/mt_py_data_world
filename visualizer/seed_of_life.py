
import math
from matplotlib import pyplot as plt

r = 10
xs=[]
ys=[]
num_circles  = 6
step = (math.pi*2)/num_circles
origin_x = 0
origin_y = 0
fig, ax = plt.subplots()
ax.add_patch(plt.Circle((origin_x, origin_y), r, fill=False))
t = 0
for i in range(num_circles):
    xs.append(origin_x + r*math.cos(t))
    ys.append(origin_y + r*math.sin(t))
    t = t + step
    ax.add_patch(plt.Circle((xs[i], ys[i]), r, fill=False))

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
plt.axis('equal')
plt.show()
 
