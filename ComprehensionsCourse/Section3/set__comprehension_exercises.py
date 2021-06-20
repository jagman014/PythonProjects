# Exercises
import os

# (1)
numbers = input('Enter a list of integers separated by spaces: ').split()

unique_sum = sum({int(number)
                  for number in numbers})

print(f'Here is a sum of the unique numbers entered: {unique_sum}')

# (2)
current_directory = os.path.dirname(__file__)
file = os.path.relpath('..\exercise-files\\nums.txt',
                       current_directory)

unique_sum_1 = sum({int(num)
                    for num in open(file)
                    if num.strip()})

print(unique_sum_1)

# (3)
file_1 = os.path.relpath('..\exercise-files\linux-etc-passwd.txt',
                         current_directory)

unique_shells = {line.strip().split(':')[-1]
                 for line in open(file_1)
                 if line.strip() and not line.startswith('#')}

print(unique_shells)
