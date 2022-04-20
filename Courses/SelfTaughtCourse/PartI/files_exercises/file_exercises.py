import os

directory = os.path.dirname(__file__)
filename = os.path.join(directory, 'test.txt')

with open(filename, 'r', encoding='utf-8') as fin:
    print(fin.read())

filename_2 = os.path.join(directory, 'answers.txt')
ans = input("What is your answer? ")

with open(filename_2, 'a', encoding='utf-8') as fout:
    fout.write(f'{ans.title()}\n')
