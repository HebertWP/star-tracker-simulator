from star_tracker.modules.camera import Camera
from star_tracker.modules.basic import *

class TestCamera():
    def load(self):
        self._camera = Camera("data/camera.json")
    
    def test_load_camera(self):
        self.load()
        aux=self._camera.dots
        assert aux[0][0] == aux[1][0] == aux[2][0] == aux[3][0]
    
    def test_rotation(self):
        self.load()
        ang = deg2rad(180)
        self._camera.ar = ang
        self._camera.dec = ang
        self._camera.roll = ang
        aux=self._camera.dots
        ang = deg2rad(540)
        self._camera.ar = ang
        self._camera.dec = ang
        self._camera.roll = ang
        aux1=self._camera.dots

        assert aux == aux1
    
    def test_position_dict(self):
        self.load()
        
        ang = deg2rad(180)
        self._camera.ar = ang
        self._camera.dec = ang
        self._camera.roll = ang
        aux = self._camera.position_dict
        ang = deg2rad(540)
        self._camera.ar = ang
        self._camera.dec = ang
        self._camera.roll = ang
        aux1 = self._camera.position_dict

        assert aux == aux1
    
    def test_position_dict_spherical(self):
        self.load()
        
        aux = self._camera.position_dict_spherical
        print(aux)
        assert True == False
        