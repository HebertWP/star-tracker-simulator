import sys
from PySide2.QtWidgets import QApplication

#my models import
from model.main_model import MainModel
from model.widget_model import WidgetModel

#my controllers import
from controllers.main_ctrl import MainController
from controllers.widget_ctrl import WidgetController

#my views import
from views.main_window_view import MainWindow
from views.widgets.widget_view import Widget

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        
        self._main_model = MainModel()
        self._main_controller = MainController(self._main_model)
        self._main_view = MainWindow(self._main_model, self._main_controller)
        
        self._widget_model = WidgetModel()
        self._widget_controller = WidgetController(self._main_model,self._widget_model)
        self._widget_view = self._main_view.view_plot_widget
        self._widget_view.model = self._widget_model
        
        self._main_model.load()
        self._main_view.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())