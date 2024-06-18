import random

def inarow_Neast(ch, r_start, c_start, A, N):
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start > H - 1:
        return False
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False
    for i in range(N):
        if A[r_start][c_start+i] != ch:
            return False
    return True

def inarow_Nsouth(ch, r_start, c_start, A, N):
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False
    if c_start < 0 or c_start > W - 1:
        return False
    for i in range(N):
        if A[r_start+i][c_start] != ch:
            return False
    return True

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    H = len(A)
    W = len(A[0])
    if r_start - (N-1) < 0 or r_start > H - 1:
        return False
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False
    for i in range(N):
        if A[r_start-i][c_start+i] != ch:
            return False
    return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False
    for i in range(N):
        if A[r_start+i][c_start+i] != ch:
            return False
    return True

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

    def __repr__(self):
        s = ''
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-' + "\n"
        for col in range(0,self.width):
            s += ' ' + str(col)

        return s
    
    def addMove(self, col, ox):
        H = self.height
        for row in range(0,H):
            if self.data[row][col] != ' ':
                self.data[row-1][col] = ox
                return
        self.data[H-1][col] = ox

    def clear(self):
        H = self.height
        W = self.width
        for row in range(0,H):
            for col in range(0,W):
                self.data[row][col] = ' '

    def setBoard(self, moveString):
        nextChecker = 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'
    
    def allowsMove(self,col):
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
        H = self.height
        W = self.width
        D = self.data
        for row in range(H):
            for col in range(W):
                if self.allowsMove(col):
                    return False
        return True
        
    def delMove(self, col):
        for row in range(self.height):
            if self.data[row][col] != ' ':
                self.data[row][col] = ' '
                return
    
    def winsFor(self, ox):
        H = self.height
        W = self.width
        D = self.data

        for row in range(H):
            for col in range(W):
                if inarow_Neast(ox, row, col, D, 4):
                    return True
                if inarow_Nsouth(ox, row, col, D, 4):
                    return True
                if inarow_Nnortheast(ox, row, col, D, 4):
                    return True
                if inarow_Nsoutheast(ox, row, col, D, 4):
                    return True
        return False

    def colsToWin(self, ox):
        H = self.height
        W = self.width
        D = self.data
        L = []
    
        for col in range(W):
            if self.allowsMove(col):
                self.addMove(col,ox)
                if self.winsFor(ox):
                    L += [col]
                self.delMove(col)
        return L
    
    def isEmpty(self):
        W = self.width
        D = self.data
        for col in range(W):
            if D[0][col] == " ":
                return False
        return True
    
    def aiMove(self, ox):
        if self.isEmpty():
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
                            if self.allowsMove(col):
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
                            if self.allowsMove(col):
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

    def playGame(self, px, po):
        """playGame does just that -- it calls the nextMove method for two 
           objects of type Player in order to play a game. Those objects are named 
           px and po."""
           
        print("Welcome to Connect-4 Advanced: Lookahead AI version!")
        print(self)
        game_over = False
        turn = 0
        while not game_over:
            if turn == 0:
                col = int(px.nextMove(self))
                if self.allowsMove(col):
                    self.addMove(col, 'X')
                    print(self)
                    if self.winsFor('X'):
                        print('AI 1 with X wins!')
                        break
            else:
                col = int(po.nextMove(self))
                if self.allowsMove(col):
                    self.addMove(col, 'O')
                    print(self)
                    if self.winsFor('O'):
                        print('AI 2 with O wins!')
                        break
            turn += 1
            turn = turn%2


bigb = Board(15,5)
b = Board(7,6)

class Player:
    """ an AI player for Connect Four """

    def __init__( self, ox, tbt, ply ):
        """ the constructor """
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__( self ):
        """ creates an appropriate string """
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s

    def oppCh(self):
        """This method should return the other kind of checker 
           or playing piece"""
        if self.ox == 'X':
            return 'O'
        else:
            return 'X'
    
    def scoreBoard(self, b):
        """This method should return a single float value representing 
           the score of the input b, which you may assume will be an object 
           of type Board. """
        if b.winsFor(self.ox):
            return 100.0
        elif b.winsFor(self.oppCh()):
            return 0.0
        else:
            return 50.0
    
    def tiebreakMove(self, scores):
        """This method takes in scores, which will be a nonempty list of floating-point 
           numbers. If there is only one highest score in that scores list, this method 
           should return its COLUMN number, not the actual score! """
        maxValue = max(scores)
        indexMax = []
        for i in range(len(scores)):
            if scores[i] == maxValue:
                indexMax += [i]
            
        if self.tbt == 'LEFT':
            return indexMax[0]
        if self.tbt == 'RIGHT':
            return indexMax[-1]
        else:
            return random.choice(indexMax)

    def scoresFor(self,b):
        """This method is the heart of the Player class! Its job is to return a list of 
           scores, with the cth score representing the "goodness" of the input board after
            the player moves to column c. And, "goodness" is measured by what happens in 
           the game after self.ply moves"""
        H = b.height
        W = b.width
        D = b.data
        scores = [50]*W
        for i in range(len(scores)):
            if not b.allowsMove(i):
                scores[i] = -1.0
            elif b.winsFor(self.ox):
                scores[i] = 100.0
            elif b.winsFor(self.oppCh()):
                scores[i] = 0.0
            elif self.ply == 0:
                scores[i] = 50.0
            else:
                b.addMove(i,self.ox)
                op = Player(self.oppCh(), self.tbt, self.ply-1)
                opScores = op.scoresFor(b)
                scores[i] = 100.0 - max(opScores)
                b.delMove(i)
        return scores
    
    def nextMove(self, b):
        """This method takes in b, an object of type Board and returns an integer -- 
           namely, the column number that the calling object (of class Player) chooses 
           to move to. """
        scores = self.scoresFor(b)
        return self.tiebreakMove(scores)
