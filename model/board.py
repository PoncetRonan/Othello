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
        self._score = 0

    def get_grid(self):
        return self._grid
        
    def get_score(self):
        return self._score

    def _is_valid_move(self, neighbor, case, current_player):
        result = False
        # case and neighbor on same row; neighbore is on the right of case
        if ((neighbor[0] == case[0]) and (neighbor[0] < case[0])):
            for j in range(case[1] + 1, 8):
                while self._grid[case[0], j].state == 'occupied':
                    if self._grid[case[0], j].pawn.color == current_player:
                        result = True
                        break

        # case and neighbor on same row; neighbore is on the left of case
        if ((neighbor[0] == case[0]) and (neighbor[0] > case[0])):
            for j in range(0, case[1]):
                while self._grid[case[0], j].state == 'occupied':
                    if self._grid[case[0], j].pawn.color == current_player:
                        result = True
                        break

        # case and neighbor on same column; neighbor is above case
        if ((neighbor[1] == case[1]) and (neighbor[1] > case[1])):
            for i in range(case[0] + 1, 8):
                while self._grid[i, case[1]].state == 'occupied':
                    if self._grid[i, case[1]].pawn.color == current_player:
                        result = True
                        break

        # case and neighbor on same column; neighbor is below case
        if ((neighbor[1] == case[1]) and (neighbor[1] < case[1])):
            for i in range(0, case[0]):
                while self._grid[i, case[1]].state == 'occupied':
                    if self._grid[i, case[1]].pawn.color == current_player:
                        result = True
                        break

        # case and neighbor on diagonal; neighbor is below and to the right of case
        if ((neighbor[0] > case[0]) and (neighbor[1] > case[1])):
            i = case[0] - 1
            j = case[1] - 1
            while ((i >= 0) and (j >= 0)):
                while self._grid[i, j].state == 'occupied':
                    if self._grid[i, j].pawn.color == current_player:
                        result = True
                        break
                i -= 1
                j -= 1

        # case and neighbor on diagonal; neighbor is below and to the left of case
        if ((neighbor[0] > case[0]) and (neighbor[1] < case[1])):
            i = case[0] - 1
            j = case[1] + 1
            while ((i >= 0) and (j < 8)):
                while self._grid[i, j].state == 'occupied':
                    if self._grid[i, j].pawn.color == current_player:
                        result = True
                        break
                i -= 1
                j += 1
        
        # case and neighbor on diagonal; neighbor is above and to the right of case
        if ((neighbor[0] < case[0]) and (neighbor[1] > case[1])):
            i = case[0] + 1
            j = case[1] - 1
            while ((i < 8) and (j >= 0)):
                while self._grid[i, j].state == 'occupied':
                    if self._grid[i, j].pawn.color == current_player:
                        result = True
                        break
                i += 1
                j -= 1




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
        pass