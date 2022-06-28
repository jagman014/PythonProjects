from settings import PLAYERS, BOARD_SIZE
from tic_tac_toe_board import TicTacToeBoard
from tic_tac_toe_game import TicTacToeGame


def main():
    game = TicTacToeGame(PLAYERS, BOARD_SIZE)
    board = TicTacToeBoard(game)
    board.mainloop()


if __name__ == '__main__':
    main()
