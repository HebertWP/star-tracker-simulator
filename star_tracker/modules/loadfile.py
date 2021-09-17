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

class Movements():
    def __init__(self,file_name) -> None:
        self.load(file_name)
        self._playing = 0
        self._current = 0

    def load(self, file_name):
        self._file_name = file_name
        positions = pandas.read_csv(self._file_name)
        time = positions["time"]
        roll = positions["roll"]
        dec = positions["dec"]
        ar = positions["ar"]
        self._positions = []
        for t,r,d,a in zip(time,roll,dec,ar):
            self._positions.append({'time': t, 'roll': r, 'dec': d, 'ar': a})

    def play(self):
        self._playing = True
        self._current = 0
    
    def stop(self):
        self._playing = False
        self._current = 0

    def move(self):
        out = self._positions[self._current]
        self._current += 1
        self._playing = False if self._current >= len(self._positions) else True
        return out
    
    @property
    def progress(self):
        pass_time = 0
        for i in self._positions[0:self._current]:
            pass_time += i["time"]
        total_time = 0
        for i in self._positions:
            total_time += i["time"]
        ret=pass_time/total_time
        return ret*100
        
    @property
    def playing(self):
        return self._playing
    
    def __len__(self):
        return len(self._positions)