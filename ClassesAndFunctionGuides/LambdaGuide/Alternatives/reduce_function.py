# reduce function
from functools import reduce

pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
print(reduce(lambda acc, pair: acc + pair[0], pairs, 0))

# generator expression version
print(sum(x[0] for x in pairs))

# slightly cleaner version, '_' is a convention for ignoring elements
print(sum(x for x, _ in pairs))
