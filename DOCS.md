`Py2048-Engine` **1.0.0**
## [Py2048_Engine.Game.py](/Py2048_Engine/Game.py)
---
### Py2048_Engine.Game.`Game` [class]
Programatic representation of the game 2048 and its logic

<details style='color: #333333'><summary>Methods</summary><p>

#### Game.`__init__`
```Python
Generates a 2048 game instance.

Args:
    startingBoard (List[List[int]], optional): A custom board to start from. Defaults to None (new game).
```
#### Game.`__repr__`
```Python
Generates a more viewable representation of the current value
of self.board.

Equally spaces items in grid, replaces 'None' with '-'.
```
#### Game.`_getTouchingPositions`
```Python
Returns all positions of 'touching' tiles
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
```
#### Game.`_canContinue`
```Python
Always Ran before Game._placeRandomTile() (except for during board initialization).

Throws GameWonException() if a tile on self.board has a value of '2048'.
Throws GameLostException() IFF both of the following are met:
    1) all tiles are filled (no values on self.board are 'None')
    2) no tiles of the same value 'touch'
        2.i) given position {r, c} with row = r and column = c, touching tiles
        are at (assuming they exist) {r+1, c}, {r-1, c}, {r, c+1}, {r, c-1}

Returns: None
```
#### Game.`_placeRandomTile`
```Python
Places a random tile onto self.board with values of either
'2' (P = 0.9) or '4' (P = 0.1) (defined in class instance vars).

Returns: None
```
#### Game.`_generateBoard`
```Python
Creates a 2 dimensional array of type List[List[int]]
representing a 2048 gamae board and sets it to self.board.

All values are initialized to 'None', except for 2 random positions
being prefilled with values from calls to Game._placeRandomTile().

Returns: None
```
#### Game.`_compressArray`
```Python
Compresses an array in a specified direction by pushing all non-None
values together and either appending or prepending the None values, depending
on direction. Combines like tiles together.

Args:
    array (List[int]): the input array.
    direction (str): the direction of compression, represented by the
    class constants: LEFT, RIGHT, UP, DOWN.

Returns:
    List[int]: the compressed array.
```
#### Game.`_move`
```Python
Performs a movement in a given direction, if possible.

Args:
    direction (str): The direction to move, represented by the
    class constants: LEFT, RIGHT, UP, DOWN.
```
#### Game.`left`
```Python
Simulates a 'left' arrow key/swipe on the board.

Can raise a GameWonException or a GameLostException
if the function call's corresponding movement triggers it.
```
#### Game.`right`
```Python
Simulates a 'right' key/swipe on the board.

Can raise a GameWonException or a GameLostException
if the function call's corresponding movement triggers it.
```
#### Game.`up`
```Python
Simulates a 'up' key/swipe on the board.

Can raise a GameWonException or a GameLostException
if the function call's corresponding movement triggers it.
```
#### Game.`down`
```Python
Simulates a 'down' key/swipe on the board.

Can raise a GameWonException or a GameLostException
if the function call's corresponding movement triggers it.
```
#### Game.`getBoard`
```Python
Getter for the current game board.

Returns:
    List[List[int]]: The current game board.
```
#### Game.`getNumMoves`
```Python
Getter for the current number of moves.

Returns:
    int: The current number of moves.
```
</p></details>

## [Py2048_Engine.Test.py](/Py2048_Engine/Test.py)
---

### Py2048_Engine.Test.`runTest` [function]
<details style='color: #333333'><summary>Details</summary>

```Python
Run a basic CLI test of the Py2048 Engine.
```
</details>

## [Py2048_Engine.Exceptions.py](/Py2048_Engine/Exceptions.py)
---
### Py2048_Engine.Exceptions.`GameException` [class] [inherits: `Exception`]
Base Exception raised when a key event happens within a Game.

Attrs:
    board (List[List[int]]): the final board before the exception was thrown.
    numMoves (int): the number of moves taken before the exception was thrown.
    message (str): a description of the exception.
<details style='color: #333333'><summary>Methods</summary><p>

#### GameException.`__init__`
```Python
Base Exception raised when a key event happens within a Game.

Args:
    board (List[List[int]]): the final board before the exception was thrown.
    numMoves (int): the number of moves taken before the exception was thrown.
    message (str): a description of the exception.
```
</p></details>

### Py2048_Engine.Exceptions.`GameWonException` [class] [inherits: `GameException`]
Exception raised when user loses a Game.

Inherits: GameException

Noninherited Attrs: None
<details style='color: #333333'><summary>Methods</summary><p>

#### GameWonException.`__init__`
```Python
Exception raised when a user wins a Game a tile (position in the board) has a value of 2048.

Args:
    board (List[List[int]]): the final board before the exception was thrown.
    numMoves (int): the number of moves taken before the exception was thrown.
    message (str, optional): a description of the exception. Defaults to "Game won - a tile with the value 2048 reached!".
```
</p></details>

### Py2048_Engine.Exceptions.`GameLostException` [class] [inherits: `GameException`]
Exception raised when user loses a Game.

Inherits: GameException

Noninherited Attrs: None
<details style='color: #333333'><summary>Methods</summary><p>

#### GameLostException.`__init__`
```Python
Exception raised when a user loses a Game (no 'None' spaces left and no tiles can be combined)

Args:
    board (List[List[int]]): the final board before the exception was thrown.
    numMoves (int): the number of moves taken before the exception was thrown.
    message (str, optional): a description of the exception. Defaults to "Game lost - no blank spaces left and no tile combinations left!".
```
</p></details>

