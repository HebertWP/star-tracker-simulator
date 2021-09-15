from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

from model.main_model import MainModel
from views.MainWindow_ui import Ui_MainWindow
try:
    from MainWindow_ui import Ui_MainWindow
except ImportError:
    from views.MainWindow_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,  model : MainModel, main_controller, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self._model = model
        self._main_controller = main_controller
        
        #connect to controller
        self.loadStarsFile.clicked.connect(self._main_controller.load_stars_dialog)
        self.view3D_icon.clicked.connect(self._main_controller.change_view_plot_mode)
        self.view3D_text.clicked.connect(self._main_controller.change_view_plot_mode)
        self._roll_spin.valueChanged.connect(self._main_controller.change_roll)
        self._roll_scroll.valueChanged.connect(self._main_controller.change_roll)
        self._ar_spin.valueChanged.connect(self._main_controller.change_ar)
        self._ar_scroll.valueChanged.connect(self._main_controller.change_ar)
        self._dec_spin.valueChanged.connect(self._main_controller.change_dec)
        self._dec_scroll.valueChanged.connect(self._main_controller.change_dec)
        
        #event signal
        self._model.view_plot_mode_changed.connect(self.change_mode_view_icon)
        self._model.view_plot_mode_changed.connect(self.change_mode_view_text)
        self._model.load_stars_file_changed.connect(self.open_stars)
        self._model.roll_changed.connect(self.change_roll)
        self._model.ar_changed.connect(self.change_ar)
        self._model.dec_changed.connect(self.change_dec)
        
    def open_stars(self):
        file = QFileDialog(self)
        file.setNameFilter("*.csv")
        file.setFileMode(QFileDialog.ExistingFile)
        file.setWindowTitle('Load Stars File')
        if file.exec_():
            fileName = file.selectedFiles()
            fileName = fileName[0]
            self._main_controller.change_stars_input_file(fileName)
    
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
    
    def change_roll(self, value):
        self._roll_scroll.setValue(value)
        self._roll_spin.setValue(value)
    
    def change_ar(self, value):
        self._ar_scroll.setValue(value)
        self._ar_spin.setValue(value)
    
    def change_dec(self, value):
        self._dec_scroll.setValue(value)
        self._dec_spin.setValue(value)
    
    @property
    def view_plot_widget(self):
        return self.viewPlot