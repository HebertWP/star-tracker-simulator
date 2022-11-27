from os import error
from PySide2.QtCore import QObject, Signal

class CameraWindowModel(QObject):
    
    def __init__(self):
        super().__init__()