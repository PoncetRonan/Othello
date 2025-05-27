from engine import Othello

# Let's start a game of Othello
game = Othello()

while game.continue_game == True:
    game.start_game()

    while game.num_blocked_players < 2:
        game.play_game()
    
    game.end_game()

