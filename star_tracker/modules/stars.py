import pandas
import os
import numpy as np

try:
    from modules.basic import *
    from modules.canvas_2D import *
    from modules.canvas_3D import *
except ImportError:
    from star_tracker.modules.basic import *
    from star_tracker.modules.canvas_2D import *
    from star_tracker.modules.canvas_3D import *

class Stars:
    def __init__(self):
        self._x, self._y, self._z, self._ar, self._dec, self._v = [], [], [], [], [], []
        self._configured = False
        self._show = True
        self._input_file = ''
    
    def load_catalog(self, input_file):
        if input_file == '':
            return
        self._input_file = input_file
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
        self._x, self._y, self._z = spherical2catersian(deg2rad(self._ar), deg2rad(self._dec))
        self._configured = True

    @property
    def input_file(self):
        return self._input_file
    
    def getStarts(self):
        return self._x, self._y, self._z

    def getDict(self):
        return {'x': self._x, 'y': self._y, 'z': self._z, 'ar': self._ar, 'dec': self._dec, 'v': self._v}
    
    def rotate(self,q):
        for i in range(len(self._x)):
            self._x[i], self._y[i], self._z[i] = quaternus_rotation(q,[self._x[i], self._y[i], self._z[i]])
            self._dec[i], self._ar[i] = catersian2spherical(self._x[i], self._y[i], self._z[i])

    @property
    def show(self):
        return self._show
    @show.setter
    def show(self, value):
        self._show = value
    
    def __len__(self):
        return len(self._n)