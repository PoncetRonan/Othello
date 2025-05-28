from model import Board, Player, PlayerIA, Color
from view import Display

class Othello():
    """
    A class representing the Othello (Reversi) game logic.

    This class manages the overall game flow including initializing the game,
    determining player turns, processing moves, updating the game board, and 
    handling the game end conditions. It interacts with a Board object (model)
    and a Display object (view) to separate logic and presentation.

    Attributes:
        _continue_game (bool): Indicates whether the game should continue or end.
        _current_player (str): The current player, either "black" or "white".
        _num_blocked_players (int): Counts how many players have no valid moves.
        _possible_moves (list): Stores possible moves for the current player as (row, col) tuples.
        _next_move (tuple): The coordinates of the next move to be made.
        _board (Board): An instance of the game board.
        _player_interface (Display): Interface for displaying messages and input.

    Raises:
        ValueError: If an invalid player is provided during initialization.
    """

    def __init__(self, continue_game=True, current_player="white"):
        self._continue_game = continue_game
        self.players={"white":None, "black":None}
                    #   Player("", color="white"),"black":Player("",color='black')}


        if current_player in ["white", "black"]:
            self._current_player = current_player
        else:
            raise ValueError(f"{current_player} is not a valid value. Valid values are: 'white', 'black'")
        
        self._num_blocked_players = 0 # Count how many players are blocked. If 2 -> end game
        self._possible_moves = None # Store all possible moves of the next player [(row, col), ...]
        self._next_move = None # Store the next move (row, col)
        self._board = None # Store an instance of Board
        self._player_interface = None # Store an instance of Display
    
    @property
    def players(self):
        return self._players
    
    @players.setter
    def players(self, players):
        self._players=players

    @property
    def continue_game(self):
        return self._continue_game
    
    @property
    def num_blocked_players(self):
        return self._num_blocked_players

    def reinitialize_game(self):
        self._current_player = "white"
        self._num_blocked_players = 0


    def start_game(self):
        """Initialize a game of othello."""
        
        # reset num_blocked players and current player
        self.reinitialize_game()

        # Initialize player interface
        self._player_interface = Display()
    

        # Print welcome message
        self._player_interface.clear_terminal()

        self._player_interface.welcome()
        if self._player_interface.play_against_IA():
            self.players={"white":Player("not def", color="white"),"black":PlayerIA("IA",color='black')}
            # self.players["white"]=
            self._player_interface.get_player_name(self.players["white"])
        else:
            self.players={"white":Player("not def", color="white"),"black":Player("Not def2",color='black')}
            self._player_interface.get_player_name(self.players["white"])
            self._player_interface.get_player_name(self.players["black"])

        # Initialize board
        self._board = Board()
        #self._player_interface.print_board(self._board._grid, [])
        

    def play_game(self):
        """
        Executes a single turn of the game.

        This method determines the next player, calculates their move,
        applies the move to the game board, and displays the current game state.
        """

        # Determine next player
        self._current_player = self.determine_next_player()
        self._player_interface.print_board(self._board.get_grid(), self._possible_moves)

        if self.num_blocked_players < 2: # else: game ends
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

            # Get a list of all possible moves
            self._possible_moves = self._board.verify_possible_move(possible_player) # Returns a list of tuples (row, col)
        
            if len(self._possible_moves) > 0: # possible_player can play and becoms the next_player
                self._num_blocked_players = 0
                next_player = possible_player   
            else: # no moves are possible, try to select the other player
                previous_player = possible_player
                self._num_blocked_players += 1
        
        return next_player


    def determine_next_move(self):
        """
        Determines the next move to be played.

        Returns:
            tuple: (row, col) coordinates of the next pawn to be played
        """
        player= self.players[self._current_player]
        if type(player) == PlayerIA:
            return player.calculate_next_move(self._board, self._possible_moves)
        else:
            return self._player_interface.input_play_move(self._possible_moves, self.players[self._current_player]) # returns tuple with coordinates

    def make_move(self):
        """
        Applies the next move to the board: place a new pawn and update 
        the board by turning all appropiate pawns.
        
        Returns:
            Nothing
        """
        self._board.play_pawn(self._next_move[0], self._next_move[1], self._current_player)
        self._board.update_board(self._next_move[0], self._next_move[1], self._current_player)
        self._board.calculate_score()
        

    def display_current_state(self):
        """
        Displays the board and score in the terminal
        """

        # Get grid and score from _board
        grid = self._board._grid # To be updated with a proper getter!!!
        score_white, score_black = self._board.score_white, self._board.score_black 
        
        # Determine next player an his possible

        
        # Feed the grid and score into _interface
        #self._player_interface.print_board(grid, self._possible_moves)
        self._player_interface.print_score(self.players ,score_black, score_white)


    def end_game(self):
        """
        Displays the winner and asks if the players want to play a next game 
        or quit -> updates self._continue_game
        """

        self._board.calculate_score()
        score_white, score_black = self._board.score_white, self._board.score_black 
        self._continue_game = self._player_interface.end_message(score_black, score_white)

        # clear terminal 
        self._player_interface.clear_terminal()


