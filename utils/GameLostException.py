from typing import List

class GameLostException(Exception):
    """Exception raised when user loses a Game."""

    board: List[List[int]]

    def __init__(self, board: List[List[int]], numMoves: int, message: str = "Game lost - no blank spaces left and no tile combinations left!") -> None:
        """Exception raised when a user loses a Game (no 'None' spaces left and no tiles can be combined)

        Args:
            board (List[List[int]]): the final board before the exception was thrown.
            numMoves (int): the number of moves taken before the exception was thrown.
            message (str, optional): a description of the exception. Defaults to "Game lost - no blank spaces left and no tile combinations left!".
        """

        self.board = board
        self.numMoves = numMoves
        self.message = message
        
        super().__init__(message)