#import sys
#sys.path.append("../views/")
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

import modules.loadfile as loadfile
from model.model import Model
from views.MainWindow_ui import Ui_MainWindow
try:
    from MainWindow_ui import Ui_MainWindow
except ImportError:
    from views.MainWindow_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,  model : Model, main_controller, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self._model = model
        self._main_controller = main_controller
        
        #connect to controller
        self.loadStarsFile.clicked.connect(self.openStars)
        self.view3D_icon.clicked.connect(self._main_controller.change_view_plot_mode)
        self.view3D_text.clicked.connect(self._main_controller.change_view_plot_mode)
        
        #event signal
        self._model.stars_input_file_changed.connect(self.update_plot)
        self._model.view_plot_mode_changed.connect(self.change_mode_view_plot)
        self._model.view_plot_mode_changed.connect(self.change_mode_view_icon)
        self._model.view_plot_mode_changed.connect(self.change_mode_view_text)
    
        #load saved data
        self._model.load()

    def openStars(self):
        file = QFileDialog(self)
        file.setNameFilter("*.csv")
        file.setFileMode(QFileDialog.ExistingFile)
        file.setWindowTitle('Load Stars File')
        if file.exec_():
            fileName = file.selectedFiles()
            fileName = fileName[0]
            self._main_controller.change_stars_input_file(fileName)
            
    def update_plot(self,value):
        try:
            n, v, ar, dec = loadfile.loadCatalog(value)
            self.viewPlot.update_data(ar,dec,v)
        except FileNotFoundError:
            pass
    
    def change_mode_view_icon(self,value):
        icon1 = QIcon()
        if value:
            icon1.addFile(u":/icon/icons/3d.png", QSize(), QIcon.Normal)
        else:
            icon1.addFile(u":/icon/icons/axis.png", QSize(), QIcon.Normal)
        self.view3D_icon.setIcon(icon1)
        self.view3D_icon.setIconSize(QSize(64, 64))
        self.view3D_icon.setChecked(value)

    def change_mode_view_text(self,value):
        self.view3D_text.setChecked(value)
    
    def change_mode_view_plot(self,value):
        self.viewPlot.view3D(value)
