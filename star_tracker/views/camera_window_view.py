from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

from model.camera_window_model import CameraWindowModel
from controllers.camera_window_ctrl import CameraWindowController
from views.CameraWindow_ui import Ui_CameraWindow

class CameraWindowView(QWindow, Ui_CameraWindow):
    def __init__(self,  model : CameraWindowModel, controller : CameraWindowController, *args, obj=None, **kwargs):
        super(CameraWindowView, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self._model = model
        self._controller = controller
        