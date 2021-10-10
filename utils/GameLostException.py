from typing import List

from utils.GameException import GameException

class GameLostException(GameException):
    """Exception raised when user loses a Game.
    
    Inherits: GameException

    Noninherited Attrs: None
    """

    def __init__(self, board: List[List[int]], numMoves: int, message: str = "Game lost - no blank spaces left and no tile combinations left!") -> None:
        """Exception raised when a user loses a Game (no 'None' spaces left and no tiles can be combined)

        Args:
            board (List[List[int]]): the final board before the exception was thrown.
            numMoves (int): the number of moves taken before the exception was thrown.
            message (str, optional): a description of the exception. Defaults to "Game lost - no blank spaces left and no tile combinations left!".
        """
        
        super().__init__(board, numMoves, message)