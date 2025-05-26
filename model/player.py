class Player:
    def __init__(self,name, color='white'):
        self.color=color
        self.name=name
    
    @property
    def color(self):
        return self.color
    
    @color.setter
    def set_color(self, color):
        if color in ['white', 'black']:
            self._color=color
        else:
            raise ValueError(f"dame F*&! color {color} is not a valide value use 'white' or 'black'")
        
    @property
    def name (self):
        return self._name
    
    @name.setter
    def get_name(self, name):
        if name in ['Jerome', 'Ronan','Jip', 'Diletta']:
            self._name
        else:
            raise ValueError(f" {name} is not a known name in the group")