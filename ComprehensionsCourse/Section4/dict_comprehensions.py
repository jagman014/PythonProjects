# Example
import os

current_directory = os.path.dirname(__file__)
file = os.path.relpath('..\exercise-files\linux-etc-passwd.txt',
                       current_directory)

dictionary = {line.split(':')[0]: line.split(':')[2]
              for line in open(file)
              if line.strip() and not line.startswith('#')}
# only creates one dictionary, {[key]: [value]}

print(dictionary)

words = 'this is a bunch of words'

words_dict = {word: len(word)
              for word in words.split()}

print(words_dict)

vowel_words = {word: len(word)
               for word in words.split()
               if word.startswith(('a', 'e', 'i', 'o', 'u'))}
# .startswith can take a tuple of values

print(vowel_words)
