from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

try:
    from modules.basic import *
    from modules.line import *
except ImportError:
    from star_tracker.modules.basic import *
    from star_tracker.modules.line import *

class CameraView(FigureCanvas):
    def __init__(self,figure=None):
        super().__init__(figure=figure)
        self.__config()
        self._stars = {'x':[],'y':[],'v':[]}
        
        self._stars_plots = []

    def __config(self):
        self.axes = self.figure.add_subplot(111)
        self.axes.set_facecolor("k")
        self.figure.set_facecolor("white")
        self.axes.set_title("Camera Frame View")
        self.axes.set_xlabel("x")
        self.axes.set_ylabel("y")
        self.axes.axis('scaled')
        self.w = 1
        self.h = 1
    
    @property
    def w(self):
        return self._w
        
    @w.setter
    def w(self, value):
        self._w = value
        self.axes.set_xlim(-self._w/2, self._w/2)
        
    @property
    def h(self):
        return self._h

    @h.setter
    def h (self, value):
        self._h = value
        self.axes.set_ylim(-self._h/2, self._h/2)
        
    @property
    def stars(self):
        return self._stars
    
    @stars.setter
    def stars(self, value):
        self._stars = value
        
        while self._stars_plots:
            self._stars_plots[0].remove()
            del self._stars_plots[0]
        for i in range(len(value['y'])):
            value['y'][i] =-value['y'][i]*self.w/2
            value['z'][i] = value['z'][i]*self.h/2
            
        self._stars_plots.append(self.axes.scatter(value['y'], value['z'], s = value['v'], c = 'white'))
        
        self.draw()