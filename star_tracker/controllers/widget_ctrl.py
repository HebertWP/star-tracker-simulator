from PySide2.QtCore import QObject, Slot

#my models includes
from model.main_model import *

#my modules includes
import modules.loadfile as loadfile
import modules.basic as basic
from modules.stars import Stars

class WidgetController(QObject):
    def __init__(self, model : MainModel):
        super().__init__()

        self._model = model
        
        self._model.view_plot_mode_changed.connect(self.change_view_mode)
        self._model.show_camera_changed.connect(self.change_camera_view)
        self._model.graticule_view_changed.connect(self.change_graticule_view)

        self._model.camera_input_file_changed.connect(self.camera_file)
        self._model.roll_changed.connect(self.roll)
        self._model.ar_changed.connect(self.ar)
        self._model.dec_changed.connect(self.dec)
            
    def change_view_mode(self,value):
        pass
        #self._model.view_mode = ViewMode.VIEW3D if value else ViewMode.VIEW2D
    
    def change_camera_view(self, value):
        pass
        #self._model.show_camera = value

    def change_graticule_view(self, value):
        self._model.show_graticule = value

    def camera_file(self, value):
        pass
        """
        try:
            self._model.camera.config = value
            data = {}
            data['3D'] = self._model.camera.position_dict
            data['2D'] = self._model.camera.position_dict_spherical
            data['3D_pos'] = self._model.camera.coordinates
            self._model.camera_position = data
        except FileNotFoundError:
            pass
        """
    def roll(self,value):
        pass
        """
        self._model.camera.roll= basic.deg2rad(value)
        self._model.roll = basic.deg2rad(value)
        self._model.camera_position = {'3D':self._model.camera.position_dict, '2D': self._model.camera.position_dict_spherical,'3D_pos':self._model.camera.coordinates}
        """

    def ar(self,value):
        pass
        """
        self._model.camera.ar = basic.deg2rad(value)
        self._model.ar = basic.deg2rad(value)
        self._model.camera_position = {'3D':self._model.camera.position_dict, '2D': self._model.camera.position_dict_spherical,'3D_pos':self._model.camera.coordinates}
        """
    def dec(self,value):
        pass
        """
        self._model.camera.dec = basic.deg2rad(value)
        self._model.dec = basic.deg2rad(value)
        self._model.camera_position = {'3D':self._model.camera.position_dict, '2D': self._model.camera.position_dict_spherical,'3D_pos':self._model.camera.coordinates}
        """
    def save_frame(self, value):
        pass
        #self._model.camera.take_frame(value)
    