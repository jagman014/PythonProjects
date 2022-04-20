# Exercises
import os


# (1)
def word_score(word):
    return sum([ord(letter) - 96
                for letter in word.lower()])


sentence = input('Enter a sentence: ').split()

scores = {word: word_score(word)
          for word in sentence}

print(f'You scored: {scores}')

# (2)
sentence_1 = input('Enter a sentence: ').split()

scores_1 = {word: word_score(word)
            for word in sentence_1
            if 3 < len(word) < 7}

print(f'You scored for words with 3 < letters < 7: {scores_1}')

# (3)
test_dict = {'a': 1, 'b': 2, 'c': 3}

flipped_dict = {value: key
                for key, value in test_dict.items()}

print(flipped_dict)

# (4)
current_directory = os.path.dirname(__file__)
file = os.path.relpath('..\exercise-files\words',
                       current_directory)

words_set = {word.strip()
             for word in open(file)}

sentence_2 = input('Enter a sentence: ')

words_dict = {word: word in words_set
              for word in sentence_2.split()}

print(words_dict)
