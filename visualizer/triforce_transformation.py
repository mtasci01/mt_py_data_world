import math
import numpy as np 
import matplotlib.pyplot as plt

side_len = 2
left_corner = np.array([0,0])
right_corner = left_corner + np.array([side_len,0])
top_corner = left_corner+ np.array([side_len/2,(side_len*math.pow(3,1/3))/2])

def simple_triforce():

    X1= np.array([left_corner,right_corner,top_corner])
    t1 = plt.Polygon(X1)
    plt.gca().add_patch(t1)

    X2= []
    for p in X1:
        X2.append(p + np.array([side_len,0]))
    t2 = plt.Polygon(X2)
    plt.gca().add_patch(t2)

    X3= []
    for p in X1:
        X3.append(p + np.array([side_len/2,(side_len*math.pow(3,1/3))/2]))
    t3 = plt.Polygon(X3)
    plt.gca().add_patch(t3)

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.show()

simple_triforce()    