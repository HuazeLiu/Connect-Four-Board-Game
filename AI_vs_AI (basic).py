import random
def inarow_Neast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading east and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start > H - 1:
        return False            # Out-of-bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False            # O.o.b. column
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start][c_start+i] != ch: # A mismatch!
            return False
    return True                 # All offsets succeeded, so we return True

def inarow_Nsouth(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading south and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start] != ch: # A mismatch!
            return False
    return True                 # All offsets succeeded, so we return True

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading northeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start - (N-1) < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start-i][c_start+i] != ch: # A mismatch!
            return False
    return True                 # All offsets succeeded, so we return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading southeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False            # Out-of-bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False            # O.o.b. column
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start+i] != ch: # A mismatch!
            return False
    return True                 # All offsets succeeded, so we return True

class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # The string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-' + "\n"   # Bottom of the board
        for col in range(0,self.width):
            s += ' ' + str(col) 
        # Add code here to put the numbers underneath

        return s       # The board is complete; return it
    
    def addMove(self, col, ox):
        """add X or O in the board according the game rules"""
        H = self.height
        for row in range(0,H):
            if self.data[row][col] != ' ':
                self.data[row-1][col] = ox
                return
        self.data[H-1][col] = ox

    def clear(self):
        """clear the board"""
        H = self.height
        W = self.width
        for row in range(0,H):
            for col in range(0,W):
                self.data[row][col] = ' '

    
    def setBoard(self, moveString):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.setBoard('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.setBoard('000000') to
           see them alternate in the left column.

           moveString must be a string of one-digit integers.
        """
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'
    
    def allowsMove(self,col):
        """True if col is in-bounds"""
        H = self.height
        W = self.width
        D = self.data
        if col >= W or col < 0:
            return False
        elif D[0][col] != ' ':
            return False
        else:
            return True

    def isFull(self):
        """checks if the board is full."""
        H = self.height
        W = self.width
        D = self.data
        for row in range(H):
            for col in range(W):
                if self.allowsMove(col):
                    return False
        return True
        
    def delMove( self, col ):
        """ removes the checker from column col """
        for row in range( self.height ):
            # look for the first nonempty row
            if self.data[row][col] != ' ':
                # put in the checker
                self.data[row][col] = ' '
                return
        # it's empty, just return
        return
                    
    
    def winsFor(self, ox):
        H = self.height
        W = self.width
        D = self.data

        for row in range(H):
            for col in range(W):
                if inarow_Neast(ox, row, col, D, 4) == True:
                    return True
                if inarow_Nsouth(ox, row, col, D, 4) == True:
                    return True
                if inarow_Nnortheast(ox, row, col, D, 4) == True:
                    return True
                if inarow_Nsoutheast(ox, row, col, D, 4) == True:
                    return True
        return False     
    
    def colsToWin(self, ox):
        """the colsToWin method should return the list of columns where ox 
           can move in the next turn in order to win and finish the game. The columns 
           should be in numeric order (if there are more than one). Also, colsToWin 
           should not look ahead more than one turn. """
        H = self.height
        W = self.width
        D = self.data
        L = []
    
        for col in range(W):
            if self.allowsMove(col) == True:
                self.addMove(col,ox)
                if self.winsFor(ox):
                    L += [col]
                self.delMove(col)
        return L
    
    def isEmpty(self):
        """Test if the Board is Empty"""
        W = self.width
        D = self.data
        for col in range(W):
            if D[0][col] == " ":
                return False
            return True

    
    def aiMove(self, ox):
        """aiMove should return a single integer, which must be a legal 
           column in which to make a move"""
        if self.isEmpty() == True:
            return random.choice(range(7))
        else:
            if ox == 'O':
                L1 = self.colsToWin('X')
                L = self.colsToWin(ox)
                while True:
                    if len(L) != 0:
                        return L[random.choice(range(len(L)))]
            
                    elif len(L1) != 0:
                        return L1[0]
                
                    elif len(L) == 0 and len(L1) == 0:
                        for col in range(7):
                            if self.allowsMove(col) == True:
                                return col
            else:
                L2 = self.colsToWin('O')
                L = self.colsToWin(ox)
                while True:
                    if len(L) != 0:
                        return L[random.choice(range(len(L)))]
            
                    elif len(L2) != 0:
                        return L2[0]
                
                    elif len(L) == 0 and len(L2) == 0:
                        for col in range(7):
                            if self.allowsMove(col) == True:
                                return col


    def hostGame(self):
        """host the Connect Four Game for two AI"""
        print("Welcome to Connect Four!")
        print(self)
        game_over = False
        turn = 0
        while not game_over:
            if turn == 0:
                col = int(self.aiMove('X'))
                if self.allowsMove(col):
                    self.addMove(col, 'X')
                    print(self)
                    if self.winsFor('X'):
                        print('AI 1 with X wins!')
                        break
            else:
                col = int(self.aiMove('O'))
                if self.allowsMove(col):
                    self.addMove(col, 'O')
                    print(self)
                    if self.winsFor('O'):
                        print('AI 2 with O wins!')
                        break
            turn += 1
            turn = turn%2

# This is the end of the Board class
# Below are some boards that will be re-created each time the file is run:

"""AI1 vs AI2:

Game 1:
| | | |O|O| | |
| | | |X|X| | |
| | | |O|O| | |
| | | |X|X| | |
| | | |O|O| | |
| |O|X|X|X|X| |
---------------
 0 1 2 3 4 5 6
AI 1 with X wins!

Game 2:
| | |O|X|X|O| |
| | |X|O|O|X| |
| |X|O|X|X|O|O|
| |O|X|O|O|X|X|
| |X|O|X|X|O|X|
|O|X|O|X|X|O|O|
---------------
 0 1 2 3 4 5 6
AI 1 with X wins!

Game 3:
| | | | | | | |
| | | | | | | |
| | | | | | | |
| |O|X| | | | |
|O|O|O|O|X| | |
|X|X|X|O|X|X|O|
---------------
 0 1 2 3 4 5 6
AI 2 with O wins!
"""

bigb = Board(15,5)
b = Board(7,6)