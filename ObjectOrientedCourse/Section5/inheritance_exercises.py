# Exercises

# (1)
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Hello, {self.name.title()}'


class VerbosePerson(Person):
    def greet(self):
        return f'Hello, {self.name.title()}! You\'re looking dapper today.'


alice = Person('alice')
bob = VerbosePerson('bob')

print(alice.greet())
print(bob.greet())


# (2)
class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add(self, name, price, quantity):
        if name in self.cart:
            self.cart[name][1] += quantity
        else:
            self.cart[name] = [price, quantity]

    def remove(self, name):
        if name in self.cart:
            if self.cart[name][1] > 1:
                self.cart[name][1] -= 1
            else:
                del self.cart[name]

    def total(self):
        return sum([price * quantity
                    for price, quantity in self.cart.values()])


class OnlineShoppingCart(ShoppingCart):
    def total(self):
        return 10 + (1.05 * super().total())


sc = ShoppingCart()
sc.add('book', 30, 1)
sc.add('toothbrush', 3, 4)

print(sc.total())

osc = OnlineShoppingCart()
osc.add('book', 30, 1)
osc.add('toothbrush', 3, 4)

print(osc.total())


# (3)
class Scoop:
    def __init__(self, flavour):
        self.flavour = flavour


class Bowl:
    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        self.scoops += new_scoops[:self.max_scoops - len(self.scoops)]

    def flavours(self):
        return [scoop.flavour
                for scoop in self.scoops]


class BigBowl(Bowl):
    max_scoops = 5


s1, s2, s3 = Scoop('Chocolate'), Scoop('Vanilla'), Scoop('Coffee')

b = Bowl()
b.add_scoops(s1, s2, s3)
print(f'Number of scoops in the bowl: {len(b.scoops)}')


b_1 = BigBowl()
b_1.add_scoops(s1, s2, s3, s1, s2)
print(f'Number of scoops in the bowl: {len(b_1.scoops)}')
