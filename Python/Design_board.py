#### Chenjunni Zeng ICS 32 Project 5
#### Design_board.py

import tkinter
import Othello
import Othello_GUI

DEFAULT_FONT = ('Helvetica', 20)
Row_and_Col = [4,6,8,10,12,14,16]
B = 'Black'
W = 'White'

class Othello_board:
    def __init__(self):
        self._design_window = tkinter.Toplevel()
        self.row = tkinter.IntVar()
        self.col = tkinter.IntVar()
        self.first_color = tkinter.StringVar()
        self.TL_color = tkinter.StringVar()
        self.win_method = tkinter.StringVar()
        self._set_label()
        self._set_button()
        OK_button = tkinter.Button(self._design_window,
                                   text = 'OK',
                                   font = (DEFAULT_FONT),
                                   command = self.display)
        OK_button.grid(row = 10,
                       column = 8,
                       sticky = tkinter.E+tkinter.S)

        self._design_window.rowconfigure(0,weight = 1)
        self._design_window.rowconfigure(1,weight = 1)
        self._design_window.rowconfigure(2,weight = 1)
        self._design_window.rowconfigure(3,weight = 1)
        self._design_window.rowconfigure(4,weight = 1)
        self._design_window.rowconfigure(5,weight = 1)
        self._design_window.rowconfigure(6,weight = 1)
        self._design_window.rowconfigure(7,weight = 1)
        self._design_window.rowconfigure(8,weight = 1)
        self._design_window.rowconfigure(9,weight = 1)
        self._design_window.rowconfigure(10,weight = 1)
        self._design_window.columnconfigure(0,weight = 1)
        self._design_window.columnconfigure(1,weight = 1)
        self._design_window.columnconfigure(2,weight = 1)
        self._design_window.columnconfigure(3,weight = 1)
        self._design_window.columnconfigure(4,weight = 1)
        self._design_window.columnconfigure(5,weight = 1)
        self._design_window.columnconfigure(6,weight = 1)
        self._design_window.columnconfigure(7,weight = 1)
        self._design_window.columnconfigure(8,weight = 1)


        
    def _set_label(self):
        row_label = tkinter.Label(self._design_window,
                                  text = 'How many rows on the board?',
                                  font = (DEFAULT_FONT))
        row_label.grid(row = 0,
                       column = 0,
                       columnspan = 8,
                       sticky = tkinter.W)
        col_label = tkinter.Label(self._design_window,
                                  text = 'How many columns on the board?',
                                  font = (DEFAULT_FONT))
        col_label.grid(row = 2,
                       column = 0,
                       columnspan = 8,
                       sticky = tkinter.W)
        sequence_label = tkinter.Label(self._design_window,
                                       text = 'Which color do you want to play first?',
                                       font = (DEFAULT_FONT))
        sequence_label.grid(row = 4,
                            column = 0,
                            columnspan = 8,
                            sticky = tkinter.W)
        T_L_label = tkinter.Label(self._design_window,
                                  text = 'Which color do you want to place on the top left of the first four discs?',
                                  font = (DEFAULT_FONT))
        T_L_label.grid(row = 6,
                       column = 0,
                       columnspan = 8,
                       sticky = tkinter.W)
        win_method_label = tkinter.Label(self._design_window,
                                         text = 'How to win?',
                                         font = (DEFAULT_FONT))
        win_method_label.grid(row = 8,
                              column = 0,
                              columnspan = 8,
                              sticky = tkinter.W)

    def _set_button(self):
        self._set_r_and_c(self.row,1)
        self._set_r_and_c(self.col,3)
        self._set_w_and_b(self.first_color,5)
        self._set_w_and_b(self.TL_color,7)
        self._set_method(9)
        

    def _set_r_and_c(self,num,row_num):
        num.set(4)
        for i in Row_and_Col:
            radiobutton = tkinter.Radiobutton(self._design_window,
                                              text = i,
                                              value = i,
                                              variable = num)
            radiobutton.grid(row = row_num,
                             column = Row_and_Col.index(i),
                             sticky = tkinter.W)

    def _set_w_and_b(self,color,row_num):
        color.set(B)
        whitebutton = tkinter.Radiobutton(self._design_window,
                                          text = W,
                                          value = W,
                                          variable = color)
        whitebutton.grid(row = row_num,
                         column = 1,
                         sticky = tkinter.W)
        blackbutton = tkinter.Radiobutton(self._design_window,
                                          text = B,
                                          value = B,
                                          variable = color)
        blackbutton.grid(row = row_num,
                         column = 0,
                         sticky = tkinter.W)

    def _set_method(self,row_num):
        self.win_method.set(1)
        H_button = tkinter.Radiobutton(self._design_window,
                                       text = 'Highest',
                                       value = 1,
                                       variable = self.win_method)
        H_button.grid(row = row_num,
                      column = 0,
                      sticky = tkinter.W)
        L_button = tkinter.Radiobutton(self._design_window,
                                       text = 'Lowest',
                                       value = 2,
                                       variable = self.win_method)
        L_button.grid(row = row_num,
                      column = 1,
                      sticky = tkinter.W)


    def display(self):
        '''Displays the game board in GUI'''
        self.row = self.row.get()
        self.col = self.col.get()
        self.first_color = self.first_color.get()
        self.TL_color = self.TL_color.get()
        self.win_method = self.win_method.get()
        self._design_window.destroy()
        game = Othello.Othello(self.row,self.col,self.first_color,self.TL_color,self.win_method)
        Othello_GUI.Othello_GUI(game)
