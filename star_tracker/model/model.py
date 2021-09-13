from os import error
from PySide2.QtCore import QObject, Signal
import json

class Model(QObject):
    stars_input_file_changed = Signal(str)
    view_plot_mode_changed = Signal(bool)

    @property
    def stars_input_file(self):
        return self._stars_input_file

    @stars_input_file.setter
    def stars_input_file(self, value):
        self._stars_input_file = value
        self.save()
        self.stars_input_file_changed.emit(value)
    
    @property
    def view_plot_mode(self):
        return self._view_plot_mode

    @view_plot_mode.setter
    def view_plot_mode(self, value):
        self._view_plot_mode = value
        self.save()
        self.view_plot_mode_changed.emit(value)
    
    def __init__(self):
        super().__init__()

        self._stars_input_file = ''
        self._view_plot_mode = True

    def load(self):
        try:
            f = open('./data/save.json','r')
            data = json.load(f)
            self.view_plot_mode = data['view_plot_mode']
            self.stars_input_file = data['stars_input_file']
        except FileNotFoundError:
            return
    
    def save(self):
        data = {}
        data['view_plot_mode'] = self._view_plot_mode
        data['stars_input_file'] = self._stars_input_file
        file = open('./data/save.json','w')
        json.dump(data,file)
        