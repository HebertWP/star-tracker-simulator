class Pair:
    #init
    def __init__(self,first_star_ID,second_starID,angle):
        self.first_star_ID=first_star_ID
        self.second_starID=second_starID
        self.angle=angle
    
    def append(self,next):
        if hasattr(self, "next") :
            next.append(self.next)
        self.next=next

    def orderedInsertion(self,element):
        if element < self:
            element.next = self
            return element
        if hasattr(self, "next"):
            self.next=self.next.orderedInsertion(element)
        else :
            self.next=element
        return self
        
    def __str__(self):
        s = ' %d --> %d %d,' % (self.first_star_ID, self.second_starID, self.angle)
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

class StarData:
    def __init__(self,theta,phi,angles):
        self.theta=theta
        self.phi=phi
        angles=angles
