# Example

class Foo:
    def __init__(self, x):
        self.x = x

    def x2(self):
        return self.x * 2  # require self.x to use variables between methods

    def get_x(self):
        return self.x

    def set_x(self, new_x):
        self.x = new_x


f = Foo(10)
print(vars(f))

# invokes the method x2 on the object f
# similar to Foo.x2(f)
print(f.x2())

print(f.get_x())

f.set_x(20)
print(f.get_x())


# more python-like method
class Bar:
    def __init__(self, x):
        self.x = x


# no need for getter / setter methods
# because there are no private methods

b = Bar(10)
print(b.x)

b.x = 20
print(b.x)
