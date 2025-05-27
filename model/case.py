from pawn import Pawn
from typing import List
from noPawnError import NoPawnError

class Case:
    """ Case class that compose the boar"""
    def __init__(self, row, column):
        self._neighbors={}
        self._state='empty'
        self._pawn=None
        self.row=row
        self.column=column
    
    @property
    def column(self):
        return self._column
    
    @property
    def row(self):
        return self._row
    
    @property
    def state(self):
        return self._state

    @property
    def pawn(self)->Pawn: 
        if self._state == 'empty':
            raise NoPawnError("No pawn available")
        else:
            return self._pawn
    
    def add_pawn(self, pawn:Pawn):
        if self._state == 'empty':
            self._pawn=pawn
            self._state='occupied'
        else:
            raise ValueError ("The place is already occupied. Can't add a pawn to the case ({self.row}, {self.column})")
        
    @property
    def neighbors(self)-> List['Case']:
        return self._neighbors

    @neighbors.setter
    def set_neighbors(self, neighbors:List['Case']):
        for n in neighbors:
            if type(n) != Case:
                raise ValueError("Neighbors need to be a list of Cases or empty list")
        self._neighbors=neighbors
    
