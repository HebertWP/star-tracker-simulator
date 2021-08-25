from pair import Pair
from kvector import Kvector
from loadfile import loadRawData
import matplotlib.pyplot as plt
import numpy as np

k = Kvector.load()
k.drawKVector(plt, markersize=0.001, title = 'k-vector')
f1 = k.search(10*np.pi/180, 0.25*np.pi/180)
print("before pivot 10º: ",len(f1))
f2 = k.search(25*np.pi/180, 0.25*np.pi/180)
print("before pivot 25º: ",len(f2))
f1,f2 = Kvector.Pivoting(f1,f2)
print("after pivot 10º: ",len(f1))
print("after pivot 25º: ",len(f2))
f3 = k.search(35*np.pi/180, 0.25*np.pi/180)
print("before pivot 35º: ",len(f3))
f1,f3 = Kvector.Pivoting(f1,f3)
print("after pivot 10º: ",len(f1))
print("after pivot 35º: ",len(f3))
plt.savefig("data/k-vector.png")