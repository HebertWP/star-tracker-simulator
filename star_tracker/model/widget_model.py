from os import error
from PySide2.QtCore import QObject, Signal
from enum import Enum

class ViewMode(Enum):
    VIEW3D = 0
    VIEW2D = 1

class WidgetModel(QObject):
    update = Signal()
    
    def __init__(self):
        super().__init__()

        self._stars = {}
        self._camera_position = {}
        self._mode = ViewMode.VIEW2D
        self._show_camera = False
        self._roll = 0
        self._ar = 0
        self._dec = 0
        self.update.emit()
    
    @property
    def stars(self):
        return self._stars

    @stars.setter
    def stars(self, value):
        self._stars = value
        if not value == {}:
            self.update.emit()
    
    @property
    def camera_position(self) -> dict:
        return self._camera_position
    
    @camera_position.setter
    def camera_position(self, value):
        self._camera_position = value
        self.update.emit()
    
    @property
    def mode(self):
        return self._mode
    
    @mode.setter
    def view_mode(self, value):
        self._mode = value
        self.update.emit()
    
    @property
    def show_camera(self):
        return self._show_camera
    
    @show_camera.setter
    def show_camera(self, value):
        self._show_camera = value
        self.update.emit()
    
    @property
    def roll(self):
        return self._roll
    
    @roll.setter
    def roll(self, value):
        self._roll = value
        self.update.emit()
    
    @property
    def ar(self):
        return self._ar
    
    @ar.setter
    def ar(self, value):
        self._ar = value
        self.update.emit()
    
    @property
    def dec(self):
        return self._dec
    
    @dec.setter
    def dec(self, value):
        self._dec = value
        self.update.emit()