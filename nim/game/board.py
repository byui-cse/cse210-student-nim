import random

# TODO: Define the Board class here
class Board:
    """ this is the playing board for the game.
    It needs a random number of piles, with a randon number of beads in each pile.
    
    Steretype: Information Holder
    Attributes: _piles (list): the number of piles of stones  """
        
    def __init__(self):
        """ this is a class constructor"""
        self._piles = []
        self._prepare()# setting up how board looks


    def apply(self, move):#public method
        
        """ Applies a move to the playing surface. 
        removes any number of stones from a pile. 
        
        accepts one argument: move
        self(Board): an instance of Board  """

        pile = move.get_pile()
        stones = move.get_stones()
        self.piles[pile] = max(0, self._piles[pile] - stones) 

    def is_empty(self):#public method
        """  determins if all the stones have been removed from the board

        Returns: Boolean:  True if board has zero stones. False if there are stones on the board
        Args: self (Board): and instance of Board
        """
        no_more_piles= len(self._piles) * [0] # I dont' know why this works
        return self._piles == no_more_piles

    def to_string(self):#public method
        """ converts the board data to its string representation and returns it to the caller
         Args:
          self(Board): an instance of Board

          Returns: string: A representation of the current board.
        """
        text = "\n ----------------"
        for pile, stones in enumerate(self._piles):
            text += (f"\n{pile}:" + "0" * stones)
        text = "\n ----------------"
        return text    

    def _prepare(self): #private method
        """ sets up the board with a random number of piles (2-5) containing a random number of stones (1-9) in each

         self(Board): an instance of Board

         this method sould be private. """
        piles =random.randint(2,5)

        for i in range(piles):
            stones = random.randint(1,9)
            self._piles.append(stones)