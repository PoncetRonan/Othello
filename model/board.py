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
            case (tuple): Coordinates of the case (row, col).
            move (tuple): Coordinates of the move (row, col).
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
        """
        Increments the coordinates of a move in a specified direction
        AND check that the incremented moves are within the board.
        The function returns a boolean indicating if the move is valid and the new coordinates.
        If the move is out of bounds, it returns the original coordinates.
        Args:
            move (tuple): Coordinates of the move (row, col).
            direction (str): Direction of the move ('up', 'down', 'left', 'right', 'up-left', 'up-right', 'down-left', 'down-right').
        Returns:
            tuple: A tuple containing a boolean indicating if the move is valid and the new coordinates (row, col).
        """
        i = move[0]
        j = move[1]
        valid = True
        if i >= 0 and i < 8 and j >= 0 and j < 8:
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
        if i < 0 or i >= 8 or j < 0 or j >= 8:
            valid = False
            i = move[0]
            j = move[1]
        return valid, (i, j)
    
    def is_valid_move(self, move, direction, color):
        """
        Checks if a move is valid according to the Othello rules.
        Args:
            move (tuple): Coordinates of the move (row, col).
            direction (str): Direction of the move ('up', 'down', 'left', 'right', 'up-left', 'up-right', 'down-left', 'down-right').
            color (str): Color of the pawn ('white' or 'black').
        Returns:
            bool: True if the move is valid, False otherwise.
        """
        result = False
        valid, (i, j) = self.increment_direction(move , direction)
        while ((valid) & (self._grid[i, j].state == 'occupied')):
            if self._grid[i, j].pawn.color == color:
                result = True
                break
            valid, (i, j) = self.increment_direction((i, j), direction)
        return result

    def verify_possible_move(self, current_player):
        """
        Verifies all possible moves for the current player.
        Iterates through the grid and checks each occupied cell for potential moves.
        Then checks if the move is valid according to the Othello rules.
        Args:
            current_player (str): Color of the current player ('white' or 'black').
        Returns:
            list: A list of tuples representing the coordinates of valid moves for the current player.
        """
        possible_moves = []
        for i in range(8):
            for j in range(8):
                if ((self._grid[i, j].state == 'occupied') and (self._grid[i, j].pawn.color != current_player)):
                    for k,l in self._grid[i, j].neighbors_coordinates():                        
                        direction = self.define_direction((i,j), (k,l))
                        if ((self._grid[k,l].state == 'empty') and (self.is_valid_move((k,l), direction, current_player))):
                            possible_moves.append((k,l))
        return list(set(possible_moves))  # Remove duplicates
                
    def play_pawn(self, row, col, current_player):
        """
        Places a pawn on the board at the specified row and column for the current player.
        Args:
            row (int): Row index where the pawn will be placed.
            col (int): Column index where the pawn will be placed.
            current_player (str): Color of the current player ('white' or 'black').
        Returns:
            None
        """
        self._grid[row, col].add_pawn(Pawn(current_player))

    def update_board(self, row, col, current_player):
        """
        Updates the board by swapping the colors of pawns that are turned over
        after a pawn is placed at the specified row and column for the current player.
        Then calculates the score for both players.
        Args:
            row (int): Row index where the pawn will be placed.
            col (int): Column index where the pawn will be placed.
            current_player (str): Color of the current player ('white' or 'black').
        Returns:
            None
        """
        pawn_to_turn = self.calculate_move(row, col, current_player)
        for (i, j) in pawn_to_turn:
            self._grid[i, j].pawn.swap_color()
        self.calculate_score()

    def calculate_move(self,row,col,color):
        pawn_to_turn=[]
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if i ==0 and j ==0:
                    continue
                try:
                    self._grid[i+row,j+col].pawn.color
                except:
                    continue    
                if (self._grid[i+row,j+col].pawn.color != color):
                    flag_pawn=False
                    n=1
                    while (n*i+row < 8) and (n*j+col < 8) and (n*i+row >-1) and (n*j+col > -1) and flag_pawn==False:                       
                        try:
                            self._grid[n*i+row,n*j+col].pawn.color
                        except:
                            flag_pawn=True
                            continue
                        if self._grid[n*i+row,n*j+col].pawn.color == color:                            
                            pawn_to_turn.extend((row + m*i, col + m*j) for m in range(1, n))
                            flag_pawn=True
                        else:
                            n=n+1
                else:
                    pass 
        return pawn_to_turn

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

    def __str__(self):
        return str(self.get_grid())
