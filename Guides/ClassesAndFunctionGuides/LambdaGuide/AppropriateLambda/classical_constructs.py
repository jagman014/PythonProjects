from functools import reduce

# map function
print(list(map(lambda x: x.upper(), ['cat', 'dog', 'cow'])))

# filter function
print(list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow'])))

# functools.reduce() function
print(reduce(lambda acc, x: f'{acc} | {x}', ['cat', 'dog', 'cow']))
