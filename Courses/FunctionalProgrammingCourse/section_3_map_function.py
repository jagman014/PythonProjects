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

NameAndAge = collections.namedtuple('NameAndAge', ['name', 'age'])

names_and_ages = tuple(map(lambda x: NameAndAge(name=x.name, age=(2020 - x.born)), scientists))
pprint(names_and_ages)
print()

# More python-like way
names_and_ages_1 = tuple(NameAndAge(name=x.name, age=(2020 - x.born)) for x in scientists)
pprint(names_and_ages_1)
