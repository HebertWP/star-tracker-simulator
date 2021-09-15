from os import error
from PySide2.QtCore import QObject, Signal
from enum import Enum

class ViewMode(Enum):
    VIEW3D = 0
    VIEW2D = 1

class WidgetModel(QObject):
    update_view = Signal(dict)
    
    def __init__(self):
        super().__init__()

        self._stars = {}
        self._mode = ViewMode.VIEW2D
    
    @property
    def stars(self):
        return self._stars

    @stars.setter
    def stars(self, value):
        if value == {}:
            return
        self._stars = value
        self._stars['mode'] = self._mode
        self.update_view.emit(self._stars)
    
    @property
    def mode(self):
        return self._mode
    
    @mode.setter
    def view_mode(self, value):
        self._mode = value
        if self._stars == {}:
            return
        self._stars['mode'] = value
        self.update_view.emit(self._stars)