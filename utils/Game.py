"""
    We can represent 2048 as a 2 dimensional array forming a 4 x 4 grid.

    Each 'position' will be an integer value representing the current value
    of the tile. Blank spaces will have a value of None.

    To start, 2 tiles are placed onto the board. For the duration of the game,
    the user can perform 4 actions: 'UP', 'DOWN', 'LEFT', 'RIGHT'.

    Any time the user performs an action, the following processes occur:
        1) All tiles on the grid that have the same value that are 'touching'
        in the direction of motion (Vertical for Up/Down, Horizontal for Left/Right)
        are combined. The resulting tile is placed where the input tile that was the furthest
        'along' the direction of motion was (Highest for Up, Lowest for Down, Leftmost for Left,
        Rightmost for right).
            - If no tiles can be combined AND all spots in the grid are taken (!None) the user LOSES.
            - If any tile has the value of '2048', the user WINS.
        
        2) A tile is generated and added to a spot on the grid 
"""

from random import choices
from typing import List, Tuple

from utils.Constants import LEFT, RIGHT, UP, DOWN
from utils.GameLostException import GameLostException
from utils.GameWonException import GameWonException

class Game:
    "Programatic representation of the game 2048 and its logic"

    population: List[int] = [2, 4] # Possible choices for random tile generation 
    weights: List[float] = [0.9, 0.1] # Probabilities for corresponding indicies in Game.population

    board: List[List[int]] # Game board
    numMoves: int = 0 # Number of moves taken
    hasOpenSpace: bool = True # Whether or not we have an open space, controlled by Game._canContinue()

    def __init__(self) -> None:
        """Creates a 2048 Game Instance"""

        self._generateBoard()
    
    def _getTouchingPositions(self, position: Tuple[int]) -> List[Tuple[int]]:
        """Returns all positions of 'touching' tiles
        relative to a given position.

        Given position {r, c} with row = r and column = c, touching tiles
        are at (assuming they exist) {r+1, c}, {r-1, c}, {r, c+1}, {r, c-1}.

        This method returns all of the possible positions that exist.

        Args:
            position (Tuple[int]): a position in the format
            (row, col) on self.board.

        Returns:
            List[Tuple[int]]: a list of tuples representing 
            positions in the format (row, col) on self.board.
        """

        row: int
        col: int
        row, col = position

        # Possible positions of touching tiles (not all guarenteed to exist)
        possibleTouchingPositions: List[Tuple[int]] = [
            (row+1, col),
            (row-1, col),
            (row, col+1),
            (row, col-1)
        ]

        touchingPositions: List[Tuple[int]] = []

        # Find out applicable touching positions
        for row, col in possibleTouchingPositions:
            if row >= 0 and row < 4 and col >= 0 and col < 4:
                touchingPositions.append((row, col))
        
        return touchingPositions

    def _canContinue(self) -> None:
        """
            Always Ran before Game._placeRandomTile() (except for during board initialization).
            
            Throws utils.GameWonException() if a tile on self.board has a value of '2048'.
            Throws utils.GameLostException() IFF both of the following are met:
                1) all tiles are filled (no values on self.board are 'None')
                2) no tiles of the same value 'touch'
                    2.i) given position {r, c} with row = r and column = c, touching tiles
                    are at (assuming they exist) {r+1, c}, {r-1, c}, {r, c+1}, {r, c-1}
            
            Returns: None
        """

        # Check for blank tiles and Game Win

        # We use a bool here instead of an instant return since we want to check for a Game Win
        # which requires iteration through the whole board
        hasBlankTile: bool = False

        for row, _ in enumerate(self.board):
            for col, val in enumerate(_):

                if val is None:
                    hasBlankTile = True # Game can continue (no loss at the moment)
                    continue

                elif val == 2048:
                    raise GameWonException(self.board, self.numMoves) # Handle Game Win
        
        if hasBlankTile:
            self.hasOpenSpace = True # update instance-level tracker
            return # Handle known playable game (>= 1 empty space)
        
        self.hasOpenSpace = False # update instance-level tracker

        # If we have no empty tiles we need to check for touching tiles to confirm playability

        for row, _ in enumerate(self.board):
            for col, val in enumerate(_):

                touchingPositions: List[Tuple[int]] = self._getTouchingPositions((row, col))

                # Check if any of the other touching positions match current value
                for row, col in touchingPositions:
                    if val == self.board[row][col]:
                        return # If the user has at least one potential move, we can continue
        
        # If we've made it this far without a return, both conditions for game loss
        # (no empty tiles & no possible moves) have been met and we need to raise GameLostException
        raise GameLostException(self.board, self.numMoves)

    def _placeRandomTile(self) -> None:
        """
            Places a random tile onto self.board with values of either
            '2' (P = 0.9) or '4' (P = 0.1) (defined in class instance vars).

            Returns: None
        """

        # Because of preprocessing done by Game._canContinue(), we
        # are guarenteed >= 1 blankTilePosition if this method runs
        # b/c it is only called if self.hasOpenSpace

        blankTilePositions: List[Tuple[int]] = []

        for row, _ in enumerate(self.board):
            for col, _ in enumerate(self.board):

                if self.board[row][col] is None:
                    blankTilePositions.append((row, col))
        
        # Getitng random tile's value and position
        tileRow: int
        tileCol: int

        tileRow, tileCol = choices(blankTilePositions)[0]
        tileValue: int = choices(Game.population, Game.weights)[0]

        # Updating board with random tile
        self.board[tileRow][tileCol] = tileValue

    def _generateBoard(self) -> None:
        """
            Creates a 2 dimensional array of type List[List[int]]
            representing a 2048 gamae board and sets it to self.board.

            All values are initialized to 'None', except for 2 random positions
            being prefilled with values from calls to Game._placeRandomTile().

            Returns: None
        """

        self.board = [ [None] * 4 for _ in range(4) ]
        self._placeRandomTile()
        self._placeRandomTile()

    def _compressArray(self, array: List[int], direction: str) -> List[int]:
        """Compresses an array in a specified direction by pushing all non-None
        values together and either appending or prepending the None values, depending
        on direction. Combines like tiles together.

        Args:
            array (List[int]): the input array.
            direction (str): the direction of compression, represented by the
            constants (import from utils.Constants): LEFT, RIGHT, UP, DOWN.

        Returns:
            List[int]: the compressed array.
        """
        
        filteredArray:  List[int] = [elem for elem in array if not elem is None]

        # Handle compression w/ like neighboring values

        i: int = 0 # use explicit idx instead of enumerate() since we want to change it
        for val in filteredArray:

            if i+1 >= len(filteredArray): # end of arr so break
                break

            if val == filteredArray[i+1]: # we have a dupe @ next pos
                
                # Compression-direction specific manipulations

                if direction == LEFT or direction == UP:
                    filteredArray[i] = 2*val # set curr val to double
                    filteredArray.pop(i+1) # remove next val
                
                elif direction == RIGHT or direction == DOWN:
                    filteredArray[i+1] = 2*val # set next val to double
                    filteredArray.pop(i+1) # remove curr val
                
                i -= 1 # we decr len(arr) by 1 so lower i

            i += 1 # next pos

        # if None not in array: # DO THIS AFTER COMPRESSING
        #     return array # Array is full so can't be compressed

        # Reintroduce None values
        if direction == LEFT or direction == UP:
            compressedArray: List[int] = filteredArray
            
            for _ in range(4-len(filteredArray)):
                compressedArray.append(None)
        
        elif direction == RIGHT or direction == DOWN:
            compressedArray: List[int] = filteredArray
            
            for _ in range(4-len(filteredArray)):
                compressedArray.insert(0, None)    
                
        return compressedArray

    def _move(self, direction: str) -> None:
        """Performs a movement in a given direction, if possible.

        Args:
            direction (str): The direction to move, represented by the
            constants (import from utils.Constants): LEFT, RIGHT, UP, DOWN.
        """

        self._canContinue()
        
        if direction == LEFT or direction == RIGHT:
            for i, row in enumerate(self.board):
                self.board[i] = self._compressArray(row, direction)

        
        elif direction == DOWN or direction == UP:
            for col in range(4):
                column: List[int] = []

                for row in range(4):
                    column.append(self.board[row][col])

                newColumn: List[int] = self._compressArray(column, direction)

                for row in range(4):
                    self.board[row][col] = newColumn[row]
        
        if self.hasOpenSpace:
            self._placeRandomTile()

    def left(self) -> None:
        """
            Moves left.
        """

        self._move(LEFT)

    def right(self) -> None:
        """
            Moves right.
        """

        self._move(RIGHT)

    def up(self) -> None:
        """
            Moves up.
        """

        self._move(UP)

    def down(self) -> None:
        """
            Moves down.
        """

        self._move(DOWN)

    def __repr__(self) -> str:
        """
            Generates a more viewable representation of the current value
            of self.board.

            Equally spaces items in grid, replaces 'None' with '-'.
        """

        # Credit: https://stackoverflow.com/questions/13214809/pretty-print-2d-list

        s: List[List[str]] = [[str(e) if e is not None else " " for e in row] for row in self.board]
        lens: List[int] = [max(map(len, col)) for col in zip(*s)]
        fmt: str = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table: List[str] = [fmt.format(*row) for row in s]
        
        return '\n'.join(table)

if __name__ == "__main__":
    ...