from model import Board
from view import Display

class Othello():
    def __init__(self, continue_game=True, current_player="black"):
        self._continue_game = continue_game

        if current_player in ["white", "black"]:
            self._current_player = current_player
        else:
            raise ValueError("Value is not valid. Valid values are: 'white', 'black'")
        
        self._num_blocked_players = 0
        self._possible_moves = None
        self._next_move = None

    @property
    def continue_game(self):
        return self._continue_game
    
    @property
    def num_blocked_players(self):
        return self._num_blocked_players

    def start_game(self):
        """Initialize a game of othello."""

        # Print welcome message
        Display.welcome()

        # Initialize board
        board = Board()


    def play_game(self):
        """
        Executes a single turn of the game.

        This method determines the next player, calculates their move,
        applies the move to the game board, and displays the current game state.
        """

        # Determine next player
        self._current_player = self.determine_next_player()

        if self.num_blocked_players < 2:
            # Determine the next move
            self._next_move = self.determine_next_move()

            # Play the move: place pawn and update board
            self.make_move()

            # Display status
            self.display_current_state()


    def determine_next_player(self):
        """
        Determines which player should take the next turn.

        Alternates between "white" and "black" players and checks for available moves.
        If a player has no possible moves, they are considered blocked, and the method 
        attempts to select the other player. The method keeps track of how many players 
        are blocked and stops when either a player with valid moves is found or 
        both players are blocked.

        Returns:
            str: The player ("white" or "black") who will take the next turn.
        """

        previous_player = self._current_player 
        next_player = "unkown"

        while next_player == "unkown" and self.num_blocked_players < 2:

            if previous_player == "white":
                possible_player = "black"
            else:
                possible_player = "white"

            self._possible_moves = Board.verify_possible_move(possible_player) # Returns a list of tuples (row, col)

            if len(self._possible_moves) > 0:
                self._num_blocked_players = 0
                next_player = "know"
            else:
                previous_player = possible_player
                self._num_blocked_players += 1
        
        return possible_player


    def determine_next_move(self):
        """
        Determines 
        Returns:
            tuple: (row, col) coordinates of the next pawn to be played
        """

        return Display.input_play_move(self._possible_moves) # returns tuple with coordinates

    def make_move(self):
        pass

    def display_current_state(self):
        pass

    def end_game(self):
        pass
