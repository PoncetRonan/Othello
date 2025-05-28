class Player:
    def __init__(self,name, color='white', type='human'):
        self.color=color
        self.name=name
        self.type=type
    @property
    def type(self):
        return self._type
    
    @type.setter
    def set_type(self, type):
        """A player can be humain or ia"""
        if type in ['human', 'ia']:
            self._type=type
        else:
            raise ValueError(f"type {type} is not a valide value can be 'humain' or 'ia'")
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def set_color(self, color):
        """A player play a color ('white', 'black') during the actual game play"""
        if color in ['white', 'black']:
            self._color=color
        else:
            raise ValueError(f"dame F*&! color {color} is not a valide value use 'white' or 'black'")
        
    @property
    def name (self):
        return self._name
    
    @name.setter
    def set_name(self, name):
        self._name=name