class Case:
    def __init__(self,x,y):
        self._neighbors={}
        self._state='empty'
        self._pawn=None
    
    @property
    def state(self):
        return self._state

    @property
    def pawn(self):
        if self._state == 'empty':
            # should raise an exception insteed
            return None
        else:
            return self._pawn
    
    def add_pawn(self, pawn):
        if self._state == 'empty':
            self._pawn=pawn
            self._state='occupied'
        else:
            raise ValueError ("Can't ")
    @property
    def neighbors(self):
        return self._neighbors

    @neighbors.setter
    def set_neighbors(self, neigghbors):
        pass




