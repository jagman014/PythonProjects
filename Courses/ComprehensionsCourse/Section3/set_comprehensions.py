# Example
import os

current_directory = os.path.dirname(__file__)
file = os.path.relpath('..\exercise-files\mini-access-log.txt',
                       current_directory)

unique_ips = {line.split()[0]
              for line in open(file)}
# a set is the keys from a dictionary therefore must be unique

print(unique_ips)

words = 'this is a bunch of words and a bunch of words this is'

unique_words = {len(word)
                for word in words.split()}
# cannot have a non-hashable object in a set i.e. a list

print(unique_words)
