import star_tracker.basic as basic
from numpy import pi
import matplotlib.pyplot as plt
import star_tracker.kvector as kvector
import star_tracker.loadfile as loadfile
import star_tracker.quadtree as quadtree
from star_tracker.triangle import *

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
    
    def test_binarySearch(self):
        k = kvector.load()
        l=k.binarySearch(0.11032827368551994, 0.0001, 0, len(k)-1)
        assert l == 62446

    def test_search3Stars(self):
        k = kvector.load()
        n   = [       54872,       63125,      57632]
        ar  = basic.deg2rad([168.52671705, 194.00767051, 177.26615977])
        dec = basic.deg2rad([20.52403384,  38.31824617, 14.57233687])
        a0 = kvector.angleCalculator([ar[0],dec[0]],[ar[1],dec[1]])
        a1 = kvector.angleCalculator([ar[1],dec[1]],[ar[2],dec[2]])
        a2 = kvector.angleCalculator([ar[2],dec[2]],[ar[0],dec[0]])
        a = kvector.distanceCalculator(a0)
        b = kvector.distanceCalculator(a1)
        c = kvector.distanceCalculator(a2)
        st=kvector.distancesSandardDeviationCalculator(a0, 0.05*pi/180)
        m = k.search3Stars(a,b,c, st)
        o = 'len = {},'.format(len(m))
        for i in m:
            o +=str(i) 
        assert o == 'len = 1,| 54872,63125,57632 --> 0.04 0.00 |'
    
    def test_pivot(self):
        k = kvector.load()
        lists = []
        lists.append([
            Triangle([113, 104, 86],3,5),
            Triangle([122, 134, 111],3,5),
            Triangle([172, 154, 175],3,5),
            Triangle([142, 151, 166],3,5)])
        lists.append([
            Triangle([322, 323, 336],3,5), 
            Triangle([148, 151, 142],3,5),
            Triangle([70, 63, 66],3,5),
            Triangle([397, 401, 411],3,5),
            Triangle([456, 457, 467],3,5)])
        lists.append([
            Triangle([339, 330, 371],3,5), 
            Triangle([142, 148, 166],3,5),
            Triangle([49, 57, 59],3,5),
            Triangle([334, 325, 367],3,5),
            Triangle([167, 181, 109],3,5),
            Triangle([300, 287, 322],3,5)])
        lists.append([
            Triangle([81, 73, 92],3,5), 
            Triangle([148, 151, 125],3,5),
            Triangle([151, 148, 166],3,5)])
        
        k.pivot(lists)
        s = ''
        for i in lists:
            for j in i:
                s += str(j)
            s += '----'
        assert s == '| 142,151,166 --> 3.00 5.00 |----| 148,151,142 --> 3.00 5.00 |----| 142,148,166 --> 3.00 5.00 |----| 151,148,166 --> 3.00 5.00 |----'

"""           
    def test_search(self):
        k = kvector.load()
        n   = [       8796,       14135,      17847]
        ar  = [28.27041595, 45.56991279, 57.29054669]
        dec = [29.57939727,  4.08992539, 24.05352412]
        ar = [t*pi/180 for t in ar]
        dec = [p*pi/180 for p in dec]
        ang = []
        for i in range(len(n)):
            ang.append([])
            for j in range(len(n)):
                ang[i].append(kvector.angleCalculator([ar[i],dec[i]],[ar[j],dec[j]]))

        m = k.search(ang, 0.5*pi/180)
        assert m == [649, 20, 22, 32, 124, 204, 1277, 1456, 256, 1199, 1476]
"""