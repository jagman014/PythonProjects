import tkinter as tk
from tkinter import font

from settings import Move
from tic_tac_toe_game import TicTacToeGame


class TicTacToeBoard(tk.Tk):
    def __init__(self, game: TicTacToeGame):
        super().__init__()

        self.title('Tic Tac Toe Game')
        self._cells = {}
        self._game = game

        self._create_menu()
        self._create_board_display()
        self._create_board_grid()

    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)

        self.display = tk.Label(
            master=display_frame,
            text='Ready?',
            font=font.Font(size=28, weight='bold'),
        )
        self.display.pack()

    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()

        for row in range(self._game.board_size):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)

            for col in range(self._game.board_size):
                button = tk.Button(
                    master=grid_frame,
                    text='',
                    font=font.Font(size=36, weight='bold'),
                    fg='black',
                    width=3,
                    height=1,
                    highlightbackground='lightblue',
                )

                self._cells[button] = (row, col)
                button.bind('<ButtonPress-1>', self.play)

                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky='nsew',
                )

    def play(self, event: tk.Event):
        clicked_btn = event.widget
        row, col = self._cells[clicked_btn]
        move = Move(row, col, self._game.current_player.label)

        if self._game.is_valid_move(move):
            self._update_button(clicked_btn)
            self._game.process_move(move)

            if self._game.is_tied():
                self._update_display(msg='Tied Game', colour='red')

            elif self._game.has_winner():
                self._highlight_cells()
                msg = f'Player "{self._game.current_player.label}" won!'
                colour = self._game.current_player.colour
                self._update_display(msg, colour)

            else:
                self._game.toggle_player()
                msg = f"{self._game.current_player.label}'s turn"
                self._update_display(msg)

    def _update_button(self, clicked_btn: tk.Widget):
        clicked_btn.config(text=self._game.current_player.label)
        clicked_btn.config(fg=self._game.current_player.colour)

    def _update_display(self, msg: str, colour: str='black'):
        self.display['text'] = msg
        self.display['fg'] = colour

    def _highlight_cells(self):
        for button, coordinates in self._cells.items():
            if coordinates in self._game.winner_combo:
                button.config(highlightbackground='red')

    def _create_menu(self):
        menu_bar = tk.Menu(master=self)
        self.config(menu=menu_bar)

        file_menu = tk.Menu(master=menu_bar)
        file_menu.add_command(
            label='Play again',
            command=self.reset_board
        )
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=quit)

        menu_bar.add_cascade(label='File', menu=file_menu)

    def reset_board(self):
        self._game.reset_game()
        self._update_display(msg='Ready?')

        for button in self._cells.keys():
            button.config(highlightbackground='lightblue')
            button.config(text='')
            button.config(fg='black')
