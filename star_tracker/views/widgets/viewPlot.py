from PySide2.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from numpy import pi
import modules.basic as basic

class ViewPlot(QWidget):
    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())
        self.toolbar = NavigationToolbar(self.canvas, self)
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.toolbar)
        vertical_layout.addWidget(self.canvas)
        self.setLayout(vertical_layout)
        self.view3D(False)

    def update_data(self, ar, dec,v):
        self._ar = ar
        self._dec = dec
        self._v = v
        self.update_plot()
    
    def view3D(self, mode):
        self._view3d = mode
        self.update_plot()
    
    def update_plot(self):
        if not hasattr(self, '_ar'):
            return
        if not self._view3d:
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
            self.canvas.axes.scatter(self._ar, self._dec, s = self._v, c = 'white')
            self.canvas.draw()
        else:
            if hasattr(self.canvas,'axes'):
                self.canvas.axes.remove()
            self.canvas.axes = self.canvas.figure.add_subplot(projection = '3d')    
            self.canvas.axes.set_title("Star Catalog 3D",{'color': 'blue'})
            ar = basic.deg2rad(self._ar)
            dec = basic.deg2rad(self._dec)
            x,y,z = basic.spherical2catersian(ar, dec)
            self.canvas.axes.scatter3D(x, y, z, s = self._v, color = "white")
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