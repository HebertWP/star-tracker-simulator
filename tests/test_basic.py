from star_tracker.modules.basic import *
from numpy import pi, rad2deg
import pytest

def test_spherical2catersian_list():
    x, y, z = spherical2catersian([0],[0])
    assert [x, y, z] == [[1.0], [0.0], [0.0]]

def test_spherical2catersian_num():
    x, y, z = spherical2catersian(0,0)
    assert [x, y, z] == [1.0, 0.0, 0.0]

def test_catersian2spherical_num():
    for i in range(0,360,1):
        for j in range(-90,90,1):
            ar  = deg2rad(i)
            dec = deg2rad(j)
            x, y, z = spherical2catersian(ar,dec)
            dec1, ar1 = catersian2spherical(x,y,z)
            assert rad2deg(ar)  == pytest.approx(rad2deg(ar1))
            assert rad2deg(dec) == pytest.approx(rad2deg(dec1))

    ar  = deg2rad(300)
    dec = deg2rad(91)
    x, y, z = spherical2catersian(ar,dec)
    dec1, ar1 = catersian2spherical(x,y,z)
    assert [rad2deg(dec)-2* (rad2deg(dec) % 90), (rad2deg(ar)+180) % 360] == [pytest.approx(rad2deg(dec1)), pytest.approx(rad2deg(ar1))]
    
def test_catersian2spherical_list():
    ar, dec = [],[]
    for i in range(0,360,1):
        for j in range(-90,90,1):
            ar.append(deg2rad(i))
            dec.append(deg2rad(j))
    x,y,z=spherical2catersian(deg2rad(ar), deg2rad(dec))
    dec1, ar1 = catersian2spherical(x,y,z)
    
    for i,j,k,l in zip(ar,ar1, dec, dec1):
        assert i == pytest.approx(rad2deg(j))
        assert k == pytest.approx(rad2deg(l))

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