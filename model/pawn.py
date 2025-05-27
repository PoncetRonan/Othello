class Pawn:
    """ definition of an othello pawn that can have white or black color"""
    def __init__(self, color):
        if color in ['white', 'black']:
            self._color=color
        else:
            raise ValueError(f"dame F*&! color {color} is not a valide value use 'white' or 'black'")
    
    @property
    def color(self):
        """ color geter the @ property let use it as an attribute (self.color call automatically self.color())"""
        return self._color
    
    def swap_color(self):
        """Change the color of the pawn (swap the pawn)"""
        if self.color == 'white':
            self._color= 'black'
        else:
            self._color= 'white'
    
    def __str__(self):
        valeur='⚫'
        if self.color == 'white':
            valeur='⚪'
        return valeur
    