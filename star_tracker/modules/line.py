from dataclasses import dataclass

class Line:
    def __init__(self, dot_int, dot_end):
        self._dot_int = dot_int
        self._dot_end = dot_end
        self.__equation_creator()
    
    def __equation_creator(self):
        self._equation_z = {'a': self._dot_end['z'] - self._dot_int['z'], 'b': self._dot_int['z']}
        self._equation_y = {'a': self._dot_end['y'] - self._dot_int['y'], 'b': self._dot_int['y']}
        self._equation_x = {'a': self._dot_end['x'] - self._dot_int['x'], 'b': self._dot_int['x']}

    def get_dot(self,var):
        x = self._equation_x['a']*var + self._equation_x['b']
        y = self._equation_y['a']*var + self._equation_y['b']
        z = self._equation_z['a']*var + self._equation_z['b']
        return {'x':x, 'y':y, 'z':z}

    def __str__(self):
        return("Line, from={} : to={}".format(self._dot_int,self._dot_end))