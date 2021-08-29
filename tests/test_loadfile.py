import pytest
from star_tracker.loadfile import *
import matplotlib.pyplot as plt

def test_loadrawdatapair():
    id,theta,phi,mag = loadRawData("data/test_loadRawDataPair.csv")
    assert id == [0,1,3,5], phi(0) == 1
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