from star_tracker.modules.line import Line

class TestLine:
    def test_dot(self):
        end = {'x':1, 'y':0,'z':0}
        init = {'x':0, 'y':0,'z':0}
        line = Line(init, end)
        
        dot=line.get_dot(0.5)

        assert dot == {'x':0.5, 'y':0, 'z':0}
        