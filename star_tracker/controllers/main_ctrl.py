import webbrowser

from PySide2.QtCore import QObject, Slot
from model.main_model import MainModel
from views.about_view import About

class MainController(QObject):
    def __init__(self, model : MainModel):
        super().__init__()

        self._model = model

    @Slot(str)
    def change_stars_input_file(self, value):
        self._model.stars_input_file = value
    
    @Slot(str)
    def change_movements_input_file(self, value):
        self._model.movements_input_file = value
    
    @Slot(str)
    def change_camera_input_file(self, value):
        self._model.camera_input_file = value
        if value == '':
            self._model.camera_name = "No Loaded File"
        else:
            v = value.split(sep="/")
            self._model.camera_name = v[-1]    
    
    @Slot(str)
    def save_frame_name(self, value):
        self._model.frame_name = value
    
    @Slot(bool)
    def change_view_plot_mode(self, value):
        self._model.view_plot_mode = value
    
    @Slot(bool)
    def change_camera_view(self, value):
        self._model.change_camera_view = value
    
    @Slot(bool)
    def change_graticule_view(self, value):
        self._model.change_graticule_view = value
    
    @Slot(bool)
    def change_view_simulation(self, value):
        print("Not implemented")

    @Slot(float)
    def change_roll(self, value):
        self._model.roll = value
    
    @Slot(float)
    def change_ar(self, value):
        self._model.ar = value
    
    @Slot(float)
    def change_dec(self, value):
        self._model.dec = value
    
    @Slot(bool)
    def open_source(self, value):
        url = "https://github.com/HebertWP/star_tracker"
        webbrowser.open(url)
    
    @Slot(object)
    def open_about_dialog(self, value):
        dlg = About()
        dlg.exec_()