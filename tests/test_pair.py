import numpy as np
import pytest
import matplotlib.pyplot as plt
from matplotlib import gridspec

from star_tracker.pair import Pair,angleCalculator

def test_minor_than():
    p1 = Pair(0,1,2)
    p2 = Pair(0,1,3)
    res = [p1 < p2, p1 < 3]
    
    assert res == [True, True]

def test_minor_equal_than():
    p1 = Pair(0,1,2)
    p2 = Pair(0,1,3)
    res = p1 <= p2

    assert res == True

def test_equal_to():
    p1 = Pair(0,1,2)
    p2 = Pair(0,1,3)
    res = p1 == p2

    assert res == False

def test_equal_bigger_to():
    p1 = Pair(0,1,2)
    p2 = Pair(0,1,3)
    res = p1 >= p2

    assert res == False

def test_bigger_than():
    p1 = Pair(0,1,2)
    p2 = Pair(0,1,3)
    res = p1 > p2

    assert res == False

def test_print():
    p = Pair(0,1,2)
    s = str(p)
    assert s == '| 0 --> 1 2.00 |'

def test_ang_calculator():
    to_rad = (np.pi/180)
    theta1 = 60  * to_rad
    phi1 = 0 * to_rad
    theta2 = 30 * to_rad
    phi2 = 0 * to_rad

    ang = angleCalculator(theta1, phi1, theta2, phi2)

    assert ang == pytest.approx(30 * to_rad)

def test_valid():
    p1 = Pair(0,1,2)
    p2 = Pair(0,1,3)
    p3 = Pair(0,1,3.5)
    s = [p1.valid(2.5, 0.5),p2.valid(2.5, 0.5),p3.valid(2.5, 0.5)]

    assert s == [True, True, False]
