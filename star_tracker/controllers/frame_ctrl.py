from PySide2.QtCore import QObject, QRunnable, QThreadPool, Slot
import time

#my models includes
from model.frame_model import *
from model.main_model import *

#my modules includes
from modules.loadfile import Movements
#import modules.basic as basic

class PlayingWorker(QRunnable):
    def __init__(self, obj : Movements, frame_model : FrameModel, main_model : MainModel):
        super().__init__()
        self._obj = obj
        self._frame_model = frame_model
        self._main_model = main_model
    
    @Slot()
    def run(self):
        self._main_model.manual_controls_enable = False
        self._obj.play()
        self._frame_model.play_progress = self._obj.progress
        while self._obj.playing and self._frame_model.playing:
            pos=self._obj.move()
            self._main_model.roll=pos["roll"]
            self._main_model.ar=pos["ar"]
            self._main_model.dec=pos["dec"]
            for i in range(2*pos["time"]):
                time.sleep(0.5)
                if not self._frame_model.playing:
                    break
            self._frame_model.play_progress = self._obj.progress
        self._obj.stop()
        self._frame_model.play_progress = self._obj.progress
        self._frame_model.playing = False
        self._main_model.manual_controls_enable = True
        
class FrameController(QObject):
    def __init__(self, main_model : MainModel, frame_model : FrameModel):
        super(QObject, self).__init__()
        
        self._treadpool = QThreadPool()
        self._main_model = main_model
        self._frame_model = frame_model

        self._main_model.movements_input_file_changed.connect(self.load_file)
    
    @Slot(str)
    def change_playing_mode(self, value):
        self._frame_model.playing = value
        if value:
            worker = PlayingWorker(self._frame_model.file,self._frame_model,self._main_model)
            self._treadpool.start(worker)
    
    def load_file(self, value):
        if value == '':
            self._frame_model.file_name = 'No loaded file'
            self._frame_model.show_play_button = False
            return
        v = value.split(sep="/")
        self._frame_model.file_name = v[-1]
        self._frame_model.file = Movements(value)
        self._frame_model.show_play_button = True