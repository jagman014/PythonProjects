names = ['Louvre', 'Diagon Alley', 'Saturn V', 'Millennium Falcon', 'NYC']
set_numbers = ['21024', '75978', '92176', '75192', '21028']
num_pieces = [695, 5544, 1969, 7541, 598]

print(zip(names, set_numbers, num_pieces))
print(list(zip(names, set_numbers, num_pieces)))

set_numbers = set_numbers[:-1]
# zipped sequence with missing item
print(list(zip(names, set_numbers, num_pieces)))

# throws error if missmatched lengths
#print(list(zip(names, set_numbers, num_pieces, strict=True)))

from itertools import zip_longest
from textwrap import fill

# fills missing with None
print(list(zip_longest(names, set_numbers, num_pieces)))

# can fill with own value
print(list(zip_longest(names, set_numbers, num_pieces, fillvalue=0)))
