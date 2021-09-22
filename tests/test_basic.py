from star_tracker.modules.basic import *
from numpy import pi
import pytest

def test_spherical2catersian_list():
    x, y, z = spherical2catersian([0],[0])
    assert [x, y, z] == [[1.0], [0.0], [0.0]]

def test_spherical2catersian_num():
    x, y, z = spherical2catersian(0,0)
    assert [x, y, z] == [1.0, 0.0, 0.0]

def test_catersian2spherical_num():
    ar, dec = deg2rad(33),deg2rad(44)
    x,y,z=spherical2catersian(ar,dec)
    dec1, ar1 = catersian2spherical(x,y,z)
    
    assert dec == dec1
    assert ar == ar1

def test_catersian2spherical_list():
    ar = [0, deg2rad(33), deg2rad(90), deg2rad(180), deg2rad(360)]
    dec = [deg2rad(90), deg2rad(45), deg2rad(0), deg2rad(-33), deg2rad(-90)] 
    x,y,z=spherical2catersian(ar[0:4], dec[0:4])
    dec1, ar1 = catersian2spherical(x,y,z)
    
    assert ar[0:4] == pytest.approx(ar1)
    assert dec[0:4] == pytest.approx(dec1)

def test_ang_calculator():
    to_rad = (pi/180)
    theta1 = 60  * to_rad
    phi1 = 0 * to_rad
    theta2 = 30 * to_rad
    phi2 = 0 * to_rad

    ang = angleCalculator([theta1, phi1], [theta2, phi2])

    assert ang == pytest.approx(30 * to_rad)

def test_distanceCalculator():
    ang = angleCalculator([0, 0], [30*pi/180, 0])
    d = distanceCalculator(ang)
    assert d == pytest.approx(0.51, 0.1)

def test_areaCalculator():
    ang1 = angleCalculator([0, 0], [pi, 0])
    ang2 = angleCalculator([0, 0], [pi/2, 0])
    ang3 = angleCalculator([pi, 0], [pi/2, 0])
    a = distanceCalculator(ang1)
    b = distanceCalculator(ang2)
    c = distanceCalculator(ang3)
    A = areaCalculator(a,b,c)
    assert 1 == pytest.approx(A)

def test_momentCalculator():
    ang1 = angleCalculator([0, 0], [pi, 0])
    ang2 = angleCalculator([0, 0], [pi/2, 0])
    ang3 = angleCalculator([pi, 0], [pi/2, 0])
    a = distanceCalculator(ang1)
    b = distanceCalculator(ang2)
    c = distanceCalculator(ang3)
    A = areaCalculator(a,b,c)
    J = momentCalculator(A,a,b,c)
    assert J == pytest.approx(0.22, 0.1)
