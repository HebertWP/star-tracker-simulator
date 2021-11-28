from os import error
from PySide2.QtCore import SIGNAL, QObject, Signal
import json
from enum import Enum
from modules.camera import Camera
from modules.stars import Stars

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
        
        self._change_camera_view = False
        self._change_graticule_view = False

        self._roll = 0.0
        self._ar = 0.0
        self._dec = 0.0

        self._load_stars_file = False
        self._load_movements_file = False
        self._manual_controls_enable = True

    def load(self):
        try:
            f = open('./data/save.json','r')
            data = json.load(f)
        except FileNotFoundError:
            return
        
        self._stars.load_catalog(data['Stars input file'])
        self._camera.stars.load_catalog(data['Stars input file'])
        self._stars.show = data['Show Stars']
        self.stars_changed.emit(self._stars.getDict(),self._stars.show)
        
        if data['view_plot_mode']:
            self.view_plot_mode = ViewMode.VIEW3D
        else:
            self.view_plot_mode = ViewMode.VIEW2D
        self.movements_input_file = data['movements_input_file']
        
        """
            self.camera_input_file = data['camera_input_file']
            
            self.change_camera_view = data['show_camera']
            self.change_graticule_view = data['show_graticule']

            self.roll = data['roll']
            self.dec = data['dec']
            self.ar = data['ar']
        """

    def save(self):
        data = {}
        data['Stars input file'] = self._stars.input_file
        data['Show Stars'] = self._stars.show
        
        data['show_graticule'] = self._change_graticule_view
        
        data['roll'] = self._roll
        data['ar'] = self._ar
        data['dec'] = self._dec

        data['movements_input_file'] = self._movements_input_file
        data['Camera input file'] = self._camera.input_file
        
        if self._view_plot_mode == ViewMode.VIEW3D:
            data['view_plot_mode'] = True
        else:
            data['view_plot_mode'] = False    
        
        data['show_camera'] = self._change_camera_view

        file = open('./data/save.json','w')
        json.dump(data,file)

    camera_position_changed = Signal(dict)
    
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
    camera_input_file_changed = Signal(str)
    @property
    def camera_input_file(self):
        return self._camera_input_file
    @camera_input_file.setter
    def camera_input_file(self,value):
        self._camera_input_file = value
        self._camera.config = value
        self.camera_input_file_changed.emit(value)
    
        if value == '':
            self.camera_name = "No Loaded File"
        else:
            v = value.split(sep="/")
            self.camera_name = v[-1]    
        self.save()
    camera_name_changed = Signal(str)
    @property
    def camera_name(self):
        return self._camera_name
    @camera_name.setter
    def camera_name(self,value):
        self._camera_name = value
        self.camera_name_changed.emit(value)

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
        self.save()
        self.view_plot_mode_changed.emit(value)
    
    ################################################################
    # Show or hide camera
    # Show: True
    # Hide: False
    ################################################################
    show_camera_changed = Signal(bool)
    @property
    def change_camera_view(self):
        return self._change_camera_view
    @change_camera_view.setter
    def change_camera_view(self,value):
        self._change_camera_view = value
        self.save()
        self.show_camera_changed.emit(value)
    
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
        return self._roll
    @roll.setter
    def roll(self, value):
        self._roll = value
        self.save()
        self._camera.roll = value
        self.roll_changed.emit(value)

    ################################################################
    # ar in degrees
    ################################################################
    ar_changed = Signal(float)
    @property
    def ar(self):
        return self._ar
    @ar.setter
    def ar(self, value):
        self._ar = value
        self.save()
        self._camera.ar = value
        self.ar_changed.emit(value)
    
    ################################################################
    # dec in degrees
    ################################################################
    dec_changed = Signal(float)
    @property
    def dec(self):
        return self._dec
    @dec.setter
    def dec(self, value):
        self._dec = value
        self.save()
        self._camera.dec = value
        self.dec_changed.emit(value)
        
    @property
    def manual_controls_enable(self):
        return self._manual_controls_enable
    @manual_controls_enable.setter
    def manual_controls_enable(self,value):
        self._manual_controls_enable = value
        self.manual_controls_enable_chaged.emit(value)
    
    @property
    def camera_position(self) -> dict:
        return self._camera_position
    
    @camera_position.setter
    def camera_position(self, value):
        self._camera_position = value
        self.camera_position_changed.emit(value)
    
    @property
    def show_camera(self):
        return self._show_camera
    
    @show_camera.setter
    def show_camera(self, value):
        self._show_camera = value
        self.camera_position_changed.emit(self.camera_position)

    def take_photo(self,output_file):
        self._camera.take_frame(output_file)