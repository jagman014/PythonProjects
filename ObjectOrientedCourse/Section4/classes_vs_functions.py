# Example
print('A')


class Person:
    print('B')  # each line within the class is run line by line

    def __init__(self, name):
        print('C')  # only occurs when method is run, i.e. when we call the class
        self.name = name

    print('D')

    def greet(self):
        return f'Hello, {self.name.title()}'


print('E')

p_1 = Person('name_1')
p_2 = Person('name_2')

print(p_1.greet())
print(p_2.greet())

# order A -> B -> D -> E -> C -> C
