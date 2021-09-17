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
    
    @Slot(bool)
    def change_view_plot_mode(self, value):
        self._model.view_plot_mode = value
    
    @Slot(bool)
    def load_stars_dialog(self, value):
        self._model.load_stars_file = value
    
    @Slot(bool)
    def load_movements_dialog(self, value):
        self._model.load_movements_file = value
    
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