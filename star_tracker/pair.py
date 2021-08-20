class Pair:
    def __init__(self,first_star_ID,second_starID,angle):
        self.first_star_ID=first_star_ID
        self.second_starID=second_starID
        self.angle=angle
    
    #minor than
    def __lt__(self,other):
        return self.angle < other.angle

    #minor equal to
    def __le__(self,other):
        return self.angle <= other.angle

    def __eq__(self, other):
        return self.angle == other.angle
    
    #bigger than
    def __gt__(self, other):
        return self.angle > other.angle

class StarData:
    def __init__(self,theta,phi,angles):
        self.theta=theta
        self.phi=phi
        angles=angles
