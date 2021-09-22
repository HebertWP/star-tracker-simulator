from numpy import sin, cos, arccos,sqrt, pi, arccos, arcsin, arctan

def spherical2catersian(ar, dec):
    if isinstance(ar,list):
        x,y,z = [],[],[]
        for i,j in zip(dec, ar):
            x.append(cos(i)*cos(j))
            y.append(cos(i)*sin(j))
            z.append(sin(i))
    else:
        x = cos(dec)*cos(ar)
        y = cos(dec)*sin(ar)
        z = sin(dec)
    return x, y, z

def catersian2spherical(x, y, z):
    if isinstance(x,list):
        ar, dec = [], []
        for i, j, k in zip(x, y, z):
            if j <= 0.001:
                dec.append(arcsin(k))
                ar.append(arccos(i/cos(dec[-1])))
            else:
                ar.append(arctan(j/i))
                dec.append(arcsin(k))
    else:
        if y <= 0.001:
            dec = arcsin(z)
            ar = arccos(x/cos(dec))
        else:
            ar = arctan(y/x)
            dec = arcsin(z)
    return dec, ar

def quaternus_rotation(q,v):
    out =[]
    out.append(v[0]*(q[0]*q[0]+q[1]*q[1]-q[2]*q[2]-q[3]*q[3])+2*v[1]*(q[1]*q[2]-q[0]*q[3])+2*v[2]*(q[0]*q[2]+q[1]*q[3]))
    out.append(2*v[0]*(q[0]*q[3]+q[1]*q[2]) + v[1]*(q[0]*q[0]-q[1]*q[1]+q[2]*q[2]-q[3]*q[3])+2*v[2]*(q[2]*q[3]-q[0]*q[1]))
    out.append(2*v[0]*(q[1]*q[3]-q[0]*q[2]) + 2*v[1]*(q[0]*q[1]+q[2]*q[3]) + v[2]*(q[0]*q[0]-q[1]*q[1]-q[2]*q[2]+q[3]*q[3]))
    return out
    
def deg2rad(ang):
    if isinstance(ang,list):
        out = []
        for i in ang:
            out.append(i*pi/180)    
    else:
        out = ang*pi/180
    return out

def angleCalculator(p1, p2):
    x1,y1,z1 = spherical2catersian(p1[0], p1[1])
    x2,y2,z2 = spherical2catersian(p2[0], p2[1])
    
    ang = arccos(x1*x2 + y1*y2 + z1*z2)
    return ang

def distanceCalculator(ang):
    a = sqrt(2 - 2*cos(ang))
    return a

def distancesSandardDeviationCalculator(ang, dp):
    eq = sin(ang)/sqrt(2-2*cos(ang))
    res = eq*dp 
    return res

def areaCalculator(a,b,c):
    s = (a + b + c)/2
    A = sqrt(s *(s - a)*(s - b)*(s - c))
    return A

def areaSandardDeviationCalculator(a, dp_a, b, dp_b, c, dp_c):
    eq_a = a*(b*b + c*c - a*a) / (2*sqrt((b + c - a)*(a + c - b)*(a + b -c)*(a + b + c)))
    eq_b = b*(a*a + c*c - b*b) / (2*sqrt((b + c - a)*(a + c - b)*(a + b -c)*(a + b + c)))
    eq_c = c*(a*a + b*b - c*c) / (2*sqrt((b + c - a)*(a + c - b)*(a + b -c)*(a + b + c)))
    res = sqrt(pow(eq_a,2)*pow(dp_a,2) + pow(eq_b,2)*pow(dp_b,2)+pow(eq_c,2)*pow(dp_c,2))
    return res

def momentCalculator(A,a,b,c):
    J = A*(a*a + b*b + c*c)/36
    return J

def momentSandardDeviationCalculator(A, dp_A, a, dp_a, b, dp_b, c, dp_c):
    eq_A = 0
    eq_a = (A/18)*a
    eq_b = (A/18)*b
    eq_c = (A/18)*c
    res = sqrt(pow(eq_a,2)*pow(dp_a,2) + pow(eq_b,2)*pow(dp_b,2)+pow(eq_c,2)*pow(dp_c,2))
    return res