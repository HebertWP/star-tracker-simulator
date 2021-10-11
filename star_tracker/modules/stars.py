import pandas
try:
    import modules.basic as basic
except ImportError:
    import star_tracker.modules.basic as basic

class Stars:
    def __init__(self, input_file):
        self._input_file = input_file
        self.loadCatalog()
    
    def loadCatalog(self):
        stars = pandas.read_csv(self._input_file)
    
        DEC = stars["Declinacao (delta)"]
        AR = stars["Ascensao  reta(alpha)"]
        V = stars["Magnitude visual(V)"]
        N = stars["Numero de catalogacao(HIP)"]
    
        size = stars.shape
        size = size[0]
        self._ar, self._dec, self._v, self._n = [],[],[],[]
        for i in range(size):
            self._ar.append(AR[i])
            self._dec.append(DEC[i])
            self._v.append(V[i])
            self._n.append(N[i])
        self._x, self._y, self._z= basic.spherical2catersian(basic.deg2rad(self._ar), basic.deg2rad(self._dec))
    
    def getStarts(self):
        return self._x, self._y, self._z

    def __len__(self):
        return len(self._n)