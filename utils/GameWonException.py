from typing import List

class GameWonException(Exception):
    """Exception raised when user wins a Game."""

    board: List[List[int]]

    def __init__(self, board: List[List[int]], numMoves: int, message: str = "Game won - a tile with the value 2048 reached!") -> None:
        """Exception raised when a user wins a Game a tile (position in the board) has a value of 2048.

        Args:
            board (List[List[int]]): the final board before the exception was thrown.
            numMoves (int): the number of moves taken before the exception was thrown.
            message (str, optional): a description of the exception. Defaults to "Game won - a tile with the value 2048 reached!".
        """

        self.board = board
        self.message = message
        
        super().__init__(message)