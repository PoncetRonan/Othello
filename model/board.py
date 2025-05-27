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
        self._grid[3, 3].add_pawn(Pawn('white'))
        self._grid[3, 4].add_pawn(Pawn('black'))
        self._grid[4, 3].add_pawn(Pawn('black'))
        self._grid[4, 4].add_pawn(Pawn('white'))
        self._score_white = 0
        self._score_black = 0

    def get_grid(self):
        return self._grid
    
    @property
    def score_white(self):
        return self._score_white
    
    @property
    def score_black(self):
        return self._score_black

    def _is_valid_move(self, neighbor, case, current_player):
        result = False
        # case and neighbor on same row; neighbore is on the right of case
        if ((neighbor[0] == case[0]) and (neighbor[0] < case[0])):
            for j in range(case[1] + 1, 8):
                if self._grid[case[0], j].state == 'occupied':
                    if self._grid[case[0], j].pawn.color == current_player:
                        result = True
                        break
        # case and neighbor on same row; neighbore is on the left of case
        if ((neighbor[0] == case[0]) and (neighbor[0] > case[0])):
            for j in range(0, case[1]):
                if self._grid[case[0], j].state == 'occupied':
                    if self._grid[case[0], j].pawn.color == current_player:
                        result = True
                        break
        # case and neighbor on same column; neighbor is above case
        if ((neighbor[1] == case[1]) and (neighbor[1] > case[1])):
            for i in range(case[0] + 1, 8):
                if self._grid[i, case[1]].state == 'occupied':
                    if self._grid[i, case[1]].pawn.color == current_player:
                        result = True
                        break
        # case and neighbor on same column; neighbor is below case
        if ((neighbor[1] == case[1]) and (neighbor[1] < case[1])):
            for i in range(0, case[0]):
                if self._grid[i, case[1]].state == 'occupied':
                    if self._grid[i, case[1]].pawn.color == current_player:
                        result = True
                        break
        # case and neighbor on diagonal; neighbor is above and to the left of case



    def verify_possible_move(self, current_player):
        possible_moves = []
        for i in range(8):
            for j in range(8):
                if ((self._grid[i, j].state == 'occupied') and (self._grid[i, j].pawn.color != current_player)):
                    for neighbor in self._grid[i, j].neighbors:
                        if ((neighbor.state == 'empty') and (self._is_valid_move(neighbor, (i,j), current_player))):
                            possible_moves.append(neighbor)
        return possible_moves
                

    def play_pawn(self):
        pass

    def update_board(self):
        pass

    def calculate_move(self):
        pass

    def calculate_score(self):
        """
        Calculates and updates the current score for both players.

        Iterates through the game board and counts the number of pawns for each player.
        For each occupied cell, the pawn's color is checked and the corresponding score 
        (white or black) is incremented. The results are stored in the instance variables 
        `_score_white` and `_score_black`.

        Returns:
            None
        """
        
        score_white = 0
        score_black = 0

        for row in self._grid: # loop over the rows on the board
            for case in row:
                if case.state == "occupied": # if there is a pawn, check the color
                    color = case.pawn.color
                    
                    if color == "white":
                        score_white += 1
                    elif color == "black":
                        score_black += 1

        self._score_white = score_white
        self._score_black = score_black

