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
    s = [t.validArea(1,2), t.validArea(5,1)]
    assert s == [False, True]