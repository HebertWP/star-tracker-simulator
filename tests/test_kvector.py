import numpy as np
import matplotlib.pyplot as plt
from star_tracker.kvector import Kvector
from star_tracker.loadfile import loadRawData

def test_data_generator():
    id,theta,phi,mag = loadRawData("data/test_data_generator.csv")
    k=Kvector.generateKVectorList(id, theta, phi, mag, 3, 6, 0, 360*np.pi/180)
    p = Kvector(k)
    s = str(p) 
    assert s == '| 0 --> 1 0.35 || 0 --> 3 0.52 || 1 --> 3 0.87 |'

def test_save_load_Kvector():
    id,theta,phi,mag = loadRawData("data/stars.csv")
    k=Kvector.generateKVectorList(id, theta, phi, mag, 5, 7, 5*np.pi/180, 45*np.pi/180)
    p = Kvector(k)
    p.save()
    a = Kvector.load()
    assert str(p) == str(a)
"""
def test_drawKVector():
    k = Kvector.loadKvector()
    k.drawKVector(plt, markersize=0.001)
    plt.savefig("data/k-vector.png", dpi = 1000)
    assert True == True
"""
def test_search():
    id,theta,phi,mag = loadRawData("data/test_data_generator.csv")
    k=Kvector.generateKVectorList(id, theta, phi, mag, 3, 6, 0, 360*np.pi/180)
    p = Kvector(k)
    m = p.search(0.52, 0.1)
    s = ''
    for i in range(0,len(m)):
        s = s + str(m[i])
    m = p.search(1.0, 0.1)
    assert s == '| 0 --> 1 0.35 || 0 --> 3 0.52 |'