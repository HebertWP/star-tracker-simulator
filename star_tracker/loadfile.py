import pandas
import numpy as np

def loadRawData(inputfile):
    stars = pandas.read_csv(inputfile)
    
    THETA = stars["theta"]*(np.pi/180)
    PHI = stars["phi"]*(np.pi/180)
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