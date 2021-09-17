from PySide2.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from model.widget_model import *

class Widget(QWidget):
    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())
        self.toolbar = NavigationToolbar(self.canvas, self)
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.toolbar)
        vertical_layout.addWidget(self.canvas)
        self.setLayout(vertical_layout)
    
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, value : WidgetModel):
        self._model = value
    
        #events signal
        self._model.update_view.connect(self.update)
        
    def update(self, value):
        if value == {}:
            return
        if value['mode'] == ViewMode.VIEW2D:
            self.plot2D(value)
        else:
            self.plot3D(value)
    
    def plot2D(self, value):
        if hasattr(self.canvas,'axes'):
            self.canvas.axes.remove()
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.axes.set_facecolor("k")
        self.canvas.figure.set_facecolor("white")
        self.canvas.axes.set_title("Star Catalog 2D")
        self.canvas.axes.set_xlabel("Ascensao  reta [deg]")
        self.canvas.axes.set_ylabel("Declinacao [deg]")
        self.canvas.axes.set_xlim(0, 360)
        self.canvas.axes.set_ylim(-90, 90)
        self.canvas.axes.scatter(value['ar'], value['dec'], s = value['v'], c = 'white')
        self.canvas.draw()

    def plot3D(self, value):
        if hasattr(self.canvas,'axes'):
            self.canvas.axes.remove()
        self.canvas.axes = self.canvas.figure.add_subplot(projection = '3d')    
        self.canvas.axes.set_title("Star Catalog 3D",{'color': 'blue'})
        self.canvas.axes.scatter3D(value['x'], value['y'], value['z'], s = value['v'], color = "white")
        self.canvas.axes.scatter3D(0, 0, 0, s = 1,color = "red")
        self.canvas.axes.set_facecolor("black")
        self.canvas.figure.set_facecolor("black")
        self.canvas.axes.grid(False)
        self.canvas.axes.w_xaxis.pane.fill = False
        self.canvas.axes.w_yaxis.pane.fill = False
        self.canvas.axes.w_zaxis.pane.fill = False
        self.canvas.axes.tick_params(axis='x', colors='blue')
        self.canvas.axes.tick_params(axis='y', colors='blue')
        self.canvas.axes.tick_params(axis='z', colors='blue')
        self.canvas.axes.yaxis.label.set_color('blue')
        self.canvas.axes.xaxis.label.set_color('blue')
        self.canvas.axes.zaxis.label.set_color('blue')
        self.canvas.axes.set_xlim(-1, 1)
        self.canvas.axes.set_ylim(-1, 1)
        self.canvas.axes.set_zlim(-1, 1)
        self.canvas.axes.set_xlabel('X axis')
        self.canvas.axes.set_ylabel('Y axis')
        self.canvas.axes.set_zlabel('Z axis')            
        self.canvas.draw()