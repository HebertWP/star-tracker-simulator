from math import sin,cos

def spherical2catersian(theta,phi):
    if isinstance(theta,list):
        x,y,z = [],[],[]
        for i,j in zip(theta,phi):
            x.append(sin(i)*cos(j))
            y.append(sin(i)*sin(j))
            z.append(cos(i))    
    else:
        x = sin(theta)*cos(phi)
        y = sin(theta)*sin(phi)
        z = cos(theta)
    return x, y, z
