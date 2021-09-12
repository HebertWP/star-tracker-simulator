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

def expandPoints(names,ar, dec, maxAng):
    points = []
    for i in range(len(names)):
        points.append(Point(ar[i], dec[i], {"id":names[i], "dec":dec[i], "ar":ar[i]}))
        if ar[i] > 360 - maxAng :
            if dec[i] < -90 + maxAng:
                points.append(Point(ar[i]-360, dec[i] + 180, {"id":names[i], "dec":dec[i], "ar":ar[i]}))
            elif dec[i] > 90 - maxAng:
                points.append(Point(ar[i]-360, dec[i] - 180, {"id":names[i], "dec":dec[i], "ar":ar[i]}))
            points.append(Point(ar[i] - 360, dec[i],  {"id":names[i], "dec":dec[i], "ar":ar[i]}))
        if ar[i] < maxAng :
            if dec[i] < -90 + maxAng:
                points.append(Point(ar[i]+360, dec[i]+180, {"id":names[i], "dec":dec[i], "ar":ar[i]}))
            elif dec[i]> 90 - maxAng:
                points.append(Point(ar[i]+360, dec[i]-180, {"id":names[i], "dec":dec[i], "ar":ar[i]}))
            points.append(Point(ar[i] + 360, dec[i], {"id":names[i], "dec":dec[i], "ar":ar[i]}))
        if dec[i] > 90 - maxAng:
            points.append(Point(ar[i], dec[i] - 180, {"id":names[i], "dec":dec[i], "ar":ar[i]}))
        if dec[i] < -90+maxAng :
            points.append(Point(ar[i], dec[i] + 180, {"id":names[i], "dec":dec[i], "ar":ar[i]}))
    return points
    
def cretequatTree(maxAng, points):
    width, height = 360 + 2*maxAng , 180 + 2 * maxAng
    domain = Rect(180, 0, width, height)
    qtree = QuadTree(domain,3)
    for point in points:
        qtree.insert(point)
    DPI = 72
    fig = plt.figure(figsize=(700/DPI, 500/DPI), dpi=DPI)
    plt.ylabel("Elevation[deg]")
    plt.xlabel("Right Ascension[deg]")
    qtree.draw(plt)
    original = Rect(180, 0, 360, 180)
    original.draw(plt,c='r')
    plt.scatter([p.x for p in points], [p.y for p in points], s=10)
    plt.savefig("data/aux.png")
    return qtree

def removePoint(qtree : QuadTree, point):
        qtree.remove(point)
        c = []
        for i in range(8):
            c.append(copy.deepcopy(point))
        c[0].y -= 180
        
        c[1].y += 180
        
        c[2].x -= 360
        
        c[3].x += 360
        
        c[4].y -= 180
        c[4].x -= 360
        
        c[5].y -= 180
        c[5].x += 360
        
        c[6].y += 180
        c[6].x += 360
        
        c[7].y += 180
        c[7].x -= 360
        
        for i in c:
            qtree.remove(i)

def triagleCalculator(list, ref:Point, maxAng):
    maxAng = maxAng*pi/180
    nameS1 = ref.payload["id"]
    decS1 = deg2rad(ref.payload["dec"])
    arS1 = deg2rad(ref.payload["ar"])
    kvector = []
    list.remove(ref)
    for i in range(len(list)):
        nameS2 = list[i].payload["id"]
        decS2 = deg2rad(list[i].payload["dec"])
        arS2 = deg2rad(list[i].payload["ar"])
        for j in range(i+1,len(list)):
            nameS3 = list[j].payload["id"]
            decS3 = deg2rad(list[j].payload["dec"])
            arS3 = deg2rad(list[j].payload["ar"])
            ang1 = angleCalculator([arS1, decS1],[arS2, decS2])
            if ang1 <= maxAng:
                ang2 = angleCalculator([arS2, decS2], [arS3, decS3])
                if ang2 <= maxAng:
                    ang3 = angleCalculator([arS3, decS3], [arS1, decS1])
                    if ang3 <= maxAng:
                        a = distanceCalculator(ang1)
                        b = distanceCalculator(ang2)
                        c = distanceCalculator(ang3)
                        A = areaCalculator(a, b, c)
                        J = momentCalculator(A,a,b,c)
                        #if(nameS1 == 54872 and nameS2 == 63125):
                        #    print('p1.ar = {}, p1.dec = {}'.format(arS1, decS1))    
                        #    print('a0 = {}, a1 = {}, a2 = {}'.format(ang1, ang2, ang2))    
                        #    print('A = {}, J = {}, a = {}, b = {}, c = {}'.format(A,J,a,b,c))
                        kvector.append(Triangle([nameS1, nameS2, nameS3],A,J))
    return kvector

def generateTriadList(names, ar, dec, maxAng):
        list = []
        points = expandPoints(names, ar, dec, maxAng)
        qtree = cretequatTree(maxAng,points)
        for i in range(len(names)):
            found_points = []
            region = Rect(ar[i], dec[i], 2*maxAng, 2*maxAng)
            qtree.query(region, found_points)
            p = Point(ar[i], dec[i], {"id":names[i], "dec":dec[i], "ar":ar[i]})
            removePoint(qtree, p)
            list += triagleCalculator(found_points,p,maxAng)
        plt.savefig("data/aux.png")
        mergeSort(list)
        return list

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

class Kvector:

    def __init__(self, list):
        self.list = list 
    
    def __str__(self) -> str:
        s = ""
        for i in self.list:
            s = s + str(i)
        return s

    def __len__(self):
        return len(self.list)
    
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
    
    def drawKVector(self,plt,**kwargs):
        fig = plt.figure()
        x = range(len(self.list))
        y = []
        for i in self.list:
            y.append(i.area)
        plt.scatter(x, y)
    
    def binarySearch(self, area, st, l, r):
        m = int((r + l) / 2)
        if l > r:
            return -1
        
        if self.list[m].valid(area,st):
            return m
        if self.list[m] < area:
            return self.binarySearch(area, st,m+1,r)
        else:
            return self.binarySearch(area, st,l,m-1)

    def search3Stars(self,a,b,c,st):
        A = areaCalculator(a,b,c)
        dp_A = areaSandardDeviationCalculator(a, st, b, st, c, st)
        J = momentCalculator(A,a,b,c)
        dp_J = momentSandardDeviationCalculator(A,dp_A, a,st, b,st, c,st)
        m = self.binarySearch(A, dp_A, 0, len(self) - 1)
        #print('A = {}, J = {}, a = {}, b = {}, c = {}'.format(A,J,a,b,c))
        if m == -1:
            return []
        aux = self.list[self.findMin(A, dp_A, m) : self.findMax(A, dp_A, m)]
        res=[]
        for i in aux:
            if i.validMoment(J,dp_J):
                res.append(i)
        return res

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
    
    def pivot(self,lists):
        for i in lists:
            for j in list(i):
                for k in lists:
                    if not j.isContainedinList(k):
                        i.remove(j)
                        break
                
"""
    def search(self,dist,st):
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
"""