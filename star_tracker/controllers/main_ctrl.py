import webbrowser

from PySide2.QtCore import QObject, Slot
from models.main_model import MainModel, ViewMode
from views.about_view import About
from modules.basic import deg2rad

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
        
    @Slot(str)
    def save_frame_name(self, value):
        self._model.take_photo(value)
    
    @Slot(bool)
    def change_view_plot_mode(self, value):
        if(value):
            self._model.view_plot_mode = ViewMode.VIEW3D
        else:
            self._model.view_plot_mode = ViewMode.VIEW2D    
    
    @Slot(bool)
    def change_camera_view(self, value):
        self._model.change_camera_view = value
    
    @Slot(bool)
    def change_graticule_view(self, value):
        self._model.change_graticule_view = value
    @Slot(bool)
    def change_stars_view(self, value):
        self._model.change_stars_view = value
    @Slot(bool)
    def change_view_simulation(self, value):
        print("Not implemented")

    @Slot(float)
    def change_roll(self, value):
        #value = deg2rad(value)
        #print("aqui")
        self._model.roll = value
    
    @Slot(float)
    def change_ar(self, value):
        #value = deg2rad(value)
        self._model.ar = value
    
    @Slot(float)
    def change_dec(self, value):
        #value = deg2rad(value)
        self._model.dec = value
    
    @Slot(bool)
    def open_source(self, value):
        url = "https://github.com/HebertWP/star_tracker"
        webbrowser.open(url)
    
    @Slot(object)
    def open_about_dialog(self, value):
        dlg = About()
        dlg.exec_()