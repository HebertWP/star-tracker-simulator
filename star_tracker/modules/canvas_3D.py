from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

try:
    from modules.basic import *
    from modules.line import *
except ImportError:
    from star_tracker.modules.basic import *
    from star_tracker.modules.line import *

class Canvas3D(FigureCanvas):
    def __init__(self,figure=None):
        super().__init__(figure=figure)
        self.__config()
        self.stars = {'x':[],'y':[],'z':[], 'v':[]}
        
        self._graticule_plots = []
        self._stars_plots = []
        self._camera_position = []

        self._graticule_color = "yellow"
        self._camera_linewidth = 1 

    def __config(self):
        color = 'white'
        self.axes = self.figure.add_subplot(projection = '3d')    
        self.axes.set_title("Star Catalog 3D",{'color': color})
        self.axes.scatter3D(0, 0, 0, s = 1,color = "red")
        self.axes.set_facecolor("black")
        self.figure.set_facecolor("black")
        self.axes.grid(False)
        self.axes.w_xaxis.pane.fill = False
        self.axes.w_yaxis.pane.fill = False
        self.axes.w_zaxis.pane.fill = False
        self.axes.tick_params(axis='x', colors=color)
        self.axes.tick_params(axis='y', colors=color)
        self.axes.tick_params(axis='z', colors=color)
        self.axes.yaxis.label.set_color(color)
        self.axes.xaxis.label.set_color(color)
        self.axes.zaxis.label.set_color(color)
        self.axes.set_xlim(-1, 1)
        self.axes.set_ylim(-1, 1)
        self.axes.set_zlim(-1, 1)
        self.axes.set_xlabel('X axis')
        self.axes.set_ylabel('Y axis')
        self.axes.set_zlabel('Z axis')
    
    def showGraticule(self, show=False):
        while self._graticule_plots:
            self._graticule_plots[0].pop(0).remove()
            del self._graticule_plots[0]
        if not show:
            return 
        ar, dec = [], []
        for j in range(0,360,60):
            for i in range(-90,91, 5):
                ar.append(deg2rad(j))
                dec.append(deg2rad(i))
            for i in range(90,-91, -5):
                ar.append(deg2rad(j+30))
                dec.append(deg2rad(i))
        
        x,y,z=spherical2catersian(ar, dec)
        self._graticule_plots.append(self.axes.plot(x,y,z, color=self._graticule_color, linewidth = 0.4))
        
        for i in range(-60, 90, 30):
            ar, dec = [], []
            for j in range(0, 361, 5):
                ar.append(deg2rad(j))
                dec.append(deg2rad(i))
            x,y,z=spherical2catersian(ar, dec)
            self._graticule_plots.append(self.axes.plot(x,y,z, color=self._graticule_color, linewidth = 0.4))
    
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
        if not show:
            return
        self._stars_plots.append(self.axes.scatter3D(self.stars['x'], self.stars['y'], self.stars['z'], s = self.stars['v'], color = "white"))
    
    @property
    def camera(self):
        return self._camera
    @camera.setter
    def camera(self, value):
        self._camera = value
    
    def show_camera(self, show = False):
        camera_3d  = self._camera['3D']
        camera_pos = self._camera['3D_pos']
        while self._camera_position:
            try:
                self._camera_position[0].pop(0).remove()
            except :
                self._camera_position[0].remove()
            del self._camera_position[0]
        
        self._camera_position.append(self.axes.plot( [0,camera_3d['x'][0]], [0,camera_3d['y'][0]], [0,camera_3d['z'][0]], color = 'g', linewidth =self._camera_linewidth))
        self._camera_position.append(self.axes.plot( [0,camera_3d['x'][1]], [0,camera_3d['y'][1]], [0,camera_3d['z'][1]], color = 'g', linewidth =self._camera_linewidth))
        self._camera_position.append(self.axes.plot( [0,camera_3d['x'][2]], [0,camera_3d['y'][2]], [0,camera_3d['z'][2]], color = 'g', linewidth =self._camera_linewidth))
        self._camera_position.append(self.axes.plot( [0,camera_3d['x'][3]], [0,camera_3d['y'][3]], [0,camera_3d['z'][3]], color = 'g', linewidth =self._camera_linewidth))
        
        self._camera_position.append(self.axes.scatter3D( camera_3d['x'][0], camera_3d['y'][0], camera_3d['z'][0], color='red'))
        self._camera_position.append(self.axes.scatter3D( camera_3d['x'][1], camera_3d['y'][1], camera_3d['z'][1], color='green'))
        self._camera_position.append(self.axes.scatter3D( camera_3d['x'][2], camera_3d['y'][2], camera_3d['z'][2], color='orange'))
        self._camera_position.append(self.axes.scatter3D( camera_3d['x'][3], camera_3d['y'][3], camera_3d['z'][3], color='yellow'))
    
        self._camera_position.append(self.axes.plot( camera_3d['x'][0:2], camera_3d['y'][0:2], camera_3d['z'][0:2], color = 'orange', linewidth =self._camera_linewidth))
        self._camera_position.append(self.axes.plot( camera_3d['x'][1:3], camera_3d['y'][1:3], camera_3d['z'][1:3], color = 'y', linewidth =self._camera_linewidth))
        self._camera_position.append(self.axes.plot( [camera_3d['x'][0],camera_3d['x'][3]], [camera_3d['y'][0],camera_3d['y'][3]], [camera_3d['z'][0],camera_3d['z'][3]], color = 'green', linewidth =self._camera_linewidth))
        self._camera_position.append(self.axes.plot( [camera_3d['x'][2],camera_3d['x'][3]], [camera_3d['y'][2],camera_3d['y'][3]], [camera_3d['z'][2],camera_3d['z'][3]], color = 'r', linewidth = self._camera_linewidth))
        
        z = camera_pos['z']
        x = camera_pos['x']
        y = camera_pos['y']
        self._camera_position.append(self.axes.quiver(0, 0, 0, z[0], z[1], z[2], color="blue"))
        self._camera_position.append(self.axes.quiver(0, 0, 0, x[0], x[1], x[2], color="red"))
        self._camera_position.append(self.axes.quiver(0, 0, 0, y[0], y[1], y[2], color="green"))