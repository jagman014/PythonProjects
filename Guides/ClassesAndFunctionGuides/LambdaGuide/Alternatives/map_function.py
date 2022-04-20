# map() function, returns an iterable
print(list(map(lambda x: x.capitalize(), ['cat', 'dog', 'cow'])))

# list comprehension version
print([x.capitalize() for x in ['cat', 'dog', 'cow']])
