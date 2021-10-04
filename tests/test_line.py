from star_tracker.modules.line import Line

class TestLine:
    def load(self):
        self.__end = {'x':2, 'y':1,'z':4}
        self.__init = {'x':1, 'y':0,'z':0}
        self.__line = Line(self.__init, self.__end)
        
    def test_dot(self):
        self.load()

        dot=self.__line.get_dot(0.5)
        assert dot == {'x':1.5, 'y':0.5, 'z':2}

        dot=self.__line.get_dot(0)
        assert dot == {'x':1, 'y':0, 'z':0}
    
    def test_line_str(self):
        self.load()
        
        assert str(self.__line) == "Line, from={'x': 1, 'y': 0, 'z': 0} : to={'x': 2, 'y': 1, 'z': 4}"