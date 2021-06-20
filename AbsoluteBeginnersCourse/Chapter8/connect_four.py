# Exercise from Chapter 8


def main():
    print('\nWelcome to Connect 4!\n')

    board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
    ]

    active_player_index = 0
    players = ["P1", "P2"]
    symbols = ["O", "X"]
    player = players[active_player_index]

    while not find_winner(board):
        player = players[active_player_index]
        symbol = symbols[active_player_index]

        announce_turn(player)
        show_board(board)
        if not choose_play(board, symbol):
            print("That's not an option, try again.")
            continue

        active_player_index = (active_player_index + 1) % len(players)

    print(f'\nGame Over! {player} has won with the board: ')
    show_board(board)
    print()


def choose_play(board, symbol):
    column = int(input('Choose a column: ')) - 1
    # Move validation
    if column < 0 or column >= len(board[0]):
        return False

    columns = []
    for col_idx in range(0, 7):
        col = [
            board[5][col_idx],
            board[4][col_idx],
            board[3][col_idx],
            board[2][col_idx],
            board[1][col_idx],
            board[0][col_idx],
        ]
        columns.append(col)

    col = columns[column]
    for index, cell in enumerate(col):
        if cell is None:
            idx = -1 - index
            board[idx][column] = symbol
            return True

    return False


def show_board(board):
    # Drawing board
    for row in board:
        print('| ', end='')
        for cell in row:
            symbol = cell if cell is not None else '_'
            print(symbol, end=' | ')
        print()


def announce_turn(player):
    print(f"\nIt's {player}'s turn. Here's the board:\n")


def find_winner(board):
    sequences = get_winning_sequences(board)

    for cells in sequences:
        symbol_1 = cells[0]
        if symbol_1 and all(symbol_1 == cell for cell in cells):
            return True

    return False


def get_winning_sequences(board):
    sequences = []

    # Win by rows
    for col_idx in range(0, 3):
        for row_idx in range(0, 6):
            col = [
                board[row_idx][col_idx],
                board[row_idx][col_idx + 1],
                board[row_idx][col_idx + 2],
                board[row_idx][col_idx + 3]
            ]
            sequences.append(col)

    # Win by columns
    for row_idx in range(0, 3):
        for col_idx in range(0, 7):
            col = [
                board[row_idx][col_idx],
                board[row_idx + 1][col_idx],
                board[row_idx + 2][col_idx],
                board[row_idx + 3][col_idx]
            ]
            sequences.append(col)

    # Win by diagonals
    for row_idx in range(0, 3):
        for col_idx in range(0, 4):
            l_diag = [
                board[row_idx][col_idx],
                board[row_idx + 1][col_idx + 1],
                board[row_idx + 2][col_idx + 2],
                board[row_idx + 3][col_idx + 3]
            ]
            sequences.append(l_diag)

    for row_idx in range(0, 3):
        for col_idx in range(1, 5):
            r_diag = [
                board[row_idx][-col_idx],
                board[row_idx + 1][-col_idx - 1],
                board[row_idx + 2][-col_idx - 2],
                board[row_idx + 3][-col_idx - 3]
            ]
            sequences.append(r_diag)

    return sequences


if __name__ == '__main__':
    main()
