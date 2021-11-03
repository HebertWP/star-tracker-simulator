from os import error
from PySide2.QtCore import SIGNAL, QObject, Signal
from enum import Enum
from modules.camera import Camera
from modules.stars import Stars

class ViewMode(Enum):
    VIEW3D = 0
    VIEW2D = 1

class WidgetModel(QObject):
    view_mode_changed = Signal(ViewMode)
    stars_changed = Signal(dict)
    camera_position_changed = Signal(dict)
    update_graticule = Signal(bool)
    
    def __init__(self):
        super().__init__()

        self._view_mode = ViewMode.VIEW2D
        self.view_mode_changed.emit(self._view_mode)
        self._stars = {}
        self._camera_position = {}
        self._show_camera = False
        self._show_camera = False
        self._roll = 0
        self._ar = 0
        self._dec = 0
        self.camera = Camera()
    
    @property
    def stars(self):
        return self._stars

    @stars.setter
    def stars(self, value):
        self._stars = value
        self.stars_changed.emit(value)
    
    @property
    def camera(self):
        return self._camera

    @camera.setter
    def camera(self, value):
        self._camera = value

    @property
    def camera_position(self) -> dict:
        return self._camera_position
    
    @camera_position.setter
    def camera_position(self, value):
        self._camera_position = value
        self.camera_position_changed.emit(value)
    
    @property
    def view_mode(self):
        return self._view_mode
    
    @view_mode.setter
    def view_mode(self, value):
        self._view_mode = value
        self.view_mode_changed.emit(value)
    
    @property
    def show_camera(self):
        return self._show_camera
    
    @show_camera.setter
    def show_camera(self, value):
        self._show_camera = value
        self.camera_position_changed.emit(self.camera_position)
    
    @property
    def show_graticule(self):
        return self._show_graticule
    
    @show_graticule.setter
    def show_graticule(self, value):
        self._show_graticule = value
        self.update_graticule.emit(value)

    @property
    def roll(self):
        return self._roll
    
    @roll.setter
    def roll(self, value):
        self._roll = value
    
    @property
    def ar(self):
        return self._ar
    
    @ar.setter
    def ar(self, value):
        self._ar = value
    
    @property
    def dec(self):
        return self._dec
    
    @dec.setter
    def dec(self, value):
        self._dec = value