import pandas
from numpy import sin,cos,pi
import matplotlib
try:
    from star_tracker.basic import *
except ImportError:
    from basic import spherical2catersian

def loadRawData(inputfile):
    stars = pandas.read_csv(inputfile)
    
    THETA = stars["theta"]*(pi/180)
    PHI = stars["phi"]*(pi/180)
    MAG = stars["Magnitude visual"]
    NAME = stars["Numero de catalogacao"]
    
    size = stars.shape
    size = size[0]
    theta,phi,mag,name = [],[],[],[]
    for i in range(size):
        theta.append(THETA[i])
        phi.append(PHI[i])
        mag.append(MAG[i])
        name.append(NAME[i])
    return name, theta, phi, mag

def plotCatalog2D(theta,phi, mag, plt,output):
    plt.figure()
    mag = [num/10 for num in mag]
    ax = plt.axes()
    ax.set_facecolor("k")
    plt.scatter(phi,theta, s=mag,c='white')
    plt.title("2-Dimensional Star Catalog")
    plt.xlabel("phi [rad]")
    plt.xlim(0, 2*pi)
    plt.ylabel("theta [rad]")
    plt.ylim(0, pi)
    plt.savefig(output)
    plt.close('all')
    

def plot3D(theta, phi, mag, plt, output):
    x,y,z = spherical2catersian(theta,phi)
    mag = [num /10 for num in mag]
    plt.figure()
    ax = plt.axes(projection ="3d")
    plt.gca().set_facecolor('k')
    ax.set_axis_off()
    # Creating plot
    ax.scatter3D(x, y, z, s = mag, color = "white")
    ax.scatter3D(0, 0, 0, s = 1,color = "red")
        
    #ax.view_init(elev=0, azim=0)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.savefig(output)
    plt.close('all')