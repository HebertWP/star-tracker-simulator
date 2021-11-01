from PySide2.QtCore import QObject, Slot

#my models includes
from model.widget_model import *
from model.main_model import *

#my modules includes
import modules.loadfile as loadfile
import modules.basic as basic
from modules.camera import Camera
from modules.stars import Stars

class WidgetController(QObject):
    def __init__(self, main_model : MainModel, widget_model : WidgetModel):
        super().__init__()

        self._main_model = main_model
        self._widget_model = widget_model
        
        self._main_model.view_plot_mode_changed.connect(self.change_view_mode)
        self._main_model.show_camera_changed.connect(self.change_camera_view)
        self._main_model.graticule_view_changed.connect(self.change_graticule_view)

        self._main_model.stars_input_file_changed.connect(self.load_file)
        self._main_model.camera_input_file_changed.connect(self.camera_file)
        self._main_model.roll_changed.connect(self.roll)
        self._main_model.ar_changed.connect(self.ar)
        self._main_model.dec_changed.connect(self.dec)
        
        self._camera = Camera()
        self._stars = Stars()
            
    def change_view_mode(self,value):
        self._widget_model.view_mode = ViewMode.VIEW3D if value else ViewMode.VIEW2D
    
    def change_camera_view(self, value):
        self._widget_model.show_camera = value

    def change_graticule_view(self, value):
        self._widget_model.show_graticule = value

    def load_file(self, value):
        try:
            self._stars.load_catalog(value)
            aux = Stars()
            aux.load_catalog(value)
            self._camera.stars = aux
            self._widget_model.stars = self._stars.getDict()
        except FileNotFoundError:
            pass

    def camera_file(self, value):
        try:
            self._camera.config = value
            data = {}
            data['3D'] = self._camera.position_dict
            data['2D'] = self._camera.position_dict_spherical
            data['3D_pos'] = self._camera.coordinates
            self._widget_model.camera_position = data
        except FileNotFoundError:
            pass
    
    def roll(self,value):
        self._camera.roll= basic.deg2rad(value)
        self._camera.take_frame()
        self._widget_model.roll = basic.deg2rad(value)
        self._widget_model.camera_position = {'3D':self._camera.position_dict, '2D': self._camera.position_dict_spherical,'3D_pos':self._camera.coordinates}
        
    def ar(self,value):
        self._camera.ar = basic.deg2rad(value)
        self._camera.take_frame()
        self._widget_model.ar = basic.deg2rad(value)
        self._widget_model.camera_position = {'3D':self._camera.position_dict, '2D': self._camera.position_dict_spherical,'3D_pos':self._camera.coordinates}

    def dec(self,value):
        self._camera.dec = basic.deg2rad(value)
        self._camera.take_frame()
        self._widget_model.dec = basic.deg2rad(value)
        self._widget_model.camera_position = {'3D':self._camera.position_dict, '2D': self._camera.position_dict_spherical,'3D_pos':self._camera.coordinates}