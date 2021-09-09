from star_tracker.triangle import Triangle
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