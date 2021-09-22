from PySide2.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from model.widget_model import *
from modules.basic import deg2rad, spherical2catersian

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
        
    def set_2D_view(self):
        self._canvas_2D = FigureCanvas(Figure())
        self._toolbar_2D = NavigationToolbar(self._canvas_2D, self)
        
        self._vertical_layout.addWidget(self._toolbar_2D)
        self._vertical_layout.addWidget(self._canvas_2D)
        self.config_2D_plot()
        
    def config_2D_plot(self):
        self._canvas_2D.axes = self._canvas_2D.figure.add_subplot(111)
        self._canvas_2D.axes.set_facecolor("k")
        self._canvas_2D.figure.set_facecolor("white")
        self._canvas_2D.axes.set_title("Star Catalog 2D")
        self._canvas_2D.axes.set_xlabel("Ascensao  reta [deg]")
        self._canvas_2D.axes.set_ylabel("Declinacao [deg]")
        self._canvas_2D.axes.set_xlim(0, 360)
        self._canvas_2D.axes.set_ylim(-90, 90)
        self._canvas_2D.draw()
    
    def set_3D_view(self):
        self._canvas_3D = FigureCanvas(Figure())
        self._toolbar_3D = NavigationToolbar(self._canvas_3D, self)
    
        self._vertical_layout.addWidget(self._toolbar_3D)
        self._vertical_layout.addWidget(self._canvas_3D)
        self.config_3D_plot()
    
    def config_3D_plot(self):
        self._canvas_3D.axes = self._canvas_3D.figure.add_subplot(projection = '3d')    
        self._canvas_3D.axes.set_title("Star Catalog 3D",{'color': 'blue'})
        self._canvas_3D.axes.scatter3D(0, 0, 0, s = 1,color = "red")
        self._canvas_3D.axes.set_facecolor("black")
        self._canvas_3D.figure.set_facecolor("black")
        self._canvas_3D.axes.grid(False)
        self._canvas_3D.axes.w_xaxis.pane.fill = False
        self._canvas_3D.axes.w_yaxis.pane.fill = False
        self._canvas_3D.axes.w_zaxis.pane.fill = False
        self._canvas_3D.axes.tick_params(axis='x', colors='blue')
        self._canvas_3D.axes.tick_params(axis='y', colors='blue')
        self._canvas_3D.axes.tick_params(axis='z', colors='blue')
        self._canvas_3D.axes.yaxis.label.set_color('blue')
        self._canvas_3D.axes.xaxis.label.set_color('blue')
        self._canvas_3D.axes.zaxis.label.set_color('blue')
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
        self._model.camera_position_changed.connect(self.plot_camera_3D)
        self._model.update_graticule.connect(self.plotGraticule)

    def plotGraticule(self, show):
        self.remove_graticule()
        if show == True:
            self.plot_2D_graticule()
            self.plot_3D_graticule()
        
    def plot_2D_graticule(self):
        for i in range(-90, 91, 30):
            self._graticule_plots.append(self._canvas_2D.axes.plot([0, 360], [i, i], color='blue', linewidth = 0.4))
        for i in range(0, 361, 30):
            self._graticule_plots.append(self._canvas_2D.axes.plot([i, i], [-90, 90], color='blue', linewidth = 0.4))
        self._canvas_2D.draw()

    def remove_graticule(self):
        while self._graticule_plots:
            self._graticule_plots[0].pop(0).remove()
            del self._graticule_plots[0] 
        self._canvas_2D.draw()
        self._canvas_3D.draw()

    def plot_3D_graticule(self):
        ar, dec = [], []
        for j in range(0,360,60):
            for i in range(-90,91, 5):
                ar.append(deg2rad(j))
                dec.append(deg2rad(i))
            for i in range(90,-91, -5):
                ar.append(deg2rad(j+30))
                dec.append(deg2rad(i))
        
        x,y,z=spherical2catersian(ar, dec)
        self._graticule_plots.append(self._canvas_3D.axes.plot(x,y,z, color='blue', linewidth = 0.4))
        self._canvas_3D.draw()
        
        for i in range(-60, 90, 30):
            ar, dec = [], []
            for j in range(0, 361, 5):
                ar.append(deg2rad(j))
                dec.append(deg2rad(i))
            x,y,z=spherical2catersian(ar, dec)
            self._graticule_plots.append(self._canvas_3D.axes.plot(x,y,z, color='blue', linewidth = 0.4))
            
    def plot_stars(self, stars):
        self._canvas_3D.axes.scatter3D(stars['x'], stars['y'], stars['z'], s = stars['v'], color = "white")
        self._canvas_2D.axes.scatter(stars['ar'], stars['dec'], s = stars['v'], c = 'white')
        self._canvas_3D.draw()
        self._canvas_2D.draw()
        
    def plot_camera_3D(self, camera):
        self.remove_camera_3D()
        if not self._model.show_camera:
            return
        if self._model.show_camera:
            self._camera_position.append(self._canvas_3D.axes.plot( camera['x'], camera['y'], camera['z'], color = 'g', linewidth = 5))
            self._camera_position.append(self._canvas_3D.axes.plot( [0,camera['x'][0],camera['x'][3]], [0,camera['y'][0],camera['y'][3]], [0,camera['z'][0],camera['z'][3]], color = 'g', linewidth = 5))
            self._camera_position.append(self._canvas_3D.axes.plot( [0,camera['x'][1]], [0,camera['y'][1]], [0,camera['z'][1]], color = 'y', linewidth = 5))
            self._camera_position.append(self._canvas_3D.axes.plot( [0,camera['x'][2]], [0,camera['y'][2]], [0,camera['z'][2]], color = 'r', linewidth = 5))
            self._camera_position.append(self._canvas_3D.axes.plot( [0,camera['x'][3]], [0,camera['y'][3]], [0,camera['z'][3]], color = 'b', linewidth = 5))
        self._canvas_3D.draw()        
    
    def remove_camera_3D(self):
        while self._camera_position:
            self._camera_position[0].pop(0).remove()
            del self._camera_position[0] 
        self._canvas_3D.draw()