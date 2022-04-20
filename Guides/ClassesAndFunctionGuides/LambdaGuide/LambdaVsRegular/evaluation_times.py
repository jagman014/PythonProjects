# standard functions
def wrap(n):
    def f():
        print(n)

    return f


numbers = 'one', 'two', 'three'

funcs = []

for n in numbers:
    funcs.append(wrap(n))

for f in funcs:
    f()

# n is evaluated at definition time when it's added to the list

# contrast with lambda
funcs = []

for n in numbers:
    funcs.append(lambda: print(n))

for f in funcs:
    f()
# now n is bound to lambda at execution time
# fixed by assignment of n at definition time
funcs = []

for n in numbers:
    funcs.append(lambda n=n: print(n))

for f in funcs:
    f()
