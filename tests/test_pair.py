import numpy as np
import pytest
import matplotlib.pyplot as plt
from matplotlib import gridspec

from star_tracker.pair import Pair,angleCalculator,generateData,pair2list,drawKVector,findPossibleCombinations
from star_tracker.loadfile import loadRawData

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
    assert s == ' 0 --> 1 2.00,'

def test_append():
    p1 = Pair(0,1,2)
    p2 = Pair(0,2,3)
    p1.append(p2)
    s = str(p1)
    assert s == ' 0 --> 1 2.00, 0 --> 2 3.00,'

def test_insert_before():
    p1 = Pair(0,1,3)
    p2 = Pair(0,2,1)
    p1=p1.orderedInsertion(p2)
    s = str(p1)
    assert s == ' 0 --> 2 1.00, 0 --> 1 3.00,'

def test_insert_last_position():
    p1 = Pair(0,1,3)
    p2 = Pair(0,2,5)
    p1=p1.orderedInsertion(p2)
    s = str(p1)
    assert s == ' 0 --> 1 3.00, 0 --> 2 5.00,'

def test_insert_in_middle_position():
    p1 = Pair(0,1,3)
    p2 = Pair(0,2,5)
    p3 = Pair(1,8,4)
    p1=p1.orderedInsertion(p2)
    p1=p1.orderedInsertion(p3)
    s = str(p1)
    assert s == ' 0 --> 1 3.00, 1 --> 8 4.00, 0 --> 2 5.00,'

def test_ang_calculator():
    to_rad = (np.pi/180)
    theta1 = 60  * to_rad
    phi1 = 0 * to_rad
    theta2 = 30 * to_rad
    phi2 = 0 * to_rad

    ang = angleCalculator(theta1, phi1, theta2, phi2)

    assert ang == pytest.approx(30 * to_rad)

def test_data_generator():
    id,theta,phi,mag = loadRawData("data/test_data_generator.csv")
    p = generateData(id,theta,phi,mag,3,6)
    s = str(p)
    assert s == ' 0 --> 1 0.35, 0 --> 3 0.52, 1 --> 3 0.87,'

def test_len():
    p1 = Pair(0,1,3)
    p2 = Pair(0,2,5)
    p3 = Pair(1,8,4)
    p1 = p1.orderedInsertion(p2)
    p1 = p1.orderedInsertion(p3)
    assert len(p1) == 3

def test_pair2list():
    p1 = Pair(0,1,3)
    p2 = Pair(0,2,5)
    p3 = Pair(1,8,4)
    p1=p1.orderedInsertion(p2)
    p1=p1.orderedInsertion(p3)
    res = pair2list(p1)
    a = []
    for i in res:
        a.append(i.second_starID)
    assert a == [1,8,2]
    
def test_drawKVector():
    p1 = Pair(0,1,3)
    p2 = Pair(0,2,5)
    p3 = Pair(1,8,4)
    p1=p1.orderedInsertion(p2)
    p1=p1.orderedInsertion(p3)
    res = pair2list(p1)
    
    drawKVector(res,plt)
    plt.savefig("data/kvector.png")
    assert True == True

def test_findPossibleCombinations_single_output():
    p1 = Pair(0,1,3)
    p2 = Pair(1,2,4)
    p3 = Pair(3,4,5)
    p4 = Pair(4,5,6)
    p5 = Pair(4,5,7)
    p1=p1.orderedInsertion(p2)
    p1=p1.orderedInsertion(p3)
    p1=p1.orderedInsertion(p4)
    p1=p1.orderedInsertion(p5)
    res = pair2list(p1)

    min,max = findPossibleCombinations(res,5,0.5)

    assert [min,max] == [2,2]

def test_findPossibleCombinations_multiples_output():
    p1 = Pair(0,1,3)
    p2 = Pair(1,2,4)
    p3 = Pair(3,4,5)
    p4 = Pair(4,5,6)
    p5 = Pair(4,5,7)
    p1=p1.orderedInsertion(p2)
    p1=p1.orderedInsertion(p3)
    p1=p1.orderedInsertion(p4)
    p1=p1.orderedInsertion(p5)
    res = pair2list(p1)

    min,max = findPossibleCombinations(res,5,1)

    assert [min,max] == [1,3]
