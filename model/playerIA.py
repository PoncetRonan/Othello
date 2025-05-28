from .player import Player 
from .board import Board

class PlayerIA(Player):
    """ player IA that calculate the next move by itself"""
    def __init__(self, name, color='white'):
        super().__init__(name, color)
    
    def calculate_next_move(board:Board):
        pass

    @property
    def type(self):
        return "ia"