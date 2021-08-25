import csv
import pandas
import importlib
try:
    from star_tracker.pair import Pair, angleCalculator
    from star_tracker.sort import mergeSort
except ImportError:
    from pair import Pair, angleCalculator
    from sort import mergeSort

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

    def save(self):
        file = open("data/kvector.csv","w")
        fieldnames = ['star_01', 'star_02', 'ang']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(self)):
            writer.writerow({'star_01': self.list[i].first_star_ID, 'star_02':self.list[i].second_starID, 'ang':self.list[i].angle})
        file.close()

    @staticmethod
    def load():
        pars = pandas.read_csv("data/kvector.csv")
    
        star_01 = pars["star_01"]
        star_02 = pars["star_02"]
        ang = pars["ang"]
        
        size = pars.shape
        size = size[0]
        list = [Pair(-1,-1,-1)] * size
        for i in range(size):
            list[i]=Pair(star_01[i],star_02[i],ang[i])
        return Kvector(list)

    @staticmethod
    def Pivoting(list_01,list_02):
        res_01 = [Pair(-1,-1,-1)] * len(list_01)
        res_02 = [Pair(-1,-1,-1)] * len(list_02)
        k = 0
        for i in range(len(list_01)):
            for j in range(len(list_02)):
                if ( list_01[i].first_star_ID == list_02[j].first_star_ID ) or ( list_01[i].first_star_ID == list_02[j].second_star_ID ) or ( list_01[i].second_star_ID == list_02[j].first_star_ID ) or ( list_01[i].second_star_ID == list_02[j].second_star_ID ):
                    res_01[k]=list_01[i]
                    k += 1
                    break
        res_01=res_01[0:k]
        k =0 
        for i in range(len(list_02)):
            for j in range(len(list_01)):
                if ( list_02[i].first_star_ID == list_01[j].first_star_ID ) or ( list_02[i].first_star_ID == list_01[j].second_star_ID ) or ( list_02[i].second_star_ID == list_01[j].first_star_ID ) or ( list_02[i].second_star_ID == list_01[j].second_star_ID ):
                    res_02[k]=list_02[i]
                    k += 1
                    break
        res_02=res_02[0:k]
        return [res_01,res_02]
    
    def drawKVector(self,plt,**kwargs):
        x = range(len(self.list))
        y = []
        for i in self.list:
            y.append(i.angle)
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
    
    def findMax(self,ang,st,m):
        i = m
        while i < len(self.list) and self.list[i].valid(ang,st):
            i += 1
        return i
    
    def search(self,ang,st):
        m = self.binarySearch(ang, st, 0, len(self) - 1)
        if m == -1:
            return []
        return  self.list[self.findMin(ang, st, m) : self.findMax(ang, st, m)]

    def __str__(self) -> str:
        s = ""
        for i in self.list:
            s = s + str(i)
        return s

    def __len__(self):
        return len(self.list)