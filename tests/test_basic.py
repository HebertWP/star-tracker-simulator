from star_tracker.basic import *
from numpy import pi
import pytest

def test_spherical2catersian_list():
    x, y, z = spherical2catersian([0],[0])
    assert [x, y, z] == [[0.0], [0.0], [1.0]]

def test_spherical2catersian_num():
    x, y, z = spherical2catersian(0,0)
    assert [x, y, z] == [0.0, 0.0, 1.0]

def test_ang_calculator():
    to_rad = (pi/180)
    theta1 = 60  * to_rad
    phi1 = 0 * to_rad
    theta2 = 30 * to_rad
    phi2 = 0 * to_rad

    ang = angleCalculator(theta1, phi1, theta2, phi2)

    assert ang == pytest.approx(30 * to_rad)

def test_distanceCalculator():
    d = distanceCalculator([0,30*pi/180],[0,0])
    assert d == pytest.approx(0.51, 0.1)

def test_areaCalculator():
    A = areaCalculator(theta = [0, pi, pi/2], phi = [0, 0, 0])
    assert 1 == pytest.approx(A)

def test_momentCalculator():
    J = momentCalculator(theta = [0, pi, pi/2], phi = [0, 0, 0])
    assert J == pytest.approx(0.22, 0.1)
