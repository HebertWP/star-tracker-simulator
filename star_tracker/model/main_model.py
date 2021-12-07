import sys, os
from pathlib import Path
from PySide2.QtCore import SIGNAL, QObject, Signal
import json
from enum import Enum
from numpy import pi
try:
    from modules.camera import Camera
    from modules.stars import Stars
except ImportError:
    pass
class ViewMode(Enum):
    VIEW3D = 0
    VIEW2D = 1

class MainModel(QObject):

    def __init__(self):
        super().__init__()

        self._stars = Stars()
        self._camera = Camera()

        self._movements_input_file = ''

        self._view_plot_mode = ViewMode.VIEW2D
        
        self._change_graticule_view = False

        self._load_movements_file = False
        self._manual_controls_enable = True

    def load(self):
        try:
            pathname = os.path.dirname(sys.argv[0])
            path = os.path.abspath(pathname) + "/data/save.json"
            f = open(path,'r')
            data = json.load(f)
        except FileNotFoundError:
            return
        
        self._stars.load_catalog(data['Stars input file'])
        self._camera.stars.load_catalog(data['Stars input file'])
        self._stars.show = data['Show Stars']
        self.stars_changed.emit(self._stars.getDict(),self._stars.show)
        self.camera_input_file = data['Camera input file']

        if data['view_plot_mode']:
            self.view_plot_mode = ViewMode.VIEW3D
        else:
            self.view_plot_mode = ViewMode.VIEW2D
        self.movements_input_file = data['movements_input_file']
        self.change_camera_view = data['Show camera']
        self.change_graticule_view = data['Show graticule']
        self.roll = data['roll']
        self.dec = data['dec']
        self.ar = data['ar']

    def save(self):
        data = {}
        data['Stars input file'] = self._stars.input_file
        data['Show Stars'] = self._stars.show
        
        data['Show graticule'] = self._change_graticule_view
        
        data['roll'] = self._camera.roll * 180/pi
        data['ar'] = self._camera.ar * 180/pi
        data['dec'] = self._camera.dec * 180/pi

        data['movements_input_file'] = self._movements_input_file
        data['Camera input file'] = self._camera.input_file
        
        if self._view_plot_mode == ViewMode.VIEW3D:
            data['view_plot_mode'] = True
        else:
            data['view_plot_mode'] = False    
        
        data['Show camera'] = self._camera.show

        pathname = os.path.dirname(sys.argv[0])        
        Path(pathname + "/data").mkdir(parents=True, exist_ok=True)
        path = os.path.abspath(pathname) + "/data/save.json"
        file = open(path,'w')
        json.dump(data,file)
        print(path)
        
    manual_controls_enable_chaged = Signal(bool)

    ################################################################
    # Load stars file to simulation.
    # The file is a .csv file, with the following format:
    # |Numero de catalogacao(HIP)        |Ascensao  reta(alpha)              | Declinacao (delta)                  |Magnitude visual(V)                                 |
    # |Interger number represent the star|Float number from 0 to 260 degrees | Float number from -90 to 90 degrees |Float number representing the brightness of the star|
    # Note: the separation between values are done my commas
    ################################################################
    
    stars_changed = Signal(dict,bool)
    stars_input_file_changed = Signal(str)
    @property
    def stars_input_file(self):
        return self._stars.input_file
    @stars_input_file.setter
    def stars_input_file(self, value):
        try:
            self._stars.load_catalog(value)
            self._camera.stars.load_catalog(value)
        except FileNotFoundError:
            pass
        
        self.stars_changed.emit(self._stars.getDict(),self._stars.show)
        #self.stars_changed.emit(Stars().getDict())  
        self.stars_input_file_changed.emit(value)
        self.save()

    ################################################################
    # Load a pre set movements file.
    # The file is a .csv file, with the following format:
    # |time                                                       |roll                    |dec                    |ar                    |
    # |time in seconds that the simulation will keep this position|roll position in degrees|dec position in degrees|ar position in degrees| 
    # Note: the separation between values are in reality commas
    ################################################################
    movements_input_file_changed = Signal(str)
    @property
    def movements_input_file(self):
        return self._movements_input_file
    @movements_input_file.setter
    def movements_input_file(self, value):
        self._movements_input_file = value
        self.save()
        self.movements_input_file_changed.emit(value)
    
    ################################################################
    # A file with Characteristics of Camera.
    # The file is a json file, with the following format:
    #   {
    #       "ang": "interger number in degrees",
    #       "w": camera width in pixels,
    #       "h": camera height in pixels
    #   }
    # Example:
    #   {
    #       "ang": 30,
    #       "w": 1280,
    #       "h": 720
    #   }
    ################################################################
    camera_auxiliary_view_changed = Signal(dict, dict, bool)
    @property
    def camera_input_file(self):
        return self._camera.input_file
    @camera_input_file.setter
    def camera_input_file(self,value):
        try:
            self._camera.config = value
            data_3D = {'3D':self._camera.position_dict, '3D_pos':self._camera.coordinates}
            data_2D = self._camera.position_dict_spherical
            self.camera_auxiliary_view_changed.emit(data_3D, data_2D,self._camera.show)            
        except FileNotFoundError:
            pass   
        self.save()

    ################################################################
    # Show or hide camera
    # Show: True
    # Hide: False
    ################################################################
    @property
    def change_camera_view(self):
        return self._camera.show
    @change_camera_view.setter
    def change_camera_view(self,value):
        self._camera.show = value
        data_3D = {'3D':self._camera.position_dict, '3D_pos':self._camera.coordinates}
        data_2D = self._camera.position_dict_spherical
        self.camera_auxiliary_view_changed.emit(data_3D, data_2D,self._camera.show) 
        self.save()
    
    ################################################################
    # Set view mode 3D or 2D
    # 3D: True
    # 2D: False
    ################################################################
    view_plot_mode_changed = Signal(ViewMode)
    @property
    def view_plot_mode(self):
        return self._view_plot_mode
    @view_plot_mode.setter
    def view_plot_mode(self, value):
        self._view_plot_mode = value
        self.view_plot_mode_changed.emit(value)
        self.save()
    
    ################################################################
    # Show or hide graticule in pre view
    # Show: True
    # Hide: False
    ################################################################
    graticule_view_changed = Signal(bool)
    @property
    def change_graticule_view(self):
        return self._change_graticule_view
    @change_graticule_view.setter
    def change_graticule_view(self,value):
        self._change_graticule_view = value
        self.save()
        self.graticule_view_changed.emit(value)
    
    @property
    def change_stars_view(self):
        return self._stars.show
    @change_stars_view.setter
    def change_stars_view(self, value):
        self._stars.show = value
        self.stars_changed.emit(self._stars.getDict(),self._stars.show)
        self.save()
        
    ################################################################
    # roll in degrees
    ################################################################
    roll_changed = Signal(float)
    @property
    def roll(self):
        return self._camera.roll * 180/pi
    @roll.setter
    def roll(self, value):
        self._camera.roll = value *pi/180
        self.roll_changed.emit(value)
        data_3D = {'3D':self._camera.position_dict, '3D_pos':self._camera.coordinates}
        data_2D = self._camera.position_dict_spherical
        self.camera_auxiliary_view_changed.emit(data_3D, data_2D,self._camera.show)
        self.save()
    
    ################################################################
    # ar in degrees
    ################################################################
    ar_changed = Signal(float)
    @property
    def ar(self):
        return self._camera.ar * 180/pi
    @ar.setter
    def ar(self, value):
        self._camera.ar = value * pi/180
        self.ar_changed.emit(value)
        data_3D = {'3D':self._camera.position_dict, '3D_pos':self._camera.coordinates}
        data_2D = self._camera.position_dict_spherical
        self.camera_auxiliary_view_changed.emit(data_3D, data_2D,self._camera.show)
        self.save()
    
    ################################################################
    # dec in degrees
    ################################################################
    dec_changed = Signal(float)
    @property
    def dec(self):
        return self._camera.dec * 180/pi
    @dec.setter
    def dec(self, value):
        self._camera.dec = value * pi/180
        self.dec_changed.emit(value)
        data_3D = {'3D':self._camera.position_dict, '3D_pos':self._camera.coordinates}
        data_2D = self._camera.position_dict_spherical
        self.camera_auxiliary_view_changed.emit(data_3D, data_2D,self._camera.show)
        self.save()
        
    @property
    def manual_controls_enable(self):
        return self._manual_controls_enable
    @manual_controls_enable.setter
    def manual_controls_enable(self,value):
        self._manual_controls_enable = value
        self.manual_controls_enable_chaged.emit(value)

    def take_photo(self,output_file):
        self._camera.take_frame(output_file)