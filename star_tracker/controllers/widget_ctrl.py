from PySide2.QtCore import QObject, Slot

#my models includes
from model.widget_model import *
from model.main_model import *

#my modules includes
import modules.loadfile as loadfile
import modules.basic as basic
from modules.camera import Camera

class WidgetController(QObject):
    def __init__(self, main_model : MainModel, widget_model : WidgetModel):
        super().__init__()

        self._main_model = main_model
        self._widget_model = widget_model
        
        self._main_model.view_plot_mode_changed.connect(self.change_view_mode)
        self._main_model.show_camera_changed.connect(self.change_camera_view)

        self._main_model.stars_input_file_changed.connect(self.load_file)
        self._main_model.camera_input_file_changed.connect(self.camera_file)
        self._main_model.roll_changed.connect(self.roll)
        self._main_model.ar_changed.connect(self.ar)
        self._main_model.dec_changed.connect(self.dec)
        
    def change_view_mode(self,value):
        self._widget_model.view_mode = ViewMode.VIEW3D if value else ViewMode.VIEW2D
    
    def change_camera_view(self, value):
        self._widget_model.show_camera = value

    def load_file(self, value):
        pass
        try:
            n, v, ar, dec = loadfile.loadCatalog(value)
            x,y,z = basic.spherical2catersian(basic.deg2rad(ar), basic.deg2rad(dec))
            d = {"v" : v, "ar" : ar, "dec" : dec, "x" : x, "y" : y, "z" : z}
            self._widget_model.stars = d
        except FileNotFoundError:
            pass

    def camera_file(self, value):
        try:
            self._camera = Camera(value)
            self._widget_model.camera_position = self._camera.position_dict
        except FileNotFoundError:
            pass
    
    def roll(self,value):
        self._camera.roll= basic.deg2rad(value)
        self._widget_model.roll = basic.deg2rad(value)
        self._widget_model.camera_position = self._camera.position_dict
        
    def ar(self,value):
        self._camera.ar = basic.deg2rad(value)
        self._widget_model.ar = basic.deg2rad(value)
        self._widget_model.camera_position = self._camera.position_dict

    def dec(self,value):
        self._camera.dec = basic.deg2rad(value)
        self._widget_model.dec = basic.deg2rad(value)
        self._widget_model.camera_position = self._camera.position_dict