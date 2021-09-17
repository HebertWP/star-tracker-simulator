from star_tracker.modules.triangle import Triangle
from numpy import pi
import pytest

def test_print():
    t = Triangle([0,0,0],3,5)
    p = str(t)
    assert p == '| 0,0,0 --> 3.00 5.00 |'

def test_validArea():
    t = Triangle([0,0,0],3,5)
    s = [t.validArea(1,2), t.validArea(1,1)]
    assert s == [True, False]

def test_validMoment():
    t = Triangle([0,0,0],3,5)
    s = [t.validMoment(1,2), t.validMoment(5,1)]
    assert s == [False, True]

def test_isContained():
    t1 = Triangle([142, 151, 166],3,5)
    t2 = Triangle([148, 151, 142],3,5)
    t3 = Triangle([ 70,  63,  66],3,5)
    assert True == t1.isContained(t2)
    assert False == t1.isContained(t3)
    assert True == t1.isContained(t1)
    
def test_isContainedinList():
    l1 = [
        Triangle([113, 104, 86],3,5),
        Triangle([122, 134, 111],3,5),
        Triangle([172, 154, 175],3,5),
        Triangle([142, 151, 166],3,5)]
    l2 = [
        Triangle([322, 323, 336],3,5), 
        Triangle([148, 151, 142],3,5),
        Triangle([70, 63, 66],3,5),
        Triangle([397, 401, 411],3,5),
        Triangle([456, 457, 467],3,5)
    ]

    assert False == l1[0].isContainedinList(l2)
    assert False == l1[1].isContainedinList(l2)
    assert False == l1[2].isContainedinList(l2)
    assert True == l1[3].isContainedinList(l2)
    assert True == l1[3].isContainedinList(l1)