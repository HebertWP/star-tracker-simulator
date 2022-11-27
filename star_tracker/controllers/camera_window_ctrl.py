import webbrowser

from PySide2.QtCore import QObject, Slot
from models.camera_window_model import CameraWindowModel
from models.main_model import MainModel
from views.about_view import About

class CameraWindowController(QObject):
    def __init__(self, main_model : MainModel, camera_model : CameraWindowModel):
        super().__init__()

        self._camera_model = camera_model
        self._main_model = main_model