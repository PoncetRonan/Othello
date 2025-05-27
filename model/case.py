from .pawn import Pawn
from .noPawnError import NoPawnError
from typing import List

class Case:

    """ Case class that compose the boar"""
    def __init__(self, row, column):
        self._neighbors={}
        self._state='empty'
        self._pawn=None
        self._row=row
        self._column=column
    
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

    def neighbors_coordinates (self):
        """Return the list of neighbors coordinate 
        return tuple of coordinates"""
        nc=list()
        # print(f"calculate in ({max(0,self.row-1)},{max(0,self.column-1)}) ({min(8,self.row+1)},{min(8,self.column+1)})")

        for r in range(max(0,self.row-1),min(8,self.row+2)):
            for c in range(max(0,self.column-1),min(8,self.column+2)):
                if ((c!=self.column) or (r!=self.row)):
                    coordinate=(r,c)
                    nc.append(coordinate)
        return nc
    
    
