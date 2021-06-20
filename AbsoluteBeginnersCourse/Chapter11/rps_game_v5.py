# Example code from chapter 11
import datetime
import random
import json
import os
from colorama import Fore, init

init()

rolls = {}


def main():
    try:
        print(Fore.WHITE)
        log('App starting up...')
        load_rolls()
        show_header()
        show_leaderboard()

        player_1, player_2 = get_players()
        log(f'{player_1} has logged in.')

        play_game(player_1, player_2)
        log('Game Over.')

    except json.decoder.JSONDecodeError as je:
        print(Fore.RED + '\nError: The file "rolls.json" is an invalid JSON.' + Fore.WHITE)
        print(Fore.RED + f'Error: {je}.' + Fore.WHITE)
    except FileNotFoundError as fe:
        print(Fore.RED + '\nError: "rolls.json" not found.' + Fore.WHITE)
        print(Fore.RED + f'Error: {fe}.' + Fore.WHITE)
    except KeyboardInterrupt:
        print(Fore.LIGHTCYAN_EX + '\nYou exiting? Goodbye then.' + Fore.WHITE)
    except Exception as x:
        print(Fore.RED + f'Unknown error: {x}' + Fore.WHITE)


def show_header():
    print(Fore.LIGHTMAGENTA_EX)
    print('------------------------------')
    print('Rock, Paper, Scissors v5')
    print('Error Handling Edit')
    print('------------------------------')
    print(Fore.WHITE)


def show_leaderboard():
    leaders = load_leaders()

    sorted_leaders = list(leaders.items())
    sorted_leaders.sort(key=lambda l: l[1], reverse=True)

    print("TOP 5 LEADERS:\n")
    for name, wins in sorted_leaders[0:5]:
        print(f'{wins:,} -- {name}')
    print('------------------------------\n')


def get_players():
    p1 = input('Player 1: What is your name? ')
    p2 = 'CPU'

    return p1, p2


def play_game(player_1, player_2):
    log(f'New game starting between {player_1} and {player_2}.')

    round_count = 0
    wins = {player_1: 0, player_2: 0}
    roll_names = list(rolls.keys())

    while not find_winner(wins, wins.keys()):
        roll_1 = get_roll(player_1, roll_names)
        roll_2 = random.choice(roll_names)

        if not roll_1:
            print(Fore.LIGHTRED_EX + 'Please try again.')
            print(Fore.WHITE)
            continue

        log(f'Round {round_count}: {player_1} roll(s) {roll_1} and {player_2} roll(s) {roll_2}.')
        print(Fore.YELLOW + f'{player_1} roll(s) {roll_1}')
        print(Fore.CYAN + f'{player_2} roll(s) {roll_2}')
        print(Fore.WHITE)

        winner = check_for_winning_throw(player_1, player_2, roll_1, roll_2)

        if winner is None:
            msg = 'The round was a tie'
            print(msg)
            log(msg)
        else:
            msg = f'{winner} win(s)!'
            fore = Fore.GREEN if winner == player_1 else Fore.LIGHTRED_EX
            print(fore + msg + Fore.WHITE)
            log(msg)
            wins[winner] += 1

        round_count += 1

        msg = f'Score after {round_count} round(s): {player_1} - {wins[player_1]}; {player_2} - {wins[player_2]}.'
        print(msg + '\n')
        log(msg)

    overall_winner = find_winner(wins, wins.keys())
    msg = f'{overall_winner} win(s) the game!'
    fore = Fore.GREEN if overall_winner == player_1 else Fore.LIGHTRED_EX
    print(fore + msg + Fore.WHITE)
    log(msg)
    record_win(overall_winner)


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
    try:
        print(f"Available rolls: ")
        for index, r in enumerate(roll_names, start=1):
            print(f'{index}) {r}')

        text = input(f"{player_name}, what is your roll? ")
        if text is None or not text.strip():
            print("You must enter a response!")
            return None

        selected_index = int(text.strip()) - 1

        if selected_index < 0 or selected_index >= len(roll_names):
            print(f'Sorry {player_name}, {text} is not valid!')
            return None

        return roll_names[selected_index]

    except ValueError as ve:
        print(Fore.RED + f"Could not convert to integer: {ve}." + Fore.WHITE)
        return None


def load_rolls():
    global rolls

    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'rolls.json')

    with open(filename, 'r', encoding='utf-8') as fin:
        rolls = json.load(fin)

    log(f'Loaded rolls: {list(rolls.keys())} from {os.path.basename(filename)}.')


def load_leaders():
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'leaderboard.json')

    if not os.path.exists(filename):
        return {}

    with open(filename, 'r', encoding='utf-8') as fin:
        return json.load(fin)


def record_win(winner_name):
    leaders = load_leaders()

    if winner_name in leaders:
        leaders[winner_name] += 1
    else:
        leaders[winner_name] = 1

    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'leaderboard.json')

    with open(filename, 'w', encoding='utf-8') as fout:
        json.dump(leaders, fout)


# Use a library for real logging, i.e. logbook
def log(msg):
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'rps.log')
    time_text = datetime.datetime.now().strftime('%c')

    with open(filename, 'a', encoding='utf-8') as fout:
        fout.write(f'[{time_text}] ')
        fout.write(msg)
        fout.write('\n')


if __name__ == '__main__':
    main()
