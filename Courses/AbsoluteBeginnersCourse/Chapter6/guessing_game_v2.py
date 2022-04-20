# Exercise from Chapter 6
import random


def main():
    show_header()
    play_game()


def show_header():
    print('----------------------------')
    print('     M&M Guessing Game v2')
    print('----------------------------')
    print("Guess the number of M&Ms and you get a free lunch!\n")


def play_game():
    mm_count = random.randint(1, 100)
    attempt_limit = 5
    attempts = 0
    while attempts < attempt_limit:
        guess = int(input('How many M&Ms are in the jar? '))
        attempts += 1

        if mm_count == guess:
            print(f'You won the free lunch!! It was {guess}.')
            break
        elif mm_count < guess:
            print("Sorry that's too HIGH!")
        else:
            print("Sorry that's too LOW!")
    print(f"Bye, there were {mm_count} M&Ms, you're done in {attempts} tries!")


if __name__ == '__main__':
    main()
