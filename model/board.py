class Board:
    def __init__(self, grid, score):
        self._grid = grid
        self._score = score

    def get_grid(self):
        return self._grid
        
    def get_score(self):
        return self._score

    def verify_possible_move(self):
        pass

    def play_pawn(self):
        pass

    def update_board(self):
        pass

    def calculate_move(self):
        pass

    def calculate_score(self):
        pass