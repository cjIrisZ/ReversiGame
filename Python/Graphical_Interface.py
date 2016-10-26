#### Chenjunni Zeng ICS 32 Project 5
#### Graphical_Interface

import Othello
import tkinter
import Design_board

DEFAULT_FONT = ('Helvetica', 20)

class OthelloApplication:
    def __init__(self):
        self._root_window = tkinter.Tk()
        _welcome_label = tkinter.Label(self._root_window,
                              text = 'Welcome to Othello Game!',
                              font = (DEFAULT_FONT))
        _welcome_label.grid(row=0,
                           column=0,
                           columnspan=2,
                           sticky=tkinter.E+tkinter.W)
        _start_button = tkinter.Button(self._root_window,
                                      text = 'Start Game',
                                      font = (DEFAULT_FONT),
                                      command = self._design_game)
        _start_button.grid(row=1,column=0,sticky=tkinter.W+tkinter.E)

        self._root_window.rowconfigure(0,weight = 1)
        self._root_window.rowconfigure(1,weight = 1)
        self._root_window.columnconfigure(0,weight = 1)

    def start(self):
        self._root_window.mainloop()

    def _design_game(self):
        Design_board.Othello_board()


if __name__ == '__main__':
    OthelloApplication().start()
