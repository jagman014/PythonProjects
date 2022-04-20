# Example of a list comprehension
squares = [x * x for x in range(10)]
print(squares)

# As a for-loop:
squares_1 = []

for x in range(10):
    squares_1.append(x * x)

print(squares_1)

# General Form of: (values) = [ (expression) for (value) in (collection) if (conditional) ]
# Transforms into:
# (values) = []
# for (value) in (collection):
#     if (conditional):
#         (values).append( (expression) )

# Filtering:
even_squares = [x * x for x in range(10) if x % 2 == 0]
print(even_squares)

# As a for-loop
even_squares_1 = []

for x in range(10):
    if x % 2 == 0:
        even_squares_1.append(x * x)

print(even_squares_1)

# Good format:
# (values) = [ (expression)
#              for (value) in (collection)
#              if (conditional) ]
