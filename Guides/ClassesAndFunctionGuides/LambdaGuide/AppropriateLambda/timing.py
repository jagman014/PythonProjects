from timeit import timeit
from math import factorial

print(timeit("factorial(999)", "from math import factorial", number=10))

print(timeit(lambda: factorial(999), number=10))

# lambda functions can be slightly faster
# more useful within the console when testing code
