from star_tracker.loadfile import loadRawData

def test_loadrawdatapair():
    id,theta,phi,mag = loadRawData("data/test_loadRawDataPair.csv")
    assert id == [0,1,3,5], phi(0) == 1