import random

from star_tracker.datagenerator import generareData

def test_loadRawData():
    random.seed(10)
    generareData("data/stars.csv",1,7,3000)

    assert True == True