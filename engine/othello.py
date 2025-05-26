class Othello():
    def __init__(self, continue_game=True, current_player="black"):
        self._continue_game = continue_game

        if current_player in ["white", "black"]:
            self._current_player = current_player
        else:
            raise ValueError("Value is not valid. Valid values are: 'white', 'black'")
        
        self._num_blocked_players = 0
        self._possible_moves = None

    @property
    def continue_game(self):
        return self._continue_game
    
    @property
    def num_blocked_players(self):
        return self._num_blocked_players

    def start_game(self):
        pass

    def play_game(self):
        pass

    def determine_next_player(self):
        pass

    def determine_next_move(self):
        pass

    def make_move(self):
        pass

    def display_current_state(self):
        pass

    def end_game(self):
        pass
