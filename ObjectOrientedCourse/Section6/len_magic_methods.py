# Example

# Magic methods form of -> __(method)__
class Foo:
    def __init__(self, x):
        self.x = x

    # need magic method as you can't get obtain len(class) properly without
    # __len__ is required to return an integer type
    def __len__(self):
        return len(self.x)


f = Foo('abcd')
print(len(f))
