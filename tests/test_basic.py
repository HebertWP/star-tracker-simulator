from star_tracker.modules.basic import *
from numpy import pi
import pytest

def test_spherical2catersian_list():
    x, y, z = spherical2catersian([0],[0])
    assert [x, y, z] == [[1.0], [0.0], [0.0]]

def test_spherical2catersian_num():
    x, y, z = spherical2catersian(0,0)
    assert [x, y, z] == [1.0, 0.0, 0.0]
def test_generate_rotation_matrix():
    m = generate_rotation_matrix(0,0,0)
    assert m[0][0] == m[1][1] == m[2][2] == 1

def test_euler2quartenus():
    m = [[0,-1, 0],
         [1, 0, 0],
         [0, 0, 1]]
    q=euler2quartenus(m)
    assert q == pytest.approx([0.70,0,0,0.70],0.1)

def test_calculate_quaternion_conjugate():
    q=[0,1,1,1]
    a=calculate_quaternion_conjugate(q)
    assert a == [0,-1,-1,-1]

def test_quaternus_rotation():
    m = [[0,-1, 0],
         [1, 0, 0],
         [0, 0, 1]]
    q=euler2quartenus(m)
    l=quaternus_rotation(q,[1,0,0])
    assert l == pytest.approx([0,1,0])

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
