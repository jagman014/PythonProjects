import os
import random


def main():
    word = get_word()

    wrong = 0
    stages = ['',
              '____________',
              '|',
              '|      |',
              '|      0',
              '|     /|\\',
              '|     / \\',
              '|',
              '____________'
              ]
    remaining_letters = list(word)
    board = ["_"] * len(word)
    win = False
    print('Welcome to Hangman')
    print(' '.join(board))

    while wrong < len(stages) - 1:
        print('\n')
        character = input('Guess a letter: ')

        if character in remaining_letters:
            while character in remaining_letters:
                character_idx = remaining_letters.index(character)
                board[character_idx] = character
                remaining_letters[character_idx] = '#'
        else:
            wrong += 1

        print((' '.join(board)))

        stage_count = wrong + 1
        print('\n'.join(stages[:stage_count]))

        if "_" not in board:
            print("You win!")
            print('The word was: ' + ''.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages))
        print(f"You lose! The word was: {word}")


def get_word():
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'words.txt')

    with open(filename, 'r', encoding='utf-8') as fin:
        words = list(fin)

    idx = random.randint(0, len(words) - 1)
    word = words[idx].lower().strip()
    return word


if __name__ == '__main__':
    main()
