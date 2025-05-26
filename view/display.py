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
        pass
        

    def print_score(self,score):
        pass

    def end_message(self):
        pass