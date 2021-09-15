from PySide2.QtCore import QObject, Slot

#my models includes
from model.widget_model import *
from model.main_model import *

#my modules includes
import modules.loadfile as loadfile
import modules.basic as basic

class WidgetController(QObject):
    def __init__(self, main_model : MainModel, widget_model : WidgetModel):
        super().__init__()

        self._main_model = main_model
        self._widget_model = widget_model
        
        self._main_model.view_plot_mode_changed.connect(self.change_view_mode)
        self._main_model.stars_input_file_changed.connect(self.load_file)
    
    def change_view_mode(self,value):
        self._widget_model.view_mode = ViewMode.VIEW3D if value else ViewMode.VIEW2D
    
    def load_file(self, value):
        try:
            n, v, ar, dec = loadfile.loadCatalog(value)
            x,y,z = basic.spherical2catersian(basic.deg2rad(ar), basic.deg2rad(dec))
            d = {"v" : v, "ar" : ar, "dec" : dec, "x" : x, "y" : y, "z" : z}
            self._widget_model.stars = d
        except FileNotFoundError:
            pass