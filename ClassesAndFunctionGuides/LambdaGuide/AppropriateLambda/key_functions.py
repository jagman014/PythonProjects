# higher order functions that take a variable 'key', i.e. sorted()
ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']

print(sorted(ids))  # Lexicographic sort

# lambda function feeds the numeric part of the strings to the sorting key
sorted_ids = sorted(ids, key=lambda x: int(x[2:]))  # Integer sort
print(sorted_ids)
