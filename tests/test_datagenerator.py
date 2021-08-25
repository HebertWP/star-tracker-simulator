import random

from star_tracker.datagenerator import creteRandomStarData

def test_creteRandomStarData():
    random.seed(10)
    creteRandomStarData("data/stars.csv", 1, 7, 3000)

    assert True == True