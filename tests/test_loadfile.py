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
    
"""
def test_loadrawdatapair():
    id,theta,phi,mag = loadRawData("data/test_loadRawDataPair.csv")
    assert id == [0,1,3,5], phi(0) == 1

    assert True == True
class TestPlotRawData:
    def loadData(self):
        self.id, self.theta, self.phi, self.mag = loadRawData("data/stars.csv")
        
    def test_plot3D(self):
        self.loadData()
        ax = plot3D(self.theta,self.phi,self.mag,plt,"data/Catalog Plot 3D.png")
        assert True == True

    def test_plot2D(self):
        self.loadData()
        plotCatalog2D(self.theta, self.phi,self.mag,plt,"data/Catalog Plot 2D.png")
        assert True == True
"""