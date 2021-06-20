# Example
class Foo:
    def __init__(self):  # init has an implicit return function
        self.x = 100  # define all attributes within __init__
        self.y = [10, 20, 30]


f = Foo()
print(vars(f))
