import collections
from pprint import pprint

Scientist = collections.namedtuple('Scientist', ['name', 'field', 'born', 'nobel'])

ada_l = Scientist(name='Ada Lovelace', field='maths', born=1815, nobel=False)
emmy = Scientist(name='Emmy Noether', field='maths', born=1882, nobel=False)
marie = Scientist(name='Marie Curie', field='physics', born=1867, nobel=True)
tu = Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True)
ada_y = Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True)
vera = Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False)
sally = Scientist(name='Sally Ride', field='physics', born=1951, nobel=False)

scientists = (ada_l, emmy, marie, tu, ada_y, vera, sally)


def nobel_filter(x):
    return x.nobel is True


fs = tuple(filter(nobel_filter, scientists))
pprint(fs)
print()

# More python-like solution with 'list'-comprehensions
fs_1 = tuple(x for x in scientists if x.field == 'chemistry')
pprint(fs_1)
print()
