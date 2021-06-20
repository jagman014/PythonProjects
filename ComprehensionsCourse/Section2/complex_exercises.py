# Complex Exercises
import math
import os
from collections import Counter

# (1)
numbers = input('Enter a few integers: ').split()

sum_factorials = sum([math.factorial(int(x))
                      for x in numbers])

print(f'Sum of the factorials: {sum_factorials}')

# (2)
current_directory = os.path.dirname(__file__)
file = os.path.relpath('..\exercise-files\mini-access-log.txt',
                       current_directory)
ips = [line.split()[0]
       for line in open(file)]  # closes automatically after comprehension

print(ips)

# (3)
count = Counter(ips)

for address, cnt in count.items():
    print(f'{address:.<20}{cnt}')

# (4)
file_1 = os.path.relpath('..\exercise-files\linux-etc-passwd.txt',
                         current_directory)

users = [tuple(line.split(':')[0:3:2])  # slice [start:end (exclusive):jump by]
         for line in open(file_1)
         if line.strip() and not line.startswith('#')]

print(users)
