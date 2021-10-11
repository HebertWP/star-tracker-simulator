from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

try:
    from modules.basic import *
    from modules.line import *
except ImportError:
    from star_tracker.modules.basic import *
    from star_tracker.modules.line import *

class Canvas2D(FigureCanvas):
    def __init__(self,figure=None):
        super().__init__(figure=figure)
        self.__config()
        self.stars = {'dec':[],'ar':[],'v':[]}
        self.camera = {'dec':[],'ar':[]}

        self._graticule_plots = []
        self._stars_plots = []
        self._camera_position = []

        self._graticule_color = "yellow"
        self._camera_linewidth = 1 
        

    def __config(self):
        self.axes = self.figure.add_subplot(111)
        self.axes.set_facecolor("k")
        self.figure.set_facecolor("white")
        self.axes.set_title("Star Catalog 2D")
        self.axes.set_xlabel("Ascensao  reta [deg]")
        self.axes.set_ylabel("Declinacao [deg]")
        self.axes.set_xlim(0, 360)
        self.axes.set_ylim(-90, 90)
    
    def showGraticule(self, show=False):
        if show:
            for i in range(-90, 91, 30):
                self._graticule_plots.append(self.axes.plot([0, 360], [i, i], color=self._graticule_color, linewidth = 0.4))
            for i in range(0, 361, 30):
                self._graticule_plots.append(self.axes.plot([i, i], [-90, 90], color=self._graticule_color, linewidth = 0.4))
        else:
            while self._graticule_plots:
                self._graticule_plots[0].pop(0).remove()
                del self._graticule_plots[0]
    @property
    def stars(self):
        return self._stars
    
    @stars.setter
    def stars(self, value):
        self._stars = value
        
    def show_stars(self, show=False):
        value = self.stars
        while self._stars_plots:
            self._stars_plots[0].remove()
            del self._stars_plots[0]
        if show:
            self._stars_plots.append(self.axes.scatter(value['ar'], value['dec'], s = value['v'], c = 'white'))
        
    @property
    def camera(self):
        return self._camera
    @camera.setter
    def camera(self, value):
        self._camera = value
    
    def show_camera(self, show = False):
        ar = rad2deg(self.camera['ar'])
        dec = rad2deg(self.camera['dec'])
        
        while self._camera_position:
            try:
                self._camera_position[0].pop(0).remove()
            except :
                self._camera_position[0].remove()
            del self._camera_position[0]
        
        if show:
            self._camera_position.append(self.axes.scatter( ar[0][0], dec[0][0] ,s=10, color='red'))
            self._camera_position.append(self.axes.scatter( ar[0][-1], dec[0][-1] ,s=10, color='green'))
            self._camera_position.append(self.axes.scatter( ar[3][-1],  dec[3][-1] ,s=7, color='yellow'))
            self._camera_position.append(self.axes.scatter( ar[2][-1], dec[2][-1] ,s=7, color='orange'))
        
            self._camera_position.append(self.axes.plot( ar[0], dec[0], color = 'orange', linewidth = self._camera_linewidth))
            self._camera_position.append(self.axes.plot( ar[3], dec[3], color = 'g', linewidth = self._camera_linewidth))
            self._camera_position.append(self.axes.plot( ar[1], dec[1], color = 'y', linewidth = self._camera_linewidth))
            self._camera_position.append(self.axes.plot( ar[2], dec[2], color = 'r', linewidth = self._camera_linewidth))
            #self.figure.savefig("./ola.png")