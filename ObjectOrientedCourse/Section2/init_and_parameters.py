# Example
class Foo:
    def __init__(self, x=888, y=999):  # can assign default values if none provided
        self.x = x  # self.attribute = local variable
        self.y = y


f = Foo(10, 20)

print(vars(f))

g = Foo()
print(vars(g))


class Foo1:
    def __init__(self, x, *args):  # can use *args and **kwargs inside __init__
        self.x = x
        self.args = args


h = Foo1(10, 20, 30, 40)

print(vars(h))
