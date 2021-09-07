"""
from star_tracker.basic import angleCalculator
from numpy import pi
import matplotlib.pyplot as plt
from star_tracker.kvector import Kvector
from star_tracker.loadfile import loadRawData, plotCatalog2D
class TestKvector:
    def test_generateTriadList(self):
        id,theta,phi,mag = loadRawData("data/stars.csv")
        l = Kvector.generateTriadList(id, theta, phi, 30*np.pi/180)
        k=Kvector(l)
        assert True == True
        #assert str(k) == '2'
    
    def test_save_load_Kvector(self):
        id,theta,phi,mag = loadRawData("data/stars.csv")
        l = Kvector.generateTriadList(id, theta, phi, 30*np.pi/180)
        k = Kvector(l)
        k.save()
        a = Kvector.load()
        assert str(k) == str(a)
    def test_drawKVector(self):
        k = Kvector.load()
        k.drawKVector(plt, markersize=0.001)
        plt.savefig("data/k-vector.png", dpi = 1000)
        assert True == True
    def test_search(self):
        k = Kvector.load()
        theta = [46.0, 44.18, 29.68, 29.84, 27.64, 41.28, 26.96, 34.04, 31.96, 33.51, 50.55]
        phi = [148.34, 149.06, 164.06, 176.36, 165.86, 152.37, 172.30, 161.17, 157.04,162.52,147.15]
        theta = [t*pi/180 for t in theta]
        phi = [p*pi/180 for p in phi]
        ang = []
        for i in range(len(theta)):
            ang.append([])
            for j in range(len(theta)):
                ang[i].append(angleCalculator(theta[i],phi[i],theta[j],phi[j]))

        m = k.search(ang, 0.15*pi/180)
        assert m == [649, 20, 22, 32, 124, 204, 1277, 1456, 256, 1199, 1476]
    def test_pivoting(self):
        k = Kvector.load()
        k.drawKVector(plt, markersize=0.001, title = 'k-vector')
        f1 = k.search(10*np.pi/180, 0.25*np.pi/180)
        f2 = k.search(25*np.pi/180, 0.25*np.pi/180)
        f1,f2 = Kvector.Pivoting(f1,f2)
        f3 = k.search(35*np.pi/180, 0.25*np.pi/180)
        f1,f3 = Kvector.Pivoting(f1,f3)
        assert len(f3) >= 100
    """