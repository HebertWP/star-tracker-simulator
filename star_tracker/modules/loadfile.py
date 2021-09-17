import pandas
import csv
from numpy import sin,cos,pi
import matplotlib
try:
    import sys
    sys.path.append("..")
    import modules.basic as basic
except ImportError:
    import star_tracker.modules.basic

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