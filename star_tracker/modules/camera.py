import json
try:
    from basic import *
except ImportError:
    from star_tracker.modules.basic import *

class Camera():
    def __init__(self,input_file):
        self._input_file = input_file
        self.load()
        self.rotate_dots(0,0,0)
    
    def load(self):
        try:
            f = open(self._input_file)
            data = json.load(f)
            self._view_ang = deg2rad(data['ang'])/2
        except FileNotFoundError:
            return

    def rotate_dots(self, roll, dec, ar):
        m=generate_rotation_matrix(roll,ar,dec)
        q=euler2quartenus(m)
        self._dots = []
        self._dots.append(spherical2catersian( 1*self._view_ang, self._view_ang))
        self._dots.append(spherical2catersian(-1*self._view_ang, self._view_ang))
        self._dots.append(spherical2catersian( 1*self._view_ang, -1*self._view_ang))
        self._dots.append(spherical2catersian(-1*self._view_ang, -1*self._view_ang))
        
        self._dots[0] = quaternus_rotation(q,self._dots[0])
        self._dots[1] = quaternus_rotation(q,self._dots[1])
        self._dots[2] = quaternus_rotation(q,self._dots[2])
        self._dots[3] = quaternus_rotation(q,self._dots[3])
    
    @property
    def dots(self):
        return self._dots