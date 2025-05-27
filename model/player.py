class Player:
    def __init__(self,name, color='white'):
        self.color=color
        self.name=name
    
    @property
    def color(self):
        return self.color
    
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
        if name in ['Jerome', 'Ronan', 'Jip', 'Diletta']:
            self._name=name
        else:
            raise ValueError(f"{name} is not a known name of the group")