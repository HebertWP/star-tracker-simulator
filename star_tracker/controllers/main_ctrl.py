from PySide2.QtCore import QObject, Slot

class MainController(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model

    @Slot(str)
    def change_stars_input_file(self, value):
        self._model.stars_input_file = value
    
    @Slot(bool)
    def change_view_plot_mode(self, value):
        self._model.view_plot_mode = value
    
    @Slot(bool)
    def load_stars_dialog(self, value):
        self._model.load_stars_file = value
    
    @Slot(float)
    def change_roll(self, value):
        self._model.roll = value
    
    @Slot(float)
    def change_ar(self, value):
        self._model.ar = value
    
    @Slot(float)
    def change_dec(self, value):
        self._model.dec = value
    