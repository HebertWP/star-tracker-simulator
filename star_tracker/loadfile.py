import pandas
import csv
from numpy import sin,cos,pi
import matplotlib
try:
    from star_tracker.basic import *
except ImportError:
    from basic import spherical2catersian

def dat2csv(inputfile, outputfile):
    input = open(inputfile,"r")
    output = open(outputfile,"w")
    fieldnames = ['Numero de catalogacao(HIP)', 'Ascensao  reta(alpha)', 'Declinacao (delta)', 'Magnitude visual(V)']
    writer = csv.DictWriter(output, fieldnames = fieldnames)
    writer.writeheader()
    Lines = input.readlines()
    for line in Lines:
        try:
            N = int(line[2:14])
            V = float(line[41:46])
            AR = float(line[51:63])
            DEC = float(line[64:76])
            if(V < 4):
                writer.writerow({'Numero de catalogacao(HIP)':N, 'Ascensao  reta(alpha)':AR, 'Declinacao (delta)': DEC,'Magnitude visual(V)':V})
        except ValueError:
            pass

def loadCatalog(inputfile):
    stars = pandas.read_csv(inputfile)
    
    DEC = stars["Declinacao (delta)"]
    AR = stars["Ascensao  reta(alpha)"]
    V = stars["Magnitude visual(V)"]
    N = stars["Numero de catalogacao(HIP)"]
    
    size = stars.shape
    size = size[0]
    ar,dec,v,n = [],[],[],[]
    for i in range(size):
        ar.append(AR[i])
        dec.append(DEC[i])
        v.append(V[i])
        n.append(N[i])
    return n, v, ar, dec

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