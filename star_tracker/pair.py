import numpy as np
class Pair:
    #init
    def __init__(self,first_star_ID,second_star_ID,angle):
        self.first_star_ID = first_star_ID
        self.second_star_ID = second_star_ID
        self.angle = angle
       
    def __len__(self):
        res = 1 
        if hasattr(self, "next"):
            res = res + len(self.next)
        return res

    def __str__(self):
        s = '| %d --> %d %.2f |' % (self.first_star_ID, self.second_star_ID, self.angle)
        return s
    
    def valid(self, ang, st):
        return (ang - st <= self.angle <= ang + st)
    #minor than
    def __lt__(self,other):
        if isinstance(other, Pair):
            return self.angle < other.angle
        return self.angle < other

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
