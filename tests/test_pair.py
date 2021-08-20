from star_tracker.star import Pair

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

def test_bigger_than():
    p1 = Pair(0,1,2)
    p2 = Pair(0,1,3)
    res = p1 > p2

    assert res == False