from .player import Player 
from .board import Board
import random
import copy

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
            next_move = self.calculate_move_minimax(board, list_possible_moves, current_depth = 0, target_depth = 2, is_maximizing = True)

        return next_move

    @property
    def type(self):
        return "ia"
    
    def select_random_move(self, list_possible_moves):
        """Selects a returns a random move among the possible moves"""
        return random.choice(list_possible_moves)
    
    def minimax(self, board:Board, current_depth = 0, target_depth = 2, is_maximizing = False):
        # base case : target_depth reached
        if (current_depth == target_depth):
            if self.color == "white":
                return board._score_white - board._score_black
            else:
                return board._score_black - board._score_white          
        if is_maximizing:
            best_score = float("-inf")
            for move in board.verify_possible_move():
                # Create a deep copy of the board to simulate the move
                # This is necessary to avoid modifying the original board
                # as we do not have a method to reset the board
                board_ia = copy.deepcopy(board)
                # Place the move on the board   
                board_ia.play_pawn(move[0], move[1], self.color)
                board_ia.update_board(move[0], move[1], self.color)
                board_ia.calculate_score()
                # Recursively call minimax with the next depth and the minimizing player
                # is_maximizing=False because at next move we will check the best movement for the human
                score = self.minimax(board_ia, current_depth + 1, target_depth, False)
                # Update the best score
                best_score = max(score, best_score)
            return best_score
        else:
            # if it is the minimizing player's turn (human), we want to minimize the score
            best_score = float("inf")
            for move in board.verify_possible_move():
                # Create a deep copy of the board to simulate the move
                # This is necessary to avoid modifying the original board
                # as we do not have a method to reset the board
                board_ia = copy.deepcopy(board)
                # Place the move on the board   
                board_ia.play_pawn(move[0], move[1], self.color)
                board_ia.update_board(move[0], move[1], self.color)
                board_ia.calculate_score()
                # Recursively call minimax with the next depth and the minimizing player
                # is_maximizing=False because at next move we will check the best movement for IA
                score = self.minimax(board_ia, current_depth + 1, target_depth, True)
                # Reset the move
                self.board[move] = " "
                # Update the best score
                best_score = min(score, best_score)
            return best_score

    def calculate_move_minimax(self, board:Board, list_possible_moves, current_depth = 0, target_depth = 2, is_maximizing = True):  
        best_score = float("-inf")
        best_move = None
        for move in list_possible_moves:
            # Create a deep copy of the board to simulate the move
            # This is necessary to avoid modifying the original board
            # as we do not have a method to reset the board
            board_ia = copy.deepcopy(board)
            # Place the move on the board   
            board_ia.play_pawn(move[0], move[1], self.color)
            board_ia.update_board(move[0], move[1], self.color)
            board_ia.calculate_score()
            # Recursively call minimax with the next depth and the minimizing player
            score = self.minimax(board_ia, current_depth + 1, target_depth, False)
            # Update the best score
            if score > best_score:
               best_score = score
               best_move = move
        # Return the best move found
        return best_move

