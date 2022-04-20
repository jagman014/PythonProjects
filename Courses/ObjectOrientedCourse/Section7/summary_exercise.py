# Exercise

class Animal:
    def __init__(self, colour, num_of_legs):
        self.species = self.__class__.__name__
        self.colour = colour
        self.num_of_legs = num_of_legs

    def __repr__(self):
        return (f'{self.colour.title()} {self.species},' +
                f' with {self.num_of_legs} legs')


class Wolf(Animal):
    def __init__(self, colour):
        super().__init__(colour, 4)


class Sheep(Animal):
    def __init__(self, colour):
        super().__init__(colour, 4)


class Snake(Animal):
    def __init__(self, colour):
        super().__init__(colour, 0)


class Parrot(Animal):
    def __init__(self, colour):
        super().__init__(colour, 2)


class Cage:
    def __init__(self, cage_id):
        self.cage_id = cage_id
        self.animals = []

    def add_animals(self, *new_animals):
        self.animals += new_animals

    def __repr__(self):
        return (f'Cage {self.cage_id}:\n' +
                '\n'.join(f'\t{index}) {animal}'
                          for index, animal in enumerate(self.animals, start=1)))


class Zoo:
    def __init__(self):
        self.cages = []

    def add_cages(self, *new_cages):
        self.cages += new_cages

    def animals_by_colour(self, colour):
        return (f'{colour.title()} animals:\n' +
                '\n'.join(f'\t{index}) {animal}'
                          for cage in self.cages
                          for index, animal in enumerate(cage.animals, start=1)
                          if colour.lower() in animal.colour))

    def number_of_legs(self):
        return str(sum(leg.num_of_legs
                       for cage in self.cages
                       for leg in cage.animals)) + ' legs'

    def __repr__(self):
        return 'Within Zoo:\n\n' + '\n'.join(str(cage)
                                             for cage in self.cages)


wolf = Wolf('black')
sheep_1 = Sheep('white')
sheep_2 = Sheep('white')
snake = Snake('brown')
parrot = Parrot('black')

print(wolf)
print(sheep_1)
print(sheep_2)
print(snake)
print(parrot)

c_1 = Cage(1)
c_1.add_animals(wolf, sheep_1, sheep_2)

c_2 = Cage(2)
c_2.add_animals(snake, parrot)

print(c_1)
print(c_2)

z = Zoo()
z.add_cages(c_1, c_2)
print(z)

print(z.animals_by_colour('black'))

print(z.number_of_legs())
