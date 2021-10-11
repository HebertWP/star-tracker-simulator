from PySide2.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from numpy import rad2deg
from model.widget_model import *
from modules.basic import deg2rad, spherical2catersian

try:
    from modules.canvas_2D import *
except ImportError:
    from star_tracker.modules.canvas_2D import *

class Widget(QWidget):
    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)

        self._vertical_layout = QVBoxLayout()
        self._graticule_plots = []
        self._camera_position = []

        self.set_2D_view()
        self.set_3D_view()
        
        self.set_view(ViewMode.VIEW2D)
        self.setLayout(self._vertical_layout)
        self._graticule_color = "yellow"
        
    def set_2D_view(self):
        self._canvas_2D = Canvas2D(Figure())
        self._toolbar_2D = NavigationToolbar(self._canvas_2D, self)
        
        self._vertical_layout.addWidget(self._toolbar_2D)
        self._vertical_layout.addWidget(self._canvas_2D)
        self._canvas_2D.draw()
    
    def set_3D_view(self):
        self._canvas_3D = FigureCanvas(Figure())
        self._toolbar_3D = NavigationToolbar(self._canvas_3D, self)
    
        self._vertical_layout.addWidget(self._toolbar_3D)
        self._vertical_layout.addWidget(self._canvas_3D)
        self.config_3D_plot()
    
    def config_3D_plot(self):
        color = 'white'
        self._canvas_3D.axes = self._canvas_3D.figure.add_subplot(projection = '3d')    
        self._canvas_3D.axes.set_title("Star Catalog 3D",{'color': color})
        self._canvas_3D.axes.scatter3D(0, 0, 0, s = 1,color = "red")
        self._canvas_3D.axes.set_facecolor("black")
        self._canvas_3D.figure.set_facecolor("black")
        self._canvas_3D.axes.grid(False)
        self._canvas_3D.axes.w_xaxis.pane.fill = False
        self._canvas_3D.axes.w_yaxis.pane.fill = False
        self._canvas_3D.axes.w_zaxis.pane.fill = False
        self._canvas_3D.axes.tick_params(axis='x', colors=color)
        self._canvas_3D.axes.tick_params(axis='y', colors=color)
        self._canvas_3D.axes.tick_params(axis='z', colors=color)
        self._canvas_3D.axes.yaxis.label.set_color(color)
        self._canvas_3D.axes.xaxis.label.set_color(color)
        self._canvas_3D.axes.zaxis.label.set_color(color)
        self._canvas_3D.axes.set_xlim(-1, 1)
        self._canvas_3D.axes.set_ylim(-1, 1)
        self._canvas_3D.axes.set_zlim(-1, 1)
        self._canvas_3D.axes.set_xlabel('X axis')
        self._canvas_3D.axes.set_ylabel('Y axis')
        self._canvas_3D.axes.set_zlabel('Z axis')
        self._canvas_3D.draw()   
        
    def set_view(self, mode):
        if mode == ViewMode.VIEW2D:
            self._canvas_2D.setVisible(True)
            self._toolbar_2D.setVisible(True)
            self._canvas_3D.setVisible(False)
            self._toolbar_3D.setVisible(False)
        else:
            self._canvas_2D.setVisible(False)
            self._toolbar_2D.setVisible(False)
            self._canvas_3D.setVisible(True)
            self._toolbar_3D.setVisible(True)
        
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, value : WidgetModel):
        self._model = value
    
        #events signal
        self._model.view_mode_changed.connect(self.set_view)
        self._model.stars_changed.connect(self.plot_stars)
        self._model.camera_position_changed.connect(self.plot_camera)
        self._model.update_graticule.connect(self.plotGraticule)

    def plotGraticule(self, show):
        self._canvas_2D.showGraticule(show)
        self._canvas_2D.draw()
        
        self.remove_graticule()
        if show == True:    
            self.plot_3D_graticule()
    
    def remove_graticule(self):
        while self._graticule_plots:
            self._graticule_plots[0].pop(0).remove()
            del self._graticule_plots[0] 
        self._canvas_3D.draw()

    def plot_3D_graticule(self):
        #if self._model.view_mode == ViewMode.VIEW2D:
        #    return
        ar, dec = [], []
        for j in range(0,360,60):
            for i in range(-90,91, 5):
                ar.append(deg2rad(j))
                dec.append(deg2rad(i))
            for i in range(90,-91, -5):
                ar.append(deg2rad(j+30))
                dec.append(deg2rad(i))
        
        x,y,z=spherical2catersian(ar, dec)
        self._graticule_plots.append(self._canvas_3D.axes.plot(x,y,z, color=self._graticule_color, linewidth = 0.4))
        self._canvas_3D.draw()
        
        for i in range(-60, 90, 30):
            ar, dec = [], []
            for j in range(0, 361, 5):
                ar.append(deg2rad(j))
                dec.append(deg2rad(i))
            x,y,z=spherical2catersian(ar, dec)
            self._graticule_plots.append(self._canvas_3D.axes.plot(x,y,z, color=self._graticule_color, linewidth = 0.4))
        self._canvas_3D.draw()

    def plot_stars(self, stars):
        self._canvas_2D.stars = stars
        self._canvas_2D.show_stars(True)
        self._canvas_2D.draw()
        self._canvas_3D.axes.scatter3D(stars['x'], stars['y'], stars['z'], s = stars['v'], color = "white")
        self._canvas_3D.draw()
    
    def plot_camera(self, camera):
        camera_3D = camera['3D']
        camera_2D = camera['2D']
        position_3D = camera['3D_pos']

        self.remove_camera()
        self._canvas_2D.camera = camera_2D
        self._canvas_2D.show_camera(self._model.show_camera)
        self._canvas_2D.draw()
        if self._model.show_camera:
            #if self._model.view_mode == ViewMode.VIEW3D:
            self.plot_camera_3D(camera_3D,position_3D)
            #else:
            
    def plot_camera_3D(self,camera_3D, position):
        came_linewidth = 1 
        self._camera_position.append(self._canvas_3D.axes.plot( [0,camera_3D['x'][0]], [0,camera_3D['y'][0]], [0,camera_3D['z'][0]], color = 'g', linewidth = came_linewidth))
        self._camera_position.append(self._canvas_3D.axes.plot( [0,camera_3D['x'][1]], [0,camera_3D['y'][1]], [0,camera_3D['z'][1]], color = 'g', linewidth = came_linewidth))
        self._camera_position.append(self._canvas_3D.axes.plot( [0,camera_3D['x'][2]], [0,camera_3D['y'][2]], [0,camera_3D['z'][2]], color = 'g', linewidth = came_linewidth))
        self._camera_position.append(self._canvas_3D.axes.plot( [0,camera_3D['x'][3]], [0,camera_3D['y'][3]], [0,camera_3D['z'][3]], color = 'g', linewidth = came_linewidth))
        
        self._camera_position.append(self._canvas_3D.axes.scatter3D( camera_3D['x'][0], camera_3D['y'][0], camera_3D['z'][0], color='red'))
        self._camera_position.append(self._canvas_3D.axes.scatter3D( camera_3D['x'][1], camera_3D['y'][1], camera_3D['z'][1], color='green'))
        self._camera_position.append(self._canvas_3D.axes.scatter3D( camera_3D['x'][2], camera_3D['y'][2], camera_3D['z'][2], color='orange'))
        self._camera_position.append(self._canvas_3D.axes.scatter3D( camera_3D['x'][3], camera_3D['y'][3], camera_3D['z'][3], color='yellow'))
    
        self._camera_position.append(self._canvas_3D.axes.plot( camera_3D['x'][0:2], camera_3D['y'][0:2], camera_3D['z'][0:2], color = 'orange', linewidth = came_linewidth))
        self._camera_position.append(self._canvas_3D.axes.plot( camera_3D['x'][1:3], camera_3D['y'][1:3], camera_3D['z'][1:3], color = 'y', linewidth = came_linewidth))
        self._camera_position.append(self._canvas_3D.axes.plot( [camera_3D['x'][0],camera_3D['x'][3]], [camera_3D['y'][0],camera_3D['y'][3]], [camera_3D['z'][0],camera_3D['z'][3]], color = 'green', linewidth = came_linewidth))
        self._camera_position.append(self._canvas_3D.axes.plot( [camera_3D['x'][2],camera_3D['x'][3]], [camera_3D['y'][2],camera_3D['y'][3]], [camera_3D['z'][2],camera_3D['z'][3]], color = 'r', linewidth = came_linewidth))
        
        z=position['z']
        x=position['x']
        y=position['y']
        self._camera_position.append(self._canvas_3D.axes.quiver(0, 0, 0, z[0], z[1], z[2], color="blue"))
        self._camera_position.append(self._canvas_3D.axes.quiver(0, 0, 0, x[0], x[1], x[2], color="red"))
        self._camera_position.append(self._canvas_3D.axes.quiver(0, 0, 0, y[0], y[1], y[2], color="green"))
        
        self._canvas_3D.draw()

    def remove_camera(self):
        while self._camera_position:
            try:
                self._camera_position[0].pop(0).remove()
            except :
                self._camera_position[0].remove()
            del self._camera_position[0]
        self._canvas_3D.draw()
