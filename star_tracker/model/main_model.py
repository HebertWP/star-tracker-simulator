from os import error
from PySide2.QtCore import QObject, Signal
import json

class MainModel(QObject):
    stars_input_file_changed = Signal(str)
    movements_input_file_changed = Signal(str)
    camera_input_file_changed = Signal(str)
    
    camera_name_changed = Signal(str)

    load_stars_file_changed = Signal()
    load_movements_file_changed = Signal()
    load_camera_file_changed = Signal()
    
    view_plot_mode_changed = Signal(bool)
    show_camera_changed = Signal(bool)
    graticule_view_changed = Signal(bool)

    roll_changed = Signal(float)
    ar_changed = Signal(float)
    dec_changed = Signal(float)
    manual_controls_enable_chaged = Signal(bool)

    @property
    def stars_input_file(self):
        return self._stars_input_file

    @stars_input_file.setter
    def stars_input_file(self, value):
        self._stars_input_file = value
        self.save()
        self.stars_input_file_changed.emit(value)
    
    @property
    def movements_input_file(self):
        return self._movements_input_file

    @movements_input_file.setter
    def movements_input_file(self, value):
        self._movements_input_file = value
        self.save()
        self.movements_input_file_changed.emit(value)
    
    @property
    def camera_input_file(self):
        return self._camera_input_file

    @camera_input_file.setter
    def camera_input_file(self,value):
        self._camera_input_file = value
        self.save()
        self.camera_input_file_changed.emit(value)

    @property
    def camera_name(self):
        return self._camera_name
    
    @camera_name.setter
    def camera_name(self,value):
        self._camera_name = value
        self.save()
        self.camera_name_changed.emit(value)
    
    @property
    def view_plot_mode(self):
        return self._view_plot_mode

    @view_plot_mode.setter
    def view_plot_mode(self, value):
        self._view_plot_mode = value
        self.save()
        self.view_plot_mode_changed.emit(value)
    
    @property
    def change_camera_view(self):
        return self._change_camera_view
    
    @change_camera_view.setter
    def change_camera_view(self,value):
        self._change_camera_view = value
        self.save()
        self.show_camera_changed.emit(value)
    
    @property
    def change_graticule_view(self):
        return self._change_graticule_view
    
    @change_graticule_view.setter
    def change_graticule_view(self,value):
        self._change_graticule_view = value
        self.save()
        self.graticule_view_changed.emit(value)
    
    @property
    def load_stars_file(self):
        return self._load_stars_file
    
    @load_stars_file.setter
    def load_stars_file(self, value):
        self._load_stars_file = value
        self.load_stars_file_changed.emit()
    
    @property
    def load_movements_file(self):
        return self._load_movements_file
    
    @load_movements_file.setter
    def load_movements_file(self, value):
        self._load_movements_file = value
        self.load_movements_file_changed.emit()
    
    @property
    def load_camera_file(self):
        return self._load_camera_file

    @load_camera_file.setter
    def load_camera_file(self, value):
        self._load_camera_file = value
        self.load_camera_file_changed.emit()

    @property
    def roll(self):
        return self._roll
    
    @roll.setter
    def roll(self, value):
        self._roll = value
        self.save()
        self.roll_changed.emit(value)

    @property
    def ar(self):
        return self._ar
    
    @ar.setter
    def ar(self, value):
        self._ar = value
        self.save()
        self.ar_changed.emit(value)
    
    @property
    def dec(self):
        return self._dec
    
    @dec.setter
    def dec(self, value):
        self._dec = value
        self.save()
        self.dec_changed.emit(value)
        
    @property
    def manual_controls_enable(self):
        return self._manual_controls_enable
    @manual_controls_enable.setter
    def manual_controls_enable(self,value):
        self._manual_controls_enable = value
        self.manual_controls_enable_chaged.emit(value)
        
    def __init__(self):
        super().__init__()

        self._stars_input_file = ''
        self._movements_input_file = ''
        self._camera_input_file = ''

        self._camera_name = 'No Loaded File'

        self._view_plot_mode = False
        self._load_stars_file = False
        self._change_camera_view = False
        self._change_graticule_view = False

        self._roll = 0.0
        self._ar = 0.0
        self._dec = 0.0
        
        self._load_movements_file = False
        self._manual_controls_enable = True

    def load(self):
        try:
            f = open('./data/save.json','r')
            data = json.load(f)
            
            self.stars_input_file = data['stars_input_file']
            self.movements_input_file = data['movements_input_file']
            self.camera_input_file = data['camera_input_file']

            self.camera_name = data['camera_name']    
            
            self.view_plot_mode = data['view_plot_mode']
            self.change_camera_view = data['show_camera']
            self.change_graticule_view = data['show_graticule']

            self.roll = data['roll']
            self.dec = data['dec']
            self.ar = data['ar']
        except FileNotFoundError:
            return
    
    def save(self):
        data = {}
        data['stars_input_file'] = self._stars_input_file
        data['movements_input_file'] = self._movements_input_file
        data['camera_input_file'] = self._camera_input_file
        data['camera_name'] = self._camera_name
        
        data['view_plot_mode'] = self._view_plot_mode
        data['show_camera'] = self._change_camera_view
        data['show_graticule'] = self._change_graticule_view
        
        data['roll'] = self._roll
        data['ar'] = self._ar
        data['dec'] = self._dec
        file = open('./data/save.json','w')
        json.dump(data,file)