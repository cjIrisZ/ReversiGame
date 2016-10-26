##Chenjunni Zeng ICS 32 Lab Project #5
##Othello.py

B = 'Black'
W = 'White'
directions = [[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]]

class InvalidMoveError(Exception):
    pass

class InvalidOthelloInputError(Exception):
    pass

class OthelloGameOverError(Exception):
    pass


def opposite_turn(turn):
    if turn == B:
        return W
    else:
        return B

    
class Othello:
    def __init__(self,rows,columns,first_color,TL_color,win_method):
        board = []
        for row in range(rows):
            board.append([])
            for col in range(columns):
                board[-1].append('*')
        mid_col = int(columns/2)
        mid_row = int(rows/2)
        board[mid_row][mid_col-1] = TL_color
        board[mid_row-1][mid_col] = TL_color
        board[mid_row][mid_col] = opposite_turn(TL_color)
        board[mid_row-1][mid_col-1] = opposite_turn(TL_color)
        self.board = board
        self.turn = first_color
        self.win_method = win_method
        self.rows = rows
        self.cols = columns
    
    def make_a_move(self,row,col):
        '''makes a move and flips discs and change the next turn'''
        self.invalid_input(row,col)
        self.invalid_move(row,col)
        self.board[row][col] = self.turn
        for direction in directions:
            n = self.flip_or_not(direction,col,row)
            self.flip_discs(row,col,direction[0],direction[1],n)
        if self.possible_move(opposite_turn(self.turn)) != []:
            self.turn = opposite_turn(self.turn)
        self.game_over()
        
    def flip_or_not(self,direction,col,row):
        row_drct = direction[0]
        col_drct = direction[1]
        new_col = col+col_drct
        new_row = row+row_drct
        n = 0
        if (new_row in range(len(self.board))) and (new_col in range(len(self.board[0]))):
            while self.board[new_row][new_col] == opposite_turn(self.turn):
                n += 1
                new_col = new_col+col_drct
                new_row = new_row+row_drct
                if not(new_row in range(len(self.board))) or not(new_col in range(len(self.board[0]))):
                    n = 0
                    break
                if self.board[new_row][new_col] == '*':
                    n = 0
                    break
        return n


    def flip_discs(self,row,col,row_drct,col_drct,n):
        for i in range(n):
            row += row_drct
            col += col_drct
            self.board[row][col] = self.turn

            
    def possible_move(self,turn):
        possible_moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == turn:
                    for direction in directions:
                        n = self.where_can_put(direction,col,row,turn)
                        if n != 0:
                            new_row = row + ((direction[0])*(n+1))
                            new_col = col + ((direction[1])*(n+1))
                            if self.board[new_row][new_col] == '*':
                                new_cell = [new_row,new_col]
                                possible_moves.append(new_cell)
        return possible_moves

    def where_can_put(self,direction,col,row,turn):
        row_drct = direction[0]
        col_drct = direction[1]
        new_col = col+col_drct
        new_row = row+row_drct
        n = 0
        if (new_row in range(len(self.board))) and (new_col in range(len(self.board[0]))):
            while self.board[new_row][new_col] == opposite_turn(turn):
                n += 1
                new_col = new_col+col_drct
                new_row = new_row+row_drct
                if not(new_row in range(len(self.board))) or not(new_col in range(len(self.board[0]))):
                    n = 0
                    break
                if self.board[new_row][new_col] == '*':
                    break
        return n

                    
                
        
    def winner(self):
        w=self.get_score(W)
        b=self.get_score(B)
        if (w>b and self.win_method == '1') or (w<b and self.win_method == '2'):
            return W
        if (w>b and self.win_method == '2') or(w<b and self.win_method == '1'):
            return B
        else:
            return None

    def get_score(self,color):
        score=0
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == color:
                    score+=1
        return score

    def game_over(self):
        if self.possible_move(self.turn) == [] and self.possible_move(opposite_turn(self.turn)) == []:
            raise OthelloGameOverError()

    def invalid_move(self,row,col):
        if self.board[row][col] != '*':
            raise InvalidMoveError()
        
    def invalid_input(self,row,col):
        if type(row) != int or type(col) != int:
            raise InvalidOthelloInputError()

