import json
import numpy as np
try:
    from modules.basic import *
    from modules.line import *
    from modules.stars import * 
except ImportError:
    from star_tracker.modules.basic import *
    from star_tracker.modules.line import *
    from star_tracker.modules.stars import *

class Camera():
    def __init__(self):
        self._configured = False
        self._axles = {'z':[-1,0,0],'y':[0,0,1],'x':[0,-1,0]}
        self.rotate_dots([1,0,0,0])
        
        self._ar = 0
        self._dec = 0
        self._roll = 0 
        self.stars = Stars()
        
    @property
    def config(self):
        return self._input_file

    @config.setter 
    def config(self, input_file):
        self._configured = True
        self._input_file = input_file
        f = open(self._input_file)
        data = json.load(f)
        self._view_ang = deg2rad(data['ang'])/2
        
        self._dots = []
        self._dots.append(spherical2catersian( 1*self._view_ang, self._view_ang))
        self._dots.append(spherical2catersian(-1*self._view_ang, self._view_ang))
        self._dots.append(spherical2catersian(-1*self._view_ang, -1*self._view_ang))
        self._dots.append(spherical2catersian(1*self._view_ang, -1*self._view_ang))
    
        aux = self._dots
        self._position_dict = {'x' : [aux[0][0], aux[1][0], aux[2][0], aux[3][0]], 'y': [aux[0][1], aux[1][1], aux[2][1], aux[3][1]],'z': [aux[0][2], aux[1][2], aux[2][2], aux[3][2]]}
    
    @property
    def stars(self) -> Stars:
        return self._stars
    
    @stars.setter
    def stars(self, value):
        self._stars = value

    @property
    def roll(self):
        return self._roll
    
    @roll.setter
    def roll(self, value):
        diff = value - self._roll
        self._roll = value
        x,y,z = spherical2catersian(self._ar, self._dec)
        q = [cos(diff/2), sin(diff/2)*x, sin(diff/2)*y, sin(diff/2)*z]
        self.rotate_axles(q)
        self.rotate_dots(q)
        #q = [q[0], -q[1], -q[2], -q[3]]
        #self.stars.rotate(q)
        
    @property
    def dec(self):
        return self._dec
    
    @dec.setter
    def dec(self, value):
        diff = value - self._dec
        self._dec = value
        x,y,z = spherical2catersian(self._ar-pi/2,0)
        q=[cos(diff/2), x*sin(diff/2), y*sin(diff/2), z*sin(diff/2)]
        self.rotate_axles(q)
        self.rotate_dots(q)
        q = [q[0], -q[1], -q[2], -q[3]]
        self.stars.rotate(q)
        
    @property
    def ar(self):
        return self._ar
    
    @ar.setter
    def ar(self, value):
        diff = value - self._ar
        self._ar = value
        q=[cos(diff/2),0,0,sin(diff/2)]
        self.rotate_axles(q)
        self.rotate_dots(q)
        q = [q[0], -q[1], -q[2], -q[3]]
        self.stars.rotate(q)
        
    def rotate_axles(self,q):
        self._axles['z'] = quaternus_rotation(q,self._axles['z'])
        self._axles['y'] = quaternus_rotation(q,self._axles['y'])
        self._axles['x'] = quaternus_rotation(q,self._axles['x'])

    def rotate_dots(self, q):
        if not self._configured:
            return
        self._dots[0] = quaternus_rotation(q,self._dots[0])
        self._dots[1] = quaternus_rotation(q,self._dots[1])
        self._dots[2] = quaternus_rotation(q,self._dots[2])
        self._dots[3] = quaternus_rotation(q,self._dots[3])

        aux = self._dots
        self._position_dict = {'x' : [aux[0][0], aux[1][0], aux[2][0], aux[3][0]], 'y': [aux[0][1], aux[1][1], aux[2][1], aux[3][1]],'z': [aux[0][2], aux[1][2], aux[2][2], aux[3][2]]}
        self.position_dict_spherical

    @property
    def dots(self):
        return self._dots
    
    @property
    def position_dict(self) -> dict:
        return self._position_dict

    @property
    def position_dict_spherical(self) -> dict:
        x = []
        for i in range(4):
            x.append({'x':self.position_dict['x'][i], 'y':self.position_dict['y'][i], 'z':self.position_dict['z'][i]})
        line = []
        line.append(Line(x[0],x[1]))
        line.append(Line(x[2],x[1]))
        line.append(Line(x[3],x[2]))
        line.append(Line(x[0],x[3]))
        out = {"ar":[],"dec":[]}
        for i in range(0,4):
            out['ar'].append([])
            out['dec'].append([])
            for j in np.linspace(0,1,1001):
                dot = line[i].get_dot(j)
                dec, ar = catersian2spherical(dot['x'], dot['y'], dot['z'])
                out['ar'][i].append(ar)
                out['dec'][i].append(dec)
        return out
    
    @property
    def coordinates(self):
        return self._axles