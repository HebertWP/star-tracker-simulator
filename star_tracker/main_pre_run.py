from pair import Pair
from kvector import Kvector
from loadfile import loadRawData
import matplotlib.pyplot as plt
import numpy as np

k = Kvector.load()
k.drawKVector(plt, markersize=0.001, title = 'k-vector')
f = k.search(10*np.pi/180, 0.25*np.pi/180)
print(len(f))
plt.savefig("data/k-vector.png")