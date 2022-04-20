# Example
class Foo:
    pass


f = Foo()

print(vars(f))

# non-inherited attributes
# dont do this, not good form
f.x = 100
f.y = [10, 20, 30]

print(dir(f))
print(vars(f))
