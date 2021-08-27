from math import sin, cos, sqrt

class Triangle:
    def __init__(self, star, area, moment):
        self.star = star
        self.area = area
        self.moment = moment
    
    def __str__(self):
        s = '| %d,%d,%d --> %.2f %.2f |' % (self.star[0], self.star[1], self.star[2], self.area, self.moment)
        return s
    
    def validArea(self, area, sd):
        return (area - sd <= self.area <= area + sd)
    
    def validMoment(self, moment,sd):
        return (moment - sd <= self.moment <= moment + sd)
    
    #minor than
    def __lt__(self,other):
        if isinstance(other, Triangle):
            return self.area < other.area
        return self.area < other
    
    #minor equal to
    def __le__(self,other):
        if isinstance(other, Triangle):
            return self.area <= other.area
        return self.area <= other
    
    #bigger equal to
    def __ge__(self,other):
        if isinstance(other, Triangle):
            return self.area >= other.area
        return self.area >= other

    #bigger than
    def __gt__(self, other):
        if isinstance(other, Triangle):
            return self.area > other.area
        return self.area > other