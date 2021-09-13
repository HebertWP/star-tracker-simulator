from PySide2.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

    
class ViewPlot(QWidget):
    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())
        self.toolbar = NavigationToolbar(self.canvas, self)
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.toolbar)
        vertical_layout.addWidget(self.canvas)
        
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.axes.set_title("Catalogo Estrelar 2D")
        self.canvas.axes.set_xlabel("Ascensao  reta [deg]")
        self.canvas.axes.set_ylabel("Declinacao [deg]")
        self.canvas.axes.set_xlim(0, 360)
        self.canvas.axes.set_ylim(-90, 90)
        self.canvas.axes.set_facecolor("k")
        
        #self.canvas.draw()
        
        self.setLayout(vertical_layout)

    def plotCatalog2D(self,ar,dec, v):
        self.canvas.axes.clear()
        self.canvas.axes.set_title("Catalogo Estrelar 2D")
        self.canvas.axes.set_xlabel("Ascensao  reta [deg]")
        self.canvas.axes.set_ylabel("Declinacao [deg]")
        #self.canvas.axes.legend(('Stars'),loc='upper right')
        self.canvas.axes.scatter(ar, dec, s=v, c='white')
        self.canvas.draw()
        