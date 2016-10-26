#### Chenjunni Zeng ICS 32 Project 5
#### Othello_GUI.py

import tkinter
import Othello

DEFAULT_FONT = ('Helvetica', 20)
B = 'Black'
W = 'White'

class Othello_GUI:
    def __init__(self,board):
        self._board = board
        self._game_window = tkinter.Toplevel()
        game_title = tkinter.Label(self._game_window,
                                   text = 'Othello Game',
                                   font = ('Timesnewroman',25))
        game_title.grid(row = 0,
                        column = 1,
                        sticky = tkinter.W+tkinter.E)
        self.btext = tkinter.StringVar()
        self.wtext = tkinter.StringVar()
        self._black_score_label()
        self._white_score_label()

        self.turn = tkinter.StringVar()
        self.turn.set('{}\'s turn'.format(self._board.turn))
        now_turn = tkinter.Label(self._game_window,
                                 textvariable = self.turn,
                                 font = DEFAULT_FONT)
        now_turn.grid(row = 2,
                  column = 1,
                  sticky = tkinter.S)

        self._signal = tkinter.StringVar()
        self._signal.set('(Game in progress)'.format(self._board.win_method))
        signal = tkinter.Label(self._game_window,
                               textvariable = self._signal,
                               font = ('Helvetica', 15))
        signal.grid(row = 1,
                  column = 1)

        self._disc_board = tkinter.Canvas(self._game_window,
                                          height = 500,
                                          width = 500,
                                          relief=tkinter.RAISED,
                                          background='#006400')
        self._disc_board.grid(row = 3,
                              column = 0,
                              columnspan = 3,
                              padx= 5,pady= 5,
                              sticky = tkinter.W+tkinter.E+tkinter.N+tkinter.S)

        self._disc_board.bind('<Configure>',self.board_resize)
        self._disc_board.bind('<Button-1>',self.clicked)

        self._game_window.rowconfigure(3,weight = 1)
        self._game_window.columnconfigure(0,weight = 1)
        self._game_window.columnconfigure(1,weight = 1)
        self._game_window.columnconfigure(2,weight = 1)
        

    def _black_score_label(self):
        self.btext.set("{}'s score: {}".format(B,self._board.get_score(B)))
        self._score(self.btext,0)
        
    def _white_score_label(self):
        self.wtext.set("{}'s score: {}".format(W,self._board.get_score(W)))
        self._score(self.wtext,2)
        
    def _score(self,color_and_scores,col_num):        
        score_label = tkinter.Label(self._game_window,
                                    textvariable = color_and_scores,
                                    font = DEFAULT_FONT)
        score_label.grid(row = 1,
                         column = col_num,
                         sticky = tkinter.W+tkinter.E)


    def _draw_disc(self,row,col,height,width,color):
        '''draw a disc at specific place'''
        tlx = col * width
        tly = row * height
        brx = tlx + width
        bry = tly + height
        self._disc_board.create_oval(tlx, tly, brx, bry,
                                     fill = color, outline = color)


    def _draw_board(self):
        '''draw the game board'''

        self._disc_board.delete(tkinter.ALL)
        
        width,height,row_height,col_width = self._get_width_and_height()
        
        for i in range(self._board.rows-1):
            self._disc_board.create_line(0,row_height*(i+1),
                                         width,row_height*(i+1),
                                         fill='#008B45',width=2)
        for i in range(self._board.cols-1):
            self._disc_board.create_line(col_width*(i+1),0,
                                         col_width*(i+1),height,
                                         fill='#008B45',width=2)

        for row in range(self._board.rows):
            for col in range(self._board.cols):
                color = self._board.board[row][col]
                if color != '*':
                   self._draw_disc(row,col,row_height,col_width,color)
        self.btext.set("{}'s score: {}".format(B,self._board.get_score(B)))
        self.wtext.set("{}'s score: {}".format(W,self._board.get_score(W)))
        self.turn.set('{}\'s turn'.format(self._board.turn))



    def board_resize(self,event):
        self._draw_board()

    def clicked(self,event):
        '''if the click valid then make the move and flip the discs'''
        x = event.x
        y = event.y
        width,height,row_height,col_width = self._get_width_and_height()
        pos_list = self._board.possible_move(self._board.turn)
        for position in pos_list:
            tlx = position[1] * col_width
            tly = position[0] * row_height
            brx = tlx + col_width
            bry = tly + row_height
            if x >= tlx and x <= brx and y >= tly and y <= bry:
                try:
                    self._board.make_a_move(position[0],position[1])
                    self._draw_board()
                    break
                except Othello.InvalidMoveError:
                    pass
                except Othello.InvalidOthelloInputError:
                    pass
                except Othello.OthelloGameOverError:
                    self._game_over()
        if self._board.possible_move(self._board.turn)==[] and self._board.possible_move(Othello.opposite_turn(self._board.turn)):
            self._game_over

    def _game_over(self):
        self._draw_board()
        winner = self._board.winner()
        self._signal.set('Game Over')
        if winner != None:
            self.turn.set('{} win!'.format(winner))
            tkinter.messagebox.showinfo(message = 'Game Over! {} win!'.format(winner))
        else:
            self.turn.set('It is a draw, nobody wins.')
            tkinter.messagebox.showinfo(nessage = 'It is a draw, nobody wins.')

        
        
    def _get_width_and_height(self):
        width = self._disc_board.winfo_width()
        height = self._disc_board.winfo_height()
        row_height = height/self._board.rows
        col_width = width/self._board.cols
        return width,height,row_height,col_width

