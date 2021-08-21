import numpy as np
import pytest
from star_tracker.pair import Pair,angleCalculator

def test_minor_than():
    p1 = Pair(0,1,2)
    p2 = Pair(0,1,3)
    res = p1 < p2

    assert res == True

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
    assert s == ' 0 --> 1 2,'

def test_append():
    p1 = Pair(0,1,2)
    p2 = Pair(0,2,3)
    p1.append(p2)
    s = str(p1)
    assert s == ' 0 --> 1 2, 0 --> 2 3,'

def test_insert_before():
    p1 = Pair(0,1,3)
    p2 = Pair(0,2,1)
    p1=p1.orderedInsertion(p2)
    s = str(p1)
    assert s == ' 0 --> 2 1, 0 --> 1 3,'

def test_insert_last_position():
    p1 = Pair(0,1,3)
    p2 = Pair(0,2,5)
    p1=p1.orderedInsertion(p2)
    s = str(p1)
    assert s == ' 0 --> 1 3, 0 --> 2 5,'

def test_insert_in_middle_position():
    p1 = Pair(0,1,3)
    p2 = Pair(0,2,5)
    p3 = Pair(1,8,4)
    p1=p1.orderedInsertion(p2)
    p1=p1.orderedInsertion(p3)
    s = str(p1)
    assert s == ' 0 --> 1 3, 1 --> 8 4, 0 --> 2 5,'

def test_ang_calculator():
    to_rad = (np.pi/180)
    theta1 = 60  * to_rad
    phi1 = 0 * to_rad
    theta2 = 30 * to_rad
    phi2 = 0 * to_rad

    ang = angleCalculator(theta1, phi1, theta2, phi2)

    assert ang == pytest.approx(30 * to_rad)