from PySide2.QtCore import QObject, Signal

class Model(QObject):
    stars_input_file_changed = Signal(str)
    view_plot_mode_changed = Signal(bool)

    @property
    def stars_input_file(self):
        return self._stars_input_file

    @stars_input_file.setter
    def stars_input_file(self, value):
        self._stars_input_file = value
        self.stars_input_file_changed.emit(value)
    
    @property
    def view_plot_mode(self):
        return self._view_plot_mode

    @view_plot_mode.setter
    def view_plot_mode(self, value):
        self._view_plot_mode = value
        self.view_plot_mode_changed.emit(value)
        print(value)
    
    def __init__(self):
        super().__init__()

        self._stars_input_file = ''
        self._view_plot_mode = False
        