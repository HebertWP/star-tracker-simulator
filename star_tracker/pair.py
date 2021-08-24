import numpy as np
class Pair:
    #init
    def __init__(self,first_star_ID,second_starID,angle):
        self.first_star_ID=first_star_ID
        self.second_starID=second_starID
        self.angle=angle
       
    def __len__(self):
        res = 1 
        if hasattr(self, "next"):
            res = res + len(self.next)
        return res

    def __str__(self):
        s = '| %d --> %d %.2f |' % (self.first_star_ID, self.second_starID, self.angle)
        if hasattr(self, "next"):
            s = s + str(self.next) 
        return s
    
    #minor than
    def __lt__(self,other):
        return self.angle < other.angle

    #minor equal to
    def __le__(self,other):
        return self.angle <= other.angle

    #equal to
    def __eq__(self, other):
        return self.angle == other.angle
    
    #bigger equal to
    def __ge__(self,other):
        return self.angle >= other.angle

    #bigger than
    def __gt__(self, other):
        return self.angle > other.angle

def angleCalculator(theta1, phi1, theta2, phi2):
    x1 = np.sin(theta1)*np.cos(phi1)
    x2 = np.sin(theta2)*np.cos(phi2)
    
    y1 = np.sin(theta1)*np.sin(phi1)
    y2 = np.sin(theta2)*np.sin(phi2)
    
    z1 = np.cos(theta1)
    z2 = np.cos(theta2)
    
    ang = np.arccos(x1*x2+y1*y2+z1*z2)
    return ang

def generateData(names,theta,phi,mag,minMag,maxMag,minAng, maxAng):
    res = [Pair(-1,-1,-1)] * int((len(names) * ( len(names) - 1)) / 2)
    aux = 0
    for i in range(len(names) - 1):
        for y in range(i + 1, len(names)):
            if (minMag <= mag[i] and mag[i] <= maxMag 
            and minMag <= mag[y] and mag[y] <= maxMag 
            and minAng <= (theta[i] - theta[y])*(theta[i] - theta[y]) and (theta[i] - theta[y])*(theta[i] - theta[y]) <= maxAng*maxAng 
            and minAng <= (phi[i] - phi[y])*(phi[i] - phi[y]) and (phi[i] - phi[y])*(phi[i] - phi[y]) <= maxAng*maxAng):
                ang = angleCalculator(theta[i], phi[i], theta[y], phi[y])
                if minAng <= ang <= maxAng :
                    res[aux] = Pair(names[i],names[y],ang)
                    aux = aux + 1
    res=res[0:aux]
    return res

def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1
def drawKVector(kvector,plt,**kwargs):
    x = range(len(kvector))
    y = []
    for i in kvector:
        y.append(i.angle)
    plt.scatter(x, y)

def findPossibleCombinations(kvector,ang,var):
    minAngle = ang - var
    minIndex = None
    maxAngle = ang + var
    maxIndex = None
    size = len(kvector)
    for x in range(size):
        if minIndex == None and kvector[x].angle >= minAngle:
            minIndex = x
        if maxIndex == None and kvector[x].angle > maxAngle:
            maxIndex = x - 1
    return minIndex, maxIndex