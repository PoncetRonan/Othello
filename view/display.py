import os
import platform
from .coordinates import Coordinates
from rich.table import Table
from rich.console import Console
from rich.box import SQUARE
from rich.style import Style
from rich.text import Text
from model import Player


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
    liste_pions = ["⚪", "⚫", "🔴", "🔵", "🐱", "🐶", "🦄", "🐉"]

    def __init__(self):
            self._black=None
            self._white=None
            self._blackPlayer = Player("",color="black")
            self._whitePlayer = Player("")

            self._black_pawn="⚫"
            self._white_pawn="⚪"
            self._liste_pions = [
    # ⚪ Couleurs / pions classiques
    "⚪", "⚫", "🔴", "🔵", "🟢", "🟡", "🟤", "🟣", "🟠",

    # 🔥 Objets / éléments
    "🧊", "🔥", "💣", "💎", "🪙", "🎯", "🎲", "🧲", "⚙️", "🔮",

    # 🐾 Animaux / créatures
    "🐱", "🐶", "🐸", "🐧", "🐵", "🐢", "🐉", "🦄",

    # ✨ Symboles / fantasy
    "👑", "🛡️", "🗡️"
]


    @property
    def liste_pions(self):
        return self._liste_pions
    @liste_pions.setter
    def liste_pions(self, new_list):
        self._liste_pions = new_list
    @property
    def black_pawn(self):
        return self._black_pawn
    
    @property
    def white_pawn(self):
        return self._white_pawn
    
    @black_pawn.setter
    def black_pawn(self, pawn):
        self._black_pawn = pawn

    @white_pawn.setter
    def white_pawn(self, pawn):
        self._white_pawn = pawn
    
            
    @property
    def white(self)->Player:
        return self._whitePlayer
    
    @property
    def black(self)->Player:
        return self._blackPlayer
    
    def clear_terminal(self):
        """Clears the terminal screen.
        BLAME JIP"""
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

    def get_player_name(self, player:Player):
        return self.input_player(player)

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


    def play_against_IA(self):
        rep=input("Do you want to play against an IA [yes/no]:\n")
        if rep== "yes":
            return True
        else:
            return False
    
    def input_player(self, player:Player):
        player.name=input(f"Enter the first player's name for {player.color} :  \n")
        if (player.color=="black"):
            self.black_pawn=self.choose_pawn()
        else:
            self.white_pawn=self.choose_pawn()

        return player       

    def input_play_move(self,list_valid_move, current_player:Player):
        """
        Prompts the current player to input their next move and validates it against a list of legal moves.
        Parameters:
            list_valid_move (list): A list of valid moves represented as tuples (row, col).
            current_player (str): The color of the current player ("white" or "black").
        Returns:
            tuple: A valid move as a tuple (row, col) if the input is valid.
        """

        is_valid=False

        print(f"It is your turn: {current_player.name} (you're playing '{current_player.color}')")
        input_msg='Enter your next move: \n'

        is_valid=False
        while is_valid == False:
            next_move=input(input_msg)
            try:
                alphan_coordinate=Coordinates(next_move)
                absolute_coord=(alphan_coordinate.row_index,alphan_coordinate.col_index)
                if absolute_coord in list_valid_move:
                    is_valid=True
                else:
                    input_msg=("You can't put a pawn there , enter a new move : \n")
                
            except:
                input_msg=("Can't recognize this move , enter a new move : \n")


        return absolute_coord




    def print_board(self, board, possible_moves):
        console = Console()
        
        table = Table(
            title="Othello",
            show_header=True,
            show_lines=True,
            box=SQUARE,  # Style de boîte carrée
            # Ajoutez ces paramètres pour contrôler l'apparence des cellules
            padding=0,    # Réduit l'espacement interne
            pad_edge=False, # Désactive le padding des bords
            collapse_padding=True # Fusionne les espacements
        )
        
        # Ajoutez une colonne pour les numéros de ligne
        table.add_column("", style="bold blue", width=3, no_wrap=True, justify="center")
        
        # Ajoutez les colonnes (A-H)
        for letter in [chr(65+i) for i in range(8)]:
            table.add_column(letter, width=3, no_wrap=True, justify="center")
        
        # Ajoutez les lignes
        for i in range(8):
            row = [str(i + 1)]
            for j in range(8):
                try:
                    if (i, j) in possible_moves:
                        row.append("[green]★[/green]")
                    elif board[i][j].pawn.color == 'white':
                        row.append(f"{self.white_pawn}")
                    elif board[i][j].pawn.color == 'black':
                        row.append(f"{self.black_pawn}")
                except:
                    row.append(" ")
            table.add_row(*row)
        
        console.print(table)
            

    def print_score(self, players, score_black, score_white):
        """
        Prints the current score of both players in a formatted manner.
        Parameters:
            score_black (int): Current score for the black player.
            score_white (int): Current score for the white player.
        Returns:
            None
        """
        print(f"Score :   {players["black"]} : {score_black}  :  {players["white"]} : {score_white}")

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
    
    def choose_pawn(self):
        pions=self.liste_pions
        pawn_valid=False
        strinput="Choisis ton pion :"
        while pawn_valid == False:
            print(strinput)
            try:
                for i, pion in enumerate(pions):
                    print(f"{i + 1}. {pion}")

                choix = int(input("Numéro du pion choisi : ")) - 1

                if 0 <= choix < len(pions):
                    print(f"Tu as choisi : {pions[choix]}")
                    pawn_valid=True
                else:
                    strinput= "Choix invalide."
            except:
                strinput='Veuillez indiquer un numéro de pion valide.'
        self.liste_pions = [p for p in self.liste_pions if p != pions[choix]]
        return pions[choix]
