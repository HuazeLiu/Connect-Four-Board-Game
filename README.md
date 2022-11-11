# Connect-Four-Board-Game
The game is played by two players, alternating turns, with each trying to place four checkers in a row vertically, horizontally, or diagonally. 
The board stands vertically, the checkers cannot be placed into an arbitrary position.


The Board class—a preview

In this problem, you will need to create a class named Board that implements some of the features of the Connect Four game. The Board class will have three data members: there will be a two-dimensional list (a list of lists) containing characters to represent the game area, and a pair of variables holding the numbers of rows and columns on the board (6 rows and 7 columns is standard, but your Board data type will be able to handle boards of any size).

Even as we allow arbitrary board sizes, however, we will preserve the four-in-a-row requirement for winning the game. (Admittedly, this makes it hard to win the game on a 3x3 board, but we'll stick with it.)

