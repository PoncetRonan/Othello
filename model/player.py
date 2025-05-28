class Player:
    def __init__(self,name, color='white'):
        self.color=color
        self.name=name

    @property
    def type(self):
        return "human"
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        """A player play a color ('white', 'black') during the actual game play"""
        if color in ['white', 'black']:
            self._color=color
        else:
            raise ValueError(f"dame F*&! color {color} is not a valide value use 'white' or 'black'")
        
    @property
    def name (self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name=name
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score=score


    def __str__(self):
        return f"{self.name} <{self.color}>"
        
