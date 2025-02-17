import math
from matplotlib import pyplot as plt
import numpy as np

origin = [0,0]
radius = 5
circles_list = []
circles_list.append(plt.Circle(origin, radius, fill=False))
fig, ax = plt.subplots()


#vertical circles
x = origin[0]
y = origin[1] + radius*4
for i in range(5):
    circle = plt.Circle([x,y], radius, fill=False)
    y = y - radius*2
    if i != 2:
        circles_list.append(circle)

#1st diagonal
x = origin[0] - radius*4*(math.sqrt(3)/2) #inradius
y = origin[1] + radius*2

np_diag  = np.array([x,y])
np_step_vec = np.array(origin) - np_diag
np_step_vec = np_step_vec/np.linalg.norm(np_step_vec)
np_step_vec = np_step_vec*2*radius

for i in range(5):
    circle = plt.Circle(np_diag, radius, fill=False)
    np_diag = np_diag + np_step_vec
    if i != 2:
        circles_list.append(circle)    

#2nd diagonal
x = origin[0] - radius*4*(math.sqrt(3)/2) #inradius
y = origin[1] - radius*2

np_diag  = np.array([x,y])
np_step_vec = np.array(origin) - np_diag
np_step_vec = np_step_vec/np.linalg.norm(np_step_vec)
np_step_vec = np_step_vec*2*radius

for i in range(5):
    circle = plt.Circle(np_diag, radius, fill=False)
    np_diag = np_diag + np_step_vec
    if i != 2:
        circles_list.append(circle)   
       

for c1 in circles_list:
    ax.add_patch(c1)    
    for c2 in circles_list:
        plt.plot([c1.get_center()[0],c2.get_center()[0]],[c1.get_center()[1],c2.get_center()[1]])

ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
plt.axis('equal')
plt.show()