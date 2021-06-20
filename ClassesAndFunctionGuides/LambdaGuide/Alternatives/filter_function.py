# filter function, requires boolean function
even = lambda x: x % 2 == 0
print(list(filter(even, range(11))))

# list comprehension version
print([x for x in range(11) if x % 2 == 0])
