from typing import List, Tuple
import matplotlib.pyplot as plt
import csv
from math import pow,pi

from numpy import generic
from numpy.core.fromnumeric import searchsorted
from star_tracker.triangle import Triangle
import pandas
import importlib
import copy
try:
    from star_tracker.pair import Pair
    from star_tracker.sort import mergeSort
    from star_tracker.basic import *
    from star_tracker.quadtree import *
    from star_tracker.stars import *
except ImportError:
    from pair import Pair
    from sort import mergeSort
    from basic import *
    from quadtree import *
    from stars import *
class Kvector:

    def __init__(self, list):
        self.list = list 
    
    @staticmethod
    def generateKVectorList(names,theta,phi,mag,minMag,maxMag,minAng, maxAng):
        kvector = [Pair(-1,-1,-1)] * int((len(names) * ( len(names) - 1)) / 2)
        aux = 0
        for i in range(len(names) - 1):
            for y in range(i + 1, len(names)):
                if (minMag <= mag[i] <= maxMag 
                and minMag <= mag[y] <= maxMag 
                and minAng*minAng <= (theta[i] - theta[y])*(theta[i] - theta[y]) <= maxAng*maxAng 
                and minAng*minAng <= (phi[i] - phi[y])*(phi[i] - phi[y]) <= maxAng*maxAng):
                    ang = angleCalculator(theta[i], phi[i], theta[y], phi[y])
                    if minAng <= ang <= maxAng :
                        kvector[aux] = Pair(names[i],names[y],ang)
                        aux = aux + 1
        kvector = kvector[0:aux]
        mergeSort(kvector)
        return kvector    
    @staticmethod
    def expandPoints(names,theta,phi,maxAng):
        points = []
        for i in range(len(names)):
            points.append(Point(phi[i], theta[i], [names[i],theta[i],phi[i]]))
            if phi[i] > 2*pi - maxAng :
                if theta[i] < maxAng:
                    points.append(Point(phi[i]-2*pi, theta[i]+pi, [names[i],theta[i],phi[i]]))
                elif theta[i]> pi - maxAng:
                    points.append(Point(phi[i]-2*pi, theta[i]-pi, [names[i],theta[i],phi[i]]))
                points.append(Point(phi[i]-2*pi,theta[i],[names[i],theta[i],phi[i]]))
            if phi[i] < maxAng :
                if theta[i] < maxAng:
                    points.append(Point(phi[i]+2*pi, theta[i]+pi, [names[i],theta[i],phi[i]]))
                elif theta[i]> pi - maxAng:
                    points.append(Point(phi[i]+2*pi, theta[i]-pi, [names[i],theta[i],phi[i]]))
                points.append(Point(phi[i]+2*pi,theta[i],[names[i],theta[i],phi[i]]))
            if theta[i] > pi - maxAng:
                points.append(Point(phi[i], theta[i]-pi, [names[i],theta[i],phi[i]]))
            if theta[i] < maxAng :
                points.append(Point(phi[i], theta[i]+pi, [names[i],theta[i],phi[i]]))
        return points
    @staticmethod
    def removePoint(qtree : QuadTree,point,maxAng):
        qtree.remove(point)
        c = []
        for i in range(8):
            c.append(copy.deepcopy(point))
        c[0].y -= pi
        
        c[1].y += pi
        
        c[2].x -= 2*pi
        
        c[3].x += 2*pi
        
        c[4].y -= pi
        c[4].x -= 2*pi
        
        c[5].y -= pi
        c[5].x += 2*pi
        
        c[6].y += pi
        c[6].x += 2*pi
        
        c[7].y += pi
        c[7].x -= 2*pi
        
        for i in c:
            qtree.remove(i)
    @staticmethod
    def triagleCalculator(list, ref:Point, maxAng):
        #[names[i],theta[i],phi[i]]
        nameS1 = ref.payload[0]
        thetaS1 = ref.payload[1]
        phiS1 = ref.payload[2]
        kvector = []
        if ref in list:
            list.remove(ref)
        for i in range(len(list)):
            nameS2 = list[i].payload[0]
            thetaS2 = list[i].payload[1]
            phiS2 = list[i].payload[2]
            for j in range(i+1,len(list)):
                nameS3 = list[j].payload[0]
                thetaS3 = list[j].payload[1]
                phiS3 = list[j].payload[2]
                ang1 = angleCalculator(thetaS2, phiS2, thetaS3, phiS3)
                if ang1 <= maxAng :
                    ang2 = angleCalculator(thetaS1, phiS1, thetaS3, phiS3)
                    if ang2 <= maxAng:
                        ang3 = angleCalculator(thetaS1, phiS1, thetaS2, phiS2)
                        if ang3 <= maxAng:
                            a = distanceCalculator(ang1)
                            b = distanceCalculator(ang2)
                            c = distanceCalculator(ang3)
                            A = areaCalculator(a, b, c)
                            J = momentCalculator(A,a,b,c)
                            kvector.append(Triangle([nameS1, nameS2, nameS3],A,J))
        return kvector

    @staticmethod
    def generateTriadList(names, theta, phi, maxAng):
        list = []
        width, height = 2*pi + 2*maxAng , pi + 2*maxAng
        domain = Rect(pi, pi/2, width, height)
        qtree = QuadTree(domain,3)
        points = Kvector.expandPoints(names,theta,phi,maxAng)
        for point in points:
            qtree.insert(point)
        DPI = 72
        fig = plt.figure(figsize=(700/DPI, 500/DPI), dpi=DPI)
        plt.ylabel("theta[rad]")
        plt.xlabel("phi[rad]")
        qtree.draw(plt)
        original = Rect(pi,pi/2,2*pi,pi)
        original.draw(plt,c='r')
        plt.scatter([p.x for p in points], [p.y for p in points], s=4)
        for i in range(len(names)):
            found_points = []
            region = Rect(phi[i], theta[i], 2*maxAng, 2*maxAng)
            qtree.query(region, found_points)
            p = Point(phi[i], theta[i],[names[i],theta[i],phi[i]])
            Kvector.removePoint(qtree, p,maxAng)
            list += Kvector.triagleCalculator(found_points,p,maxAng)
        plt.savefig("data/aux.png")
        mergeSort(list)
        return list
    
    def save(self):
        file = open("data/kvector.csv","w")
        fieldnames = ['star_01', 'star_02', 'star_03', 'area', 'moment']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(self)):
            writer.writerow({'star_01': self.list[i].star[0],
                            'star_02': self.list[i].star[1],
                            'star_03': self.list[i].star[2],
                            'area': self.list[i].area,
                            'moment': self.list[i].moment})
        file.close()

    @staticmethod
    def load():
        triangles = pandas.read_csv("data/kvector.csv")
        star_01 = triangles["star_01"]
        star_02 = triangles["star_02"]
        star_03 = triangles["star_03"]
        area = triangles["area"]
        moment = triangles["moment"]
        size = triangles.shape
        size = size[0]
        list = [Triangle([-1,-1,-1],-1,-1)] * size
        for i in range(size):
            list[i] = Triangle([star_01[i], star_02[i], star_03[i],], area[i], moment[i])
        return Kvector(list)

    def drawKVector(self,plt,**kwargs):
        x = range(len(self.list))
        y = []
        for i in self.list:
            y.append(i.area)
        plt.scatter(x, y)

    def binarySearch(self, ang, st, l, r):
        m = int((r + l) / 2)
        if l > r:
            return -1
        
        if self.list[m].valid(ang,st):
            return m
        if self.list[m] < ang:
            return self.binarySearch(ang,st,m+1,r)
        else:
            return self.binarySearch(ang,st,l,m-1)

    def findMin(self,ang,st,m):
        i = m
        while i > 0 and self.list[i].valid(ang,st):
            i -= 1
        return i
    
    def findMax(self,area,st,m):
        i = m
        while i < len(self.list) and self.list[i].valid(area,st):
            i += 1
        return i

    def search(self,ang,st):
        n = len(ang[0])
        stars = [[] for i in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    possibilities = self.search3Stars([ang[i][j],ang[j][k],ang[k][i]],st)
                    stars[i].append(possibilities) 
                    stars[j].append(possibilities) 
                    stars[k].append(possibilities) 
        
        for i in range(len(stars)):
            for j in range(len(stars[i])):#how many possibilities lists
                stars[i][j] = Triangle.triangleListToNumList(stars[i][j])
        res = []
        for i in range(len(stars)):
            res.append(self.selectStar(stars[i]))
        return res
    
    def selectStar(self,lists):
        res = -1
        for i in range(len(lists[0])):
            aux = 0
            for j in range(1,len(lists)):
                if lists[0][i] in lists[j]:
                    aux += 1
            if aux == len(lists) - 1:
                if res != -1:
                    return -2
                res = lists[0][i]
        return res

    def search3Stars(self,ang,st):
        a = distanceCalculator(ang[0])
        dp_a = distancesSandardDeviationCalculator(ang[0],st)
        b = distanceCalculator(ang[1])
        dp_b = distancesSandardDeviationCalculator(ang[1],st)
        c = distanceCalculator(ang[2])
        dp_c = distancesSandardDeviationCalculator(ang[2],st)
        A = areaCalculator(a,b,c)
        dp_A = areaSandardDeviationCalculator(a,dp_a,b,dp_b,c,dp_c)
        J = momentCalculator(A,a,b,c)
        dp_J = momentSandardDeviationCalculator(A,dp_A,a,dp_a,b,dp_b,c,dp_c)
        m = self.binarySearch(A, dp_A, 0, len(self) - 1)
        if m == -1:
            return []
        aux = self.list[self.findMin(A, dp_A, m) : self.findMax(A, dp_A, m)]
        res=[]
        for i in aux:
            if i.validMoment(J,dp_J):
                res.append(i)
        return res
    def __str__(self) -> str:
        s = ""
        for i in self.list:
            s = s + str(i)
        return s

    def __len__(self):
        return len(self.list)