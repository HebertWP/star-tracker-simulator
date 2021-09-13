import sys
from PySide2.QtWidgets import QApplication
from model.model import Model
from controllers.main_ctrl import MainController
from views.MainWindow import MainWindow

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = Model()
        self.main_controller = MainController(self.model)
        #self.main_view = MainWindow()
        self.main_view = MainWindow(self.model, self.main_controller)
        self.main_view.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())