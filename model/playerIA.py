from .player import Player 
from .board import Board
import random

class PlayerIA(Player):
    """ player IA that calculate the next move by itself"""
    def __init__(self, name, color='white', mode_play = "random"):
        super().__init__(name, color)
        self.mode_play = mode_play
    
    def calculate_next_move(self, board:Board, list_possible_moves):
        """
        Input:
            board: an instance of Board() with the current state of the board
            list_possible_moves: a list of tuples [(1, 2), (3, 4),...] with possible moves

        Calculates the next move by either selcting a random move among the possible moves or
        by using the minimax algoritm to select the optimal move.

        Returns:
            The next move as a tuple (row, col)
        """
        
        if self.mode_play == "random":
            next_move = self.select_random_move(list_possible_moves)
        else: 
            next_move = self.calculate_move_minimax(board)

        return next_move

    @property
    def type(self):
        return "ia"
    
    def select_random_move(self, list_possible_moves):
        """Selects a returns a random move among the possible moves"""
        return random.choice(list_possible_moves)

    def calculate_move_minimax(self):
        pass