from os import error
from PySide2.QtCore import QObject, Signal
from enum import Enum

class ViewMode(Enum):
    VIEW3D = 0
    VIEW2D = 1

class WidgetModel(QObject):
    update_all = Signal(ViewMode)
    update_camera = Signal(dict)

    def __init__(self):
        super().__init__()

        self._stars = {}
        self._camera_position = {}
        self._view_mode = ViewMode.VIEW2D
        self._show_camera = False
        self._roll = 0
        self._ar = 0
        self._dec = 0
        self.update_all.emit(ViewMode.VIEW2D)
    
    @property
    def stars(self):
        return self._stars

    @stars.setter
    def stars(self, value):
        self._stars = value
        if not value == {}:
            self.update_all.emit(self.view_mode)
    
    @property
    def camera_position(self) -> dict:
        return self._camera_position
    
    @camera_position.setter
    def camera_position(self, value):
        self._camera_position = value
        self.update_camera.emit(value)
    
    @property
    def view_mode(self):
        return self._view_mode
    
    @view_mode.setter
    def view_mode(self, value):
        self._view_mode = value
        self.update_all.emit(value)
    
    @property
    def show_camera(self):
        return self._show_camera
    
    @show_camera.setter
    def show_camera(self, value):
        self._show_camera = value
        self.update_camera.emit(self._camera_position)
    
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