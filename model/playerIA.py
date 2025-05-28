from .player import Player 
from .board import Board

class PlayerIA(Player):
    """ player IA that calculate the next move by itself"""
    def __init__(self, name, color='white'):
        super().__init__(name, color)
        self.mode_play = "random"
    
    def calculate_next_move(self, board:Board, list_possible_moves):
        
        if self.mode_play == "random":
            next_move = self.select_random_move(list_possible_moves)
        else: 
            next_move = self.calculate_move_minimax()

        return next_move

    @property
    def type(self):
        return "ia"
    
    def select_random_move(self, list_possible_moves):
        pass

    def calculate_move_minimax(self):
        pass