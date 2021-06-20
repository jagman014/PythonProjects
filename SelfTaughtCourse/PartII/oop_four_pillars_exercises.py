class Shape:
    def what_am_i(self):
        print(f'I am a {self.__class__.__name__}')


class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return (2 * self.width) + (2 * self.length)


class Square(Rectangle):
    def __init__(self, l):
        super().__init__(l, l)

    def change_size(self, inc):
        self.length = self.length + inc


rectangle = Rectangle(2, 4)
print(rectangle.calculate_perimeter())

square = Square(4)
print(square.calculate_perimeter())

square.change_size(2)
print(square.length)

square.change_size(-3)
print(square.length)

square.what_am_i()
rectangle.what_am_i()
