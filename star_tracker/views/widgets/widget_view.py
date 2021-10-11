from PySide2.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from numpy import rad2deg
from model.widget_model import *
from modules.basic import deg2rad, spherical2catersian

try:
    from modules.canvas_2D import *
    from modules.canvas_3D import *
except ImportError:
    from star_tracker.modules.canvas_2D import *
    from star_tracker.modules.canvas_3D import *
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
        self._canvas_3D = Canvas3D(Figure())
        self._toolbar_3D = NavigationToolbar(self._canvas_3D, self)
    
        self._vertical_layout.addWidget(self._toolbar_3D)
        self._vertical_layout.addWidget(self._canvas_3D)
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
        
        self._canvas_3D.showGraticule(show)
        self._canvas_3D.draw()
        
    def plot_stars(self, stars):
        self._canvas_2D.stars = stars
        self._canvas_2D.show_stars(True)
        self._canvas_2D.draw()
        
        self._canvas_3D.stars = stars
        self._canvas_3D.show_stars(True)
        self._canvas_3D.draw()
        
    def plot_camera(self, camera):
        camera_3D = {'3D':camera['3D'], '3D_pos': camera['3D_pos']}
        camera_2D = camera['2D']
        
        self._canvas_2D.camera = camera_2D
        self._canvas_2D.show_camera(self._model.show_camera)
        self._canvas_2D.draw()
        
        self._canvas_3D.camera = camera_3D
        self._canvas_3D.show_camera(self._model.show_camera)
        self._canvas_3D.draw()