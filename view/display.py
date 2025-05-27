import os
import platform


class Display():
    """
    Handles all terminal input and output for the Othello game.

    The Display class manages user interactions and visual representations of the game.
    It collects player names, handles user move inputs, prints the game board and scores,
    and displays messages including welcome and end-game summaries.

    Attributes:
        _black (str): Name of the player playing with black pawns.
        _white (str): Name of the player playing with white pawns.

    Properties:
        black (str): Returns the black player's name.
        white (str): Returns the white player's name.

    Methods:
        clear_terminal():
            Clears the terminal.

        welcome():
            Displays a welcome message and prompts users to enter player names.

        input_player():
            Prompts users to enter names for black and white players.

        input_play_move(list_valid_move):
            Asks the current player to input a move, and validates it against a list of legal moves.
            Returns a valid move as a tuple (row, col).

        print_board(board):
            Prints a formatted 8x8 Othello game board with Unicode characters.

        print_score(score_black, score_white):
            Displays the current score of both players.

        end_message(score_black, score_white):
            Announces the winner or a tie with emoji decorations and prompts whether to play again.
            Returns True if the user wants to play another game, False otherwise.
    """

    def __init__(self):
            self._black=None
            self._white=None
            
    @property
    def white(self):
        return self._white
    
    @property
    def black(self):
        return self._black
    
    def clear_terminal(self):
        """Clears the terminal screen."""
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")


    def welcome(self):
        """Displays a welcome message and optionally shows the game rules before starting."""
        print("\n🎮 Welcome to Othello! 🎮")
        print("A strategic board game where black and white pawns battle for dominance.")
        print("Let the best player win!\n")

        # Ask if the player wants to see the rules
        response = input("Would you like to see the game rules? [yes/no]: ").strip().lower()
        if response in ("yes", "y"):
            self.show_rules()
        
        print("\nLet's set up the game!")
        self.input_player()

    def show_rules(self):
        """Prints the rules of the game to the terminal."""
        print("\n📜 Othello Rules:")
        print("- The game is played on an 8x8 grid.")
        print("- Players take turns placing their pawns (⚫ or ⚪) on the board.")
        print("- A move is valid only if it outflanks one or more of the opponent's pawns.")
        print("- Outflanked pawns are flipped to the current player's color.")
        print("- You must play a move if you have one; otherwise, you pass.")
        print("- The game ends when neither player can move.")
        print("- The player with the most pawns on the board at the end wins.")
        print("\n🧠 Tip: Corners are powerful. Plan your moves carefully!")


    def input_player(self):
        self._black=input("Enter the first player's name :  \n")
        self._white=input("Enter the second player's name : \n")

    def input_play_move(self,list_valid_move):
        is_valid=False
        next_move=input('Enter your next move')
        if next_move in list_valid_move:
            is_valid=True
        while is_valid == False:
            next_move=input('Incorrect move , enter a valid move')
            if next_move in list_valid_move:
                is_valid=True
        return next_move


    def print_board(self,board):
        haut = "  ┌" + "───┬" * 7 + "───┐"
        milieu = "  ├" + "───┼" * 7 + "───┤"
        bas = "  └" + "───┴" * 7 + "───┘"

        # En-tête colonnes
        print("    " + "   ".join(str(i+1) for i in range(8)))
        print(haut)

        for i, ligne in enumerate(board):
            ligne_affichée = f"{chr(65 + i)} │"
            for case in ligne:
                if case == "N":
                    ligne_affichée += " ● │"
                elif case == "B":
                    ligne_affichée += " ○ │"
                else:
                    ligne_affichée += "   │"
            print(ligne_affichée)
            if i < 7:
                print(milieu)
            else:
                print(bas)
            pass
        

    def print_score(self,score_black,score_white):
        print(f"Score :   {self.black} : {score_black}  :  {self.white} : {score_white}")
        pass

    def end_message(self, score_black, score_white):
        """
        Displays the end-of-game message, announces the winner or a tie with emojis,
        and prompts the user to decide whether to play another game.

        Parameters:
            score_black (int): Final score for the black player.
            score_white (int): Final score for the white player.

        Returns:
            bool: True if the user wants to play another game, False otherwise.
        """
        
        if score_black > score_white:
            winner = self.black
            winning_score = score_black
            emoji = "🏆⚫"
        elif score_white > score_black:
            winner = self.white
            winning_score = score_white
            emoji = "🏆⚪"
        else:
            winner = "No one"
            winning_score = score_black  # since both are equal
            emoji = "🤝"

        print("\n🎉 Game Over! 🎉")
        if winner == "No one":
            print(f"It's a tie with both players scoring {winning_score}! {emoji}")
        else:
            print(f"The winner is {winner} with a score of {winning_score}! {emoji} Congratulations! 🥳")

        response = input("Do you want to play another game [yes/no]: ").strip().lower()
        if response in ("yes", "y"):
            play_again = True
        else:
            play_again = False
        
        return play_again