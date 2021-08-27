from numpy import sin, cos, arccos,sqrt

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

def angleCalculator(theta1, phi1, theta2, phi2):
    x1 = sin(theta1)*cos(phi1)
    x2 = sin(theta2)*cos(phi2)
    
    y1 = sin(theta1)*sin(phi1)
    y2 = sin(theta2)*sin(phi2)
    
    z1 = cos(theta1)
    z2 = cos(theta2)
    
    ang = arccos(x1*x2 + y1*y2 + z1*z2)
    return ang

def distanceCalculator(theta,phi):
    ang = angleCalculator(theta[0], phi[0], theta[1], phi[1])
    a = sqrt(2 - 2*cos(ang))
    return a

def areaCalculator(theta, phi):
    a = distanceCalculator(theta[0:2],phi[0:2])
    b = distanceCalculator([theta[0],theta[2]], [phi[0], phi[2]])
    c = distanceCalculator(theta[1:3],phi[1:3])
    s = (a + b + c)/2
    A = sqrt(s *(s - a)*(s - b)*(s - c))
    return A

def momentCalculator(theta, phi):
    a = distanceCalculator(theta[0:2],phi[0:2])
    b = distanceCalculator([theta[0],theta[2]], [phi[0], phi[2]])
    c = distanceCalculator(theta[1:3],phi[1:3])
    A = areaCalculator(theta,phi)
    J = A*(a*a + b*b + c*c)/36
    return J