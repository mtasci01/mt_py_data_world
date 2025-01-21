import math
import numpy as np 
import matplotlib.pyplot as plt

SIDE_LEN = 2
left_corner = np.array([0,0])
right_corner = left_corner + np.array([SIDE_LEN,0])
top_corner = left_corner+ np.array([SIDE_LEN/2,(SIDE_LEN*math.pow(3,1/3))/2])
MAX_REC_DEPTH = 6
XLIM_NEG = -1
XLIM_POS = 3
YLIM_NEG = -1
YLIM_POS = 3

simple = False

def triangle_sierpinski():
    triangle_list = []
    triangle_sierpinski_rec(left_corner,right_corner,top_corner,triangle_list,0)

    for t in triangle_list:
        plt.gca().add_patch(plt.Polygon(t,fill=False))
 
    plt.xlim(XLIM_NEG, XLIM_POS)
    plt.ylim(YLIM_NEG, YLIM_POS)
    plt.show()    

def triangle_sierpinski_rec(left_corner,right_corner,top_corner, triangle_list, rec_depth):
    if rec_depth > MAX_REC_DEPTH:
        return
    triangle_list.append(np.array([left_corner,right_corner,top_corner]))

    left_half = [(left_corner[0] + top_corner[0])/2,(left_corner[1] + top_corner[1])/2]
    right_half = [(top_corner[0] + right_corner[0])/2,(top_corner[1] + right_corner[1])/2]
    bottom_half = [(left_corner[0] + right_corner[0])/2,(left_corner[1] + right_corner[1])/2]
    rec_depth = rec_depth + 1
    triangle_sierpinski_rec(left_corner,bottom_half,left_half,triangle_list,rec_depth)
    triangle_sierpinski_rec(left_half,right_half,top_corner,triangle_list,rec_depth)
    triangle_sierpinski_rec(bottom_half,right_corner,right_half,triangle_list,rec_depth)
    

def simple_triforce():

    X1= np.array([left_corner,right_corner,top_corner])
    t1 = plt.Polygon(X1)
    plt.gca().add_patch(t1)

    X2= []
    for p in X1:
        X2.append(p + np.array([SIDE_LEN,0]))
    t2 = plt.Polygon(X2)
    plt.gca().add_patch(t2)

    X3= []
    for p in X1:
        X3.append(p + np.array([SIDE_LEN/2,(SIDE_LEN*math.pow(3,1/3))/2]))
    t3 = plt.Polygon(X3)
    plt.gca().add_patch(t3)

    plt.xlim(XLIM_NEG, XLIM_POS)
    plt.ylim(YLIM_NEG, YLIM_POS)
    plt.show()

if simple:
    simple_triforce()  
else:
    triangle_sierpinski()  