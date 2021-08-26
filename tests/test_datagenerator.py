import random

from star_tracker.datagenerator import creteRandomStarData

def test_creteRandomStarData():
    random.seed(10)
    creteRandomStarData("data/stars.csv", 4, 7, 1500)

    assert True == True