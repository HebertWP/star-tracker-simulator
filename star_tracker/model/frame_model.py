from os import error
from PySide2.QtCore import QObject, Signal
from enum import Enum

class FrameModel(QObject):
    file_name_changed = Signal(str)
    show_play_button_changed = Signal(bool)
    playing_changed = Signal(bool)
    finished = Signal()
    play_progress_changed = Signal(float)

    def __init__(self):
        super().__init__()
        self._file_name = ''
        self._playing = False
        self.show_play_button = False
        self.play_progress = 0
        self.play_progress = 0
    
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
        self.file_name_changed.emit(value)
    
    @property
    def file(self):
        return self._file
    @file.setter
    def file(self,value):
        self._file = value
    
    @property
    def playing(self):
        return self._playing
    @playing.setter
    def playing(self, value):
        self._playing = value
        self.playing_changed.emit(value)
    
    @property
    def show_play_button(self):
        return self._show_play_button
    @show_play_button.setter
    def show_play_button(self,value):
        self._show_play_button = value
        self.show_play_button_changed.emit(value)

    @property
    def play_progress(self):
        return self._play_progress
    @play_progress.setter
    def play_progress(self,value):
        self._play_progress = value
        self.play_progress_changed.emit(value)