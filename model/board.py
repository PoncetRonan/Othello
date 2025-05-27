import numpy as np
from .case import Case
from .pawn import Pawn
from .player import Player

class Board:
    def __init__(self):
        #Initialize an 8x8 grid of Case objects
        self._grid = np.empty((8, 8), dtype=Case)
        for i in range(8):
            for j in range(8):
                self._grid[i, j] = Case(i, j)
        # Place the initial pawns on the board   
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
      
    def define_direction(self, case, move):
        """
        Determines the direction of the case relative to the move.
        Args:
            move (tuple): Coordinates of the move (row, col).
            case (tuple): Coordinates of the case (row, col).
        Returns:
            str: Direction of the move ('up', 'down', 'left', 'right', 'up-left', 'up-right', 'down-left', 'down-right').
        """
        if case[0] == move[0] - 1:
            if case[1] == move[1] - 1:
                direction = 'up-left'
            elif case[1] == move[1] + 1:
                direction = 'up-right'
            else:
                direction = 'up'
        elif case[0] == move[0] + 1:
            if case[1] == move[1] - 1:
                direction = 'down-left'
            elif case[1] == move[1] + 1:
                direction = 'down-right'
            else:
                direction = 'down'
        elif case[0] == move[0]:
            if case[1] == move[1] - 1:
                direction = 'left'
            elif case[1] == move[1] + 1:
                direction = 'right'
            else:
                direction = None
        return direction
    
    def increment_direction(self, move, direction):
        i = move[0]
        j = move[1]
        if i > 0 and i < 7 and j > 0 and j < 7:
            valid = True
            if direction == 'up':
                i -= 1
            elif direction == 'down':
                i += 1
            elif direction == 'left':
                j -= 1
            elif direction == 'right':
                j += 1
            elif direction == 'up-left':
                i -= 1
                j -= 1
            elif direction == 'up-right':
                i -= 1
                j += 1
            elif direction == 'down-left':
                i += 1
                j -= 1
            elif direction == 'down-right':
                i += 1
                j += 1
        else:
            valid = False
        return valid, (i, j)
    
    def is_valid_move(self, move, direction, color):
        result = False
        valid, (i, j) = self.increment_direction(i, j, direction)
        while ((valid) & (self._grid[i, j].state == 'occupied')):
            if self._grid[i, j].pawn.color == color:
                result = True
                break
            valid, (i, j) = self.increment_direction(i, j, direction)
        return result

    def verify_possible_move(self, current_player):
        possible_moves = []
        for i in range(8):
            for j in range(8):
                if ((self._grid[i, j].state == 'occupied') and (self._grid[i, j].pawn.color != current_player)):
                    for move in self._grid[i, j].neighbors:
                        direction = self.define_direction(move, (i,j))
                        if ((move.state == 'empty') and (self.is_valid_move(move, direction, current_player))):
                            possible_moves.append(move)
        return list(set(possible_moves))  # Remove duplicates
                
    def play_pawn(self, row, col, current_player):
        self._grid[row, col].add_pawn(Pawn(current_player))

    def update_board(self, row, col, current_player):
        self.calculate_move(row, col, current_player)
        self.calculate_score()

    def calculate_move(self):
        pass

    def calculate_score(self):
        pass