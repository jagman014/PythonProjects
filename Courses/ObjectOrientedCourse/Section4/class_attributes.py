# Example

class Person:
    population = 0
    # anything defined within the class is an attribute, known as a class attribute
    # is shared between the class and any instances of the class

    def __init__(self, name):
        Person.population += 1
        # must be an attribute within the method, don't define as self.attribute
        # it will only change the instance attribute not the class attribute
        self.name = name


print(f'Before, population: {Person.population}')

p_1 = Person('name_1')
p_2 = Person('name_2')

print(f'After, population: {Person.population}')
print(f'After, p_1.population: {p_1.population}')

# if asking for a.b:
# (1) look for 'b' attribute on 'a'
# (2) look for 'b' attribute on type(a)
# (3) look for 'b' attribute on object
