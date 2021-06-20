# Exercises 1 & 2
class Square:
    square_list = []

    def __init__(self, l):
        self.length = l
        self.square_list.append((self.length, self.length))

    def __repr__(self):
        return f'Side lengths of {self.length} by {self.length}'


square = Square(5)
print(square)
print(square.square_list)


# Exercise 3
def compare(object_1, object_2):
    return object_1 is object_2


print(compare('a', 'b'))
print(compare('a', 'a'))
