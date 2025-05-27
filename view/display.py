class Display():




    def __init__(self):
            self._black=None
            self._white=None
            
    @property
    def white(self):
        return self._white
    
    @property
    def black(self):
        return self._black
    

    def welcome(self):
        print('Welcome')
        self.input_player()


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