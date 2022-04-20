# Example code from chapter 6
import random


def main():
    show_header()
    play_game('You', 'CPU')


def show_header():
    print('------------------------------')
    print('Rock, Paper, Scissors v1')
    print('------------------------------')


def play_game(player_1, player_2):
    best_of = 3
    round_count = 0
    wins_p1 = 0
    wins_p2 = 0

    rolls = ['rock', 'paper', 'scissors']

    while wins_p1 < best_of and wins_p2 < best_of:
        roll_1 = get_roll(player_1, rolls)
        roll_2 = random.choice(rolls)

        if not roll_1:
            print('Please try again.')
            continue

        print(f'{player_1} roll(s) {roll_1}')
        print(f'{player_2} roll(s) {roll_2}')

        winner = check_for_winning_throw(player_1, player_2, roll_1, roll_2)

        if winner is None:
            print('The round was a tie')
        else:
            print(f'{winner} win(s)!')
            if winner == player_1:
                wins_p1 += 1
            elif winner == player_2:
                wins_p2 += 1
        round_count += 1

        print(f'Score after {round_count} round(s): {player_1} - {wins_p1}; {player_2} - {wins_p2}.\n')

    if wins_p1 >= best_of:
        overall_winner = player_1
    else:
        overall_winner = player_2

    print(f'{overall_winner} win(s) the game!')


def check_for_winning_throw(player_1, player_2, roll_1, roll_2):
    # Rock
    #       Rock -> tie
    #       Paper -> lose
    #       Scissors -> win
    # Paper
    #       Rock -> win
    #       Paper -> tie
    #       Scissors -> lose
    # Scissors
    #       Rock -> lose
    #       Paper -> win
    #       Scissors -> tie
    winner = None
    if roll_1 == roll_2:
        winner = None
    elif roll_1 == 'rock':
        if roll_2 == 'paper':
            winner = player_2
        elif roll_2 == 'scissors':
            winner = player_1
    elif roll_1 == 'paper':
        if roll_2 == 'scissors':
            winner = player_2
        elif roll_2 == 'rock':
            winner = player_1
    elif roll_1 == 'scissors':
        if roll_2 == 'rock':
            winner = player_2
        elif roll_2 == 'paper':
            winner = player_1
    return winner


def get_roll(player_name, rolls):
    print('Available rolls:')
    for index, r in enumerate(rolls, start=1):
        print(f'{index}. {r}')

    selected_index = int(input(f'{player_name}, what is your roll?: ')) - 1

    if selected_index not in [0, 1, 2]:
        print(f'Sorry {player_name}, {selected_index+1} is put of bounds!')
        return None

    return rolls[selected_index]


if __name__ == '__main__':
    main()
