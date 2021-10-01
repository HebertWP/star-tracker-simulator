import json
try:
    from modules.basic import *
except ImportError:
    from star_tracker.modules.basic import *

class Camera():
    def __init__(self,input_file):
        self._input_file = input_file
        self.load()
        self._dots = []
        self._dots.append(spherical2catersian( 1*self._view_ang, self._view_ang))
        self._dots.append(spherical2catersian(-1*self._view_ang, self._view_ang))
        self._dots.append(spherical2catersian(-1*self._view_ang, -1*self._view_ang))
        self._dots.append(spherical2catersian(1*self._view_ang, -1*self._view_ang))
        self._ar = 0
        self._dec = 0
        self._roll = 0 
        self.rotate_dots([1,0,0,0])
        
    def load(self):
        f = open(self._input_file)
        data = json.load(f)
        self._view_ang = deg2rad(data['ang'])/2

    @property
    def roll(self):
        return self._roll
    
    @roll.setter
    def roll(self, value):
        diff = value - self._roll
        self._roll = value
        x,y,z = spherical2catersian(self._ar, self._dec)
        self.rotate_dots([cos(diff/2), sin(diff/2)*x, sin(diff/2)*y, sin(diff/2)*z])
    
    @property
    def dec(self):
        return self._dec
    
    @dec.setter
    def dec(self, value):
        diff = value - self._dec
        self._dec = value
        x,y,z = spherical2catersian(self._ar-pi/2,0)
        q=[cos(diff/2), x*sin(diff/2), y*sin(diff/2), z*sin(diff/2)]
        self.rotate_dots(q)

    @property
    def ar(self):
        return self._ar
    
    @ar.setter
    def ar(self, value):
        diff = value - self._ar
        self._ar = value
        q=[cos(diff/2),0,0,sin(diff/2)]
        self.rotate_dots(q)

    def rotate_dots(self, q):
        
        self._dots[0] = quaternus_rotation(q,self._dots[0])
        self._dots[1] = quaternus_rotation(q,self._dots[1])
        self._dots[2] = quaternus_rotation(q,self._dots[2])
        self._dots[3] = quaternus_rotation(q,self._dots[3])

        aux = self._dots
        self._position_dict = {'x' : [aux[0][0], aux[1][0], aux[2][0], aux[3][0]], 'y': [aux[0][1], aux[1][1], aux[2][1], aux[3][1]],'z': [aux[0][2], aux[1][2], aux[2][2], aux[3][2]]}
    
    @property
    def dots(self):
        return self._dots
    
    @property
    def position_dict(self) -> dict:
        return self._position_dict

    @property
    def position_dict_spherical(self) -> dict:
        dec, ar = catersian2spherical(self.position_dict['x'],self.position_dict['y'],self.position_dict['z'])
        out = {'dec':dec,'ar':ar}
        return out
    
    @property
    def coordinates(self):
        out = {}
        x, y, z = spherical2catersian(self._ar, self._dec)
        z_axle = [-x, -y, -z] 
        out['z'] = [ z_axle[0], z_axle[1], z_axle[2]]

        x,y,z = spherical2catersian(self._ar-pi/2, self._dec)
        
        q = [cos(self._roll/2), sin(self._roll/2)*-z_axle[0], sin(self._roll/2)*-z_axle[1], sin(self._roll/2)*-z_axle[2]]
        x,y,z=quaternus_rotation(q, [x,y,z])
    
        self._roll
        out['x'] = [ x, y, z]

        x,y,z = spherical2catersian(self._ar, self._dec+pi/2)
        
        q = [cos(self._roll/2), sin(self._roll/2)*-z_axle[0], sin(self._roll/2)*-z_axle[1], sin(self._roll/2)*-z_axle[2]]
        x,y,z=quaternus_rotation(q, [x,y,z])
    
        self._roll
        out['y'] = [ x, y, z]

        return out