from typing import List

class GameException(Exception):
    """Base Exception raised when a key event happens within a Game.
    
    Attrs:
        board (List[List[int]]): the final board before the exception was thrown.
        numMoves (int): the number of moves taken before the exception was thrown.
        message (str): a description of the exception.
    """

    board: List[List[int]]
    numMoves: int
    message: str

    def __init__(self, board: List[List[int]], numMoves: int, message: str) -> None:
        """Base Exception raised when a key event happens within a Game.

        Args:
            board (List[List[int]]): the final board before the exception was thrown.
            numMoves (int): the number of moves taken before the exception was thrown.
            message (str): a description of the exception.
        """

        self.board = board
        self.numMoves = numMoves
        self.message = message
        
        super().__init__(message)