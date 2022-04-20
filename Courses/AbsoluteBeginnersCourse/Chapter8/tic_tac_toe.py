# Example code from Chapter 8

# Choose the players
# Create the board
# Choose an initial player
# Until someone wins, check for winner
#   Show the board
#   Choose a location, mark it
#   Toggle active player

# Game over, active player won


def main():
    print('\nWelcome to TIC TAC TOE\n')

    # Board is a list of rows
    # Rows are a list of cells
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

    # Define players
    active_player_index = 0
    players = ["Jag", "CPU"]
    symbols = ["O", "X"]
    player = players[active_player_index]

    # Game start
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
    row = int(input('Choose a row: ')) - 1
    column = int(input('Choose a column: ')) - 1

    # Move validation
    if row < 0 or row >= len(board):
        return False
    if column < 0 or column >= len(board[0]):
        return False

    cell = board[row][column]
    if cell is not None:
        return False

    # Playing move
    board[row][column] = symbol
    return True


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
    rows = board
    sequences.extend(rows)

    # Win by columns
    for col_idx in range(0, 3):
        col = [
            board[0][col_idx],
            board[1][col_idx],
            board[2][col_idx],
        ]
        sequences.append(col)

    # Win by diagonals
    diagonals = [
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    sequences.extend(diagonals)

    return sequences


if __name__ == '__main__':
    main()
