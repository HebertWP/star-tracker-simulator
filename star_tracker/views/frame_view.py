from PySide2.QtWidgets import *
from models.frame_model import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from controllers.frame_ctrl import *

class AutomaticMovements(QFrame):
    
    def __init__(self, parent = None):

        QFrame.__init__(self, parent)
    
    @property
    def file(self):
        return self._file
    @file.setter
    def file(self,value):
        self._file = value
    
    @property
    def play_button(self):
        return self._play_button
    @play_button.setter
    def play_button(self,value):
        self._play_button = value
        #self._play_button.setObjectName(u"_play_button")
    
    @property
    def movement_play_progress_bar(self):
        return self._movement_play_progress_bar
    @movement_play_progress_bar.setter
    def movement_play_progress_bar(self,value):
        self._movement_play_progress_bar = value
        self.change_progress_bar(0)
    
    @property
    def model(self):
        return self._model
    @model.setter
    def model(self, value : FrameModel):
        self._model = value
        self.change_mode_view_icon(False)
        
        #events signal
        self._model.file_name_changed.connect(self.change_file_name)
        self._model.playing_changed.connect(self.change_mode_view_icon)
        self._model.show_play_button_changed.connect(self.hide_show_button)
        self._model.play_progress_changed.connect(self.change_progress_bar)
        
    @property
    def controller(self):
        return self._controller
    @controller.setter
    def controller(self, value : FrameController):
        self._controller = value
        
        #connect to controller
        self._play_button.clicked.connect(self._controller.change_playing_mode)

    def change_file_name(self,value):
        self._file.setText(value)
    
    def change_mode_view_icon(self,value):
        icon1 = QIcon()
        if value:
            icon1.addFile(u":/icon/icons/stop.png", QSize(), QIcon.Normal)
        else:
            icon1.addFile(u":/icon/icons/botao-play.png", QSize(), QIcon.Normal)
        self._play_button.setIcon(icon1)
        self._play_button.setIconSize(QSize(24, 24))
        self._play_button.setChecked(value)
    
    def hide_show_button(self,value):
        self._play_button.setVisible(value)
    
    def change_progress_bar(self,value):
        self._movement_play_progress_bar.setValue(value)