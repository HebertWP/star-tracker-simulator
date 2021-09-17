from numpy.core.fromnumeric import size
import pandas
import pytest
import star_tracker.modules.loadfile as loadfile
from star_tracker.modules.loadfile import Movements
import matplotlib.pyplot as plt

def test_dat2csv():
    loadfile.dat2csv("data/hip_main.dat","data/stars.csv")
    try:
        stars = pandas.read_csv("data/stars.csv")
        assert True == True
    except FileNotFoundError:
        assert True == "File not found."
    except pandas.errors.EmptyDataError:
        assert True == "No data"
    except pandas.errors.ParserError:
        assert True == "Parse error"
    except Exception:
        assert True == "Some other exception"

class TestLoad:
    def loadData(self):
        self.n, self.v, self.ar, self.dec = loadfile.loadCatalog("data/stars.csv")
    
    def loadMovements(self):
        self._m = Movements('data/Movements.csv')
    
    def test_loadCatalog(self):
        self.loadData()
        assert size(self.n) == size(self.dec)
    
    def test_loadMovements(self):
        self.loadMovements()
        assert 2 == len(self._m)
    
    def test_Movements_play(self):
        self.loadMovements()
        assert self._m.playing == False
        self._m.play()
        assert self._m.playing == True
    
    def test_Movements_move(self):
        self.loadMovements()
        self._m.play()
        a = [self._m.move(),self._m.move()]
        b = {'time': 3, 'ar':0, 'dec':0, 'roll':0}
        assert a[0] == b
    
    def test_Movements_stop(self):
        self.loadMovements()
        self._m.play()
        a = [self._m.move(),self._m.move()]
        assert self._m.playing == False
    
    def test_Movements_progress(self):
        self.loadMovements()
        self._m.play()
        assert 0 == self._m.progress
        self._m.move()
        assert 37.5 == self._m.progress
        self._m.move()
        assert 100 == self._m.progress