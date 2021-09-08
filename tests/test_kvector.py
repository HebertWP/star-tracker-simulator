import star_tracker.basic as basic
from numpy import pi
import matplotlib.pyplot as plt
import star_tracker.kvector as kvector
import star_tracker.loadfile as loadfile
import star_tracker.quadtree as quadtree
class TestKvector:
    def loadData(self):
        self.n, self.v, self.ar, self.dec = loadfile.loadCatalog("data/stars.csv")
    
    def test_cretequatTree(self):
        points = [quadtree.Point(10,0),quadtree.Point(10,80),quadtree.Point(10,-80),quadtree.Point(350,0),quadtree.Point(350,80),quadtree.Point(350,-80),quadtree.Point(180,0),quadtree.Point(180,80),quadtree.Point(180,-80)]
        kvector.cretequatTree(30,points)
        assert True == True
    
    def test_expandPoints(self):
        self.loadData()
        #n   = [0,   1,   2,   3,   4,   5,   6,   7, 8]
        #ar  = [10, 10,  10, 340, 350, 355, 180, 180, 180]
        #dec = [0,  80, -75, -10,  80, -80,  20,  80, -60]
        points = kvector.expandPoints(self.n, self.ar, self.dec, 30)
        kvector.cretequatTree(30,points)
        assert True == True
    
    def test_removePoints(self):
        self.loadData()
        points = kvector.expandPoints(self.n, self.ar, self.dec, 30)
        qtree=kvector.cretequatTree(30,points)
        for i in range(len(self.n)):
            p = quadtree.Point(self.ar[i], self.dec[i], [self.n[i], self.ar[i], self.dec[i]])
            kvector.removePoint(qtree, p)
        fig = plt.figure()
        points = []
        qtree.query(quadtree.Rect(180, 0, 360 + 2*30, 180 + 2 * 30),points)
        plt.scatter([p.x for p in points], [p.y for p in points], s=10)
        
        plt.savefig("data/test_remove_points.png")
        assert True == True
        
    def test_generateTriadList(self):
        self.loadData()
        
        self.l = kvector.generateTriadList(self.n, self.ar, self.dec, 30)
        self.k = kvector.Kvector(self.l)
        assert True == True
        #assert str(k) == '2'

    def test_save_load_Kvector(self):
        self.test_generateTriadList()        
        self.k.save()
        a = kvector.load()
        assert str(self.k) == str(a)

    def test_drawKVector(self):
        k = kvector.load()
        k.drawKVector(plt, markersize=0.001)
        plt.savefig("data/k-vector.png", dpi = 1000)
        assert True == True
"""
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