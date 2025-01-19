import matplotlib.pyplot as plt

#drawing the vesica piscis symbol which stems from the intersection of 2 circles.

x1 = 0
start_radius = 5
x2 = x1 + start_radius

fig, ax = plt.subplots()
circle = plt.Circle((x1, 0), start_radius, fill=False)
circle2 = plt.Circle((x2, 0), start_radius, fill=False)
ax.add_patch(circle)
ax.add_patch(circle2)

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
plt.axis('equal')
plt.show()