

class Coordinates:
    def __init__(self,coord):
        if len(coord) < 2 or not coord[0].isalpha() or not coord[1:].isdigit():
            raise ValueError(f"Coordonnée invalide : {coord}")
    
        column_letter = coord[0].upper()
        row_number = int(coord[1:])

        column_index = ord(column_letter) - ord('A')
        row_index = row_number - 1

        if not (0 <= column_index <= 7 and 0 <= row_index <= 7):
            raise ValueError(f"Coordonnée hors du plateau : {coord}")
        
        self._row_alphanum=row_number
        self._col_alphanum=column_letter

        self._row_index =row_index
        self._col_index = column_index

    @property
    def row_index(self):
        return self._row_index
    
    @property
    def col_index(self):
        return self._col_index
    
    @property
    def col_alphanum(self):
        return self._col_alphanum
    
    @property
    def row_alphanum(self):
        return self._row_alphanum
