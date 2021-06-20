# Example code from chapter 7
import random

rolls = {
    'rock': {
        'defeats': ['scissors'],
        'defeated_by': ['paper'],
    },
    'paper': {
        'defeats': ['rock'],
        'defeated_by': ['scissors'],
    },
    'scissors': {
        'defeats': ['paper'],
        'defeated_by': ['rock'],
    },
}


def main():
    show_header()
    play_game('You', 'CPU')


def show_header():
    print('------------------------------')
    print('Rock, Paper, Scissors v2')
    print('Data Structures Edit')
    print('------------------------------')


def play_game(player_1, player_2):
    round_count = 0
    wins = {player_1: 0,
            player_2: 0,
            }

    roll_names = list(rolls.keys())

    while not find_winner(wins, wins.keys()):
        roll_1 = get_roll(player_1, roll_names)
        roll_2 = random.choice(roll_names)

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
            wins[winner] += 1

        round_count += 1

        print(f'Score after {round_count} round(s): {player_1} - {wins[player_1]}; {player_2} - {wins[player_2]}.\n')

    overall_winner = find_winner(wins, wins.keys())
    print(f'{overall_winner} win(s) the game!')


def find_winner(wins, names):
    best_of = 3
    for name in names:
        if wins.get(name, 0) >= best_of:
            return name

    return None


def check_for_winning_throw(player_1, player_2, roll_1, roll_2):
    winner = None
    if roll_1 == roll_2:
        winner = None

    outcome = rolls.get(roll_1, {})
    if roll_2 in outcome.get('defeats'):
        return player_1
    elif roll_2 in outcome.get('defeated_by'):
        return player_2

    return winner


def get_roll(player_name, roll_names):
    print('Available rolls:')
    for index, r in enumerate(roll_names, start=1):
        print(f'{index}. {r}')

    selected_index = int(input(f'{player_name}, what is your roll?: ')) - 1

    if selected_index not in [0, 1, 2]:
        print(f'Sorry {player_name}, {selected_index + 1} is put of bounds!')
        return None

    return roll_names[selected_index]


if __name__ == '__main__':
    main()
