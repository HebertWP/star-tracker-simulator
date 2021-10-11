import pytest
from star_tracker.modules.stars import Stars

class TestStars:
    def load(self):
        self._stars = Stars("data/stars.csv") 
        
    def test_load_stars(self):
        self.load()
        assert len(self._stars) == 515       