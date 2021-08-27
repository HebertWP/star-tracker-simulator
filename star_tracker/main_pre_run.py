"""
from pair import Pair
from kvector import Kvector
from loadfile import loadRawData
import matplotlib.pyplot as plt
import numpy as np

k = Kvector.load()
k.drawKVector(plt, markersize=0.001, title = 'k-vector')
f1 = k.search(10*np.pi/180, 0.25*np.pi/180)
f2 = k.search(25*np.pi/180, 0.25*np.pi/180)
f3 = k.search(20*np.pi/180, 0.25*np.pi/180)
f4 = k.search(15*np.pi/180, 0.25*np.pi/180)

print("before pivot 10º: ",len(f1))

f1,f2 = Kvector.Pivoting(f1,f2)
print("after pivot 10º: ",len(f1))

f1,f3 = Kvector.Pivoting(f1,f3)
print("after pivot 10º: ",len(f1))

f1,f4 = Kvector.Pivoting(f1,f4)
print("after pivot 10º: ",len(f1))
for i in f1:
    print(i)
"""
from math import pow
x=1
i=1
while( x<=1000):
    x=pow(2,x)
    i+=1
print(i)