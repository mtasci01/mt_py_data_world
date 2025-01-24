import numpy as np
import matplotlib.pyplot as plt

treeNodes = np.array([
    [0,0],
    [-1,-1],
    [1,-1],
    [-1,-2],
    [1,-2],
    [1,-3]
])
#rows num of dimensions, cols num of nodes 
treeNodesT = np.transpose(treeNodes)
print("geometrically flipping a tree (original in red) with root at the origin")


rotationMat = np.array([
    [1, 0],
    [0,-1]
])

treeNodesRotated = np.matmul(rotationMat,treeNodesT)

plt.ylim([-10,10])
plt.ylim([-10,10])
x_list_or = treeNodesT[0]
y_list_or = treeNodesT[1]
x_list_fl = treeNodesRotated[0]
y_list_fl = treeNodesRotated[1]

plt.scatter(x_list_or,y_list_or, color='red')
plt.scatter(x_list_fl,y_list_fl, color='blue')
plt.show() 
