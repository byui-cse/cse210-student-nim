import random

# TODO: Define the Board class here
class Board:
    """ this is the playing board for the game.
    It needs a random number of piles, with a randon number of beads in each pile.
    
    Steretype: Information Holder
    Attributes: _piles (list): the number of piles of stones  """
        
    def __init__(self) -> None:
        self._piles = []
        self._prepare()

    def apply(self, move):#public method
        
        """ Applies a move to the playing surface. 
        removes any number of stones from a pile. 
        
        accepts one argument: move
        self(Board): an instance of Board  """

    def is_empty():#public method
        """  determins if all the stones have been removed from the board

        Returns: Boolean:  True if board has zero stones. False if there are stones on the board
        Args: self (Board): and instance of Board
        """
        pass

    def to_string():#public method
        """ converts the board data to its string representation and returns it to the caller
         Args:
          self(Board): an instance of Board

          Returns: string: A representation of the current board.
        """
        pass

    def _prepare(): #private method
        """ sets up the board with a random number of piles (2-5) containing a random number of stones (1-9) in each

         self(Board): an instance of Board

         this method sould be private. """
        pass   