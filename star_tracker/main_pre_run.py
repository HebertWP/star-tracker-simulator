from pair import generateData,Pair,mergeSort,drawKVector
from loadfile import loadRawData
import matplotlib.pyplot as plt
import numpy as np

name, theta, phi, mag = loadRawData("data/stars.csv")
data = generateData(name,theta,phi,mag, 3, 5, 5*np.pi/180,90*np.pi/180)
print(len(data))
mergeSort(data)
drawKVector(data,plt,markersize=0.001)
plt.savefig("data/k-vector.png", dpi = 1000, title = 'k-vector', c = 'y')