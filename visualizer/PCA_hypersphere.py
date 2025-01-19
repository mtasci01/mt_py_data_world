from matplotlib import pyplot as plt
import numpy as np
from sklearn.decomposition import PCA

#projecting a 4d hypersphere to a 3d space
pca = PCA(n_components=3)
center = [1,2,3,4]
radius = 10
spherePoints=[]
numOfPoints=1000
for i in range(numOfPoints):
    phi1=np.random.rand()*np.pi
    phi2=np.random.rand()*np.pi
    phi3=np.random.rand()*2*np.pi
    x1=radius*np.sin(phi1)*np.sin(phi2)*np.cos(phi3)
    x2=radius*np.sin(phi1)*np.sin(phi2)*np.sin(phi3)
    x3=radius*np.sin(phi1)*np.cos(phi2)
    x4=radius*np.cos(phi1)
    point4d=[x1,x2,x3,x4]
    spherePoints.append(point4d)
spherePoints = np.array(spherePoints)
circlePoints=pca.fit_transform(spherePoints)

plt3D = plt.axes(projection='3d')
plt3D.scatter3D(circlePoints[:,0],circlePoints[:,1],circlePoints[:,2])
plt.show()

