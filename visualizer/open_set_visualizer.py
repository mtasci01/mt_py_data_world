import math
import matplotlib.pyplot as plt

#recursively drawing a circle at the edge of an open boundary

iter_num = 7
start_radius = 5

fig, ax = plt.subplots()
circle = plt.Circle((0, 0), start_radius, fill=False)
ax.add_patch(circle)

for i in range(iter_num):
    pow_n = i*-1
    print(pow_n)
    circle = plt.Circle((start_radius - math.pow(10,pow_n), 0), math.pow(10,pow_n), fill=False)
    ax.add_patch(circle)

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
plt.axis('equal')
plt.show()