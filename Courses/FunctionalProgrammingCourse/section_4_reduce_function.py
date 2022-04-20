import collections
from pprint import pprint
from functools import reduce
import itertools


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

names_and_ages = tuple(NameAndAge(name=x.name, age=(2020 - x.born)) for x in scientists)

total_age = reduce(lambda acc, val: acc + val.age, names_and_ages, 0)
print(total_age)

# More python-like way
total_age_1 = sum(x.age for x in names_and_ages)
print(total_age_1)


def reducer(acc, val):
    acc[val.field].append(val.name)
    return acc


scientists_by_field = reduce(reducer, scientists, {'maths': [], 'physics': [], 'chemistry': [], 'astronomy': []})
pprint(scientists_by_field)

# Better option
scientists_by_field_1 = reduce(reducer, scientists, collections.defaultdict(list))
pprint(scientists_by_field_1)

# Another option
scientists_by_field_2 = {item[0]: list(item[1]) for item in itertools.groupby(scientists, lambda x: x.field)}
pprint(scientists_by_field_2)

# Yet another
scientists_by_field_3 = reduce(lambda acc, val: {**acc, **{val.field: acc[val.field] + [val.name]}}, scientists,
                               {'maths': [], 'physics': [], 'chemistry': [], 'astronomy': []})
pprint(scientists_by_field_3)
