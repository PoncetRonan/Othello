import numpy as np
from .case import Case
from .pawn import Pawn
from .player import Player

class Board:
    def __init__(self):
        self._grid = np.empty((8, 8), dtype=object)
        for i in range(8):
            for j in range(8):
                self._grid[i, j] = Case(i, j)
        self._score = 0

    def get_grid(self):
        return self._grid
        
    def get_score(self):
        return self._score

    def verify_possible_move(self, current_player):
        for i in range(8):
            for j in range(8):
                pass
                

    def play_pawn(self):
        pass

    def update_board(self):
        pass

    def calculate_move(self):
        pass

    def calculate_score(self):
        pass