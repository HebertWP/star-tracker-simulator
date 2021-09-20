from PySide2.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from model.widget_model import *
from modules.basic import spherical2catersian

class Widget(QWidget):
    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())
        self.toolbar = NavigationToolbar(self.canvas, self)
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.toolbar)
        vertical_layout.addWidget(self.canvas)
        self.setLayout(vertical_layout)
        self.set3D()
    
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, value : WidgetModel):
        self._model = value
    
        #events signal
        self._model.update_all.connect(self.update_all)
        self._model.update_camera.connect(self.plotCamera3D)
    
    def set2D(self):
        self._mode = ViewMode.VIEW2D
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
        self.canvas.draw()
    
    def set3D(self):
        self._mode = ViewMode.VIEW3D
        if hasattr(self.canvas,'axes'):
            self.canvas.axes.remove()
        self.canvas.axes = self.canvas.figure.add_subplot(projection = '3d')    
        self.canvas.axes.set_title("Star Catalog 3D",{'color': 'blue'})
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
    
    def update_all(self,value):
        if value == ViewMode.VIEW2D and self._mode != value:
            self.set2D()
        elif value == ViewMode.VIEW3D and self._mode != value:
            self.set3D()
        if value == ViewMode.VIEW3D:
            self.plotCamera3D(self._model.camera_position)
            self.plot3D()
        else:
            self.plot2D()

    def plot2D(self):
        value = self._model.stars
        if not value == {}:
            self.canvas.axes.scatter(value['ar'], value['dec'], s = value['v'], c = 'white')
        self.canvas.draw()

    def plot3D(self):
        value = self._model.stars
        if not value == {}:
            self.canvas.axes.scatter3D(value['x'], value['y'], value['z'], s = value['v'], color = "white")
        self.canvas.draw()

    def plotCamera3D(self, camera):
        if camera == {} or not self._model.show_camera:
            self.set3D()
            self.plot3D()
            return
        
        if hasattr(self,'_camera_line0'):
            self._camera_line0.pop(0).remove()
            self._camera_line1.pop(0).remove()
            self._camera_line2.pop(0).remove()
            self._camera_line3.pop(0).remove()
            self._camera_line4.pop(0).remove()
        
        #x,y,z = spherical2catersian(self._model.ar,self._model.dec)
        #self._camera_dots = self.canvas.axes.scatter3D(x, y, z, s = 5, color = "g")
        #self._camera_dots = self.canvas.axes.scatter3D(camera['x'], camera['y'], camera['z'], s = 5, color = "g")
        self._camera_line0 = self.canvas.axes.plot( camera['x'], camera['y'], camera['z'], color = 'g', linewidth = 5)
        self._camera_line1 = self.canvas.axes.plot( [0,camera['x'][0],camera['x'][3]], [0,camera['y'][0],camera['y'][3]], [0,camera['z'][0],camera['z'][3]], color = 'g', linewidth = 5)
        self._camera_line2 = self.canvas.axes.plot( [0,camera['x'][1]], [0,camera['y'][1]], [0,camera['z'][1]], color = 'y', linewidth = 5)
        self._camera_line3 = self.canvas.axes.plot( [0,camera['x'][2]], [0,camera['y'][2]], [0,camera['z'][2]], color = 'r', linewidth = 5)
        self._camera_line4 = self.canvas.axes.plot( [0,camera['x'][3]], [0,camera['y'][3]], [0,camera['z'][3]], color = 'b', linewidth = 5)
        self.canvas.draw()