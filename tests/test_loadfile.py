from numpy.core.fromnumeric import size
import pandas
import pytest
import star_tracker.loadfile as loadfile
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
    
class TestPlotRawData:
    def loadData(self):
        self.n, self.v, self.ar, self.dec = loadfile.loadCatalog("data/stars.csv")

    def test_loadCatalog(self):
        self.loadData()
        assert size(self.n) == size(self.dec)
    
    def test_plot2D(self):
        self.loadData()
        loadfile.plotCatalog2D(self.ar, self.dec, self.v, plt, "data/Catalog Plot 2D.png")
        assert True == True        
    
    def test_plot3D(self):
        self.loadData()
        ax = loadfile.plot3D(self.ar, self.dec, self.v, plt, "data/Catalog Plot 3D.png")
        assert True == True