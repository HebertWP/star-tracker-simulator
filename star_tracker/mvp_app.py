import sys
from PySide2.QtWidgets import QApplication

#my models import
from model.main_model import MainModel
from model.frame_model import FrameModel
from model.camera_window_model import CameraWindowModel

#my controllers import
from controllers.main_ctrl import MainController
from controllers.frame_ctrl import FrameController
from controllers.camera_window_ctrl import CameraWindowController

#my views import
from views.main_window_view import MainWindow
from views.widgets.widget_view import Widget
from views.frame_view import AutomaticMovements
from views.camera_window_view import CameraWindowView 

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        
        self._main_model = MainModel()
        self._main_controller = MainController(self._main_model)
        self._main_view = MainWindow(self._main_model, self._main_controller)
        
        self._widget_view = self._main_view.view_plot_widget
        self._widget_view.model = self._main_model
        
        self._frame_model = FrameModel()
        self._frame_controller = FrameController(self._main_model, self._frame_model)
        self._frame_view = self._main_view.view_automatic_control_frame
        self._frame_view.model  = self._frame_model
        self._frame_view.controller = self._frame_controller

        self._camera_window_model = CameraWindowModel()
        self._camera_window_controller = CameraWindowController(self._main_model, self._camera_window_model)
        #self._camera_window_view = CameraWindow(self._camera_window_model, self._camera_window_controller)

        self._main_model.load()
        self._main_view.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())