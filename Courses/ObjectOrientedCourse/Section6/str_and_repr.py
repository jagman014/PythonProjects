# Example

class Foo:
    def __init__(self, x):
        self.x = x

    def __len__(self):
        return len(self.x)

    # __str__ used for str() representation for common usage
    def __str__(self):
        return f'[str] I\'m a Foo, with vars = {vars(self)}'

    # __repr__ used for repr() representation for developed usage
    # can alternatively have just __repr__ as it can be used in place of __str__
    def __repr__(self):
        return f'[repr] I\'m a Foo, with vars = {vars(self)}'


f = Foo('abcd')
print(len(f))

print(f)  # calls str(f) -> f.__str__()
# similar concept for f'' strings

print(repr(f))  # repr is from evaluative lines of code
