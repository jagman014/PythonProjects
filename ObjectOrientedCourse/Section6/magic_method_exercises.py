# Exercises

# (1) & (2)
class Scoop:
    def __init__(self, flavour):
        self.flavour = flavour

    def __repr__(self):
        return f'Scoop of {self.flavour}'


class Bowl:
    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        self.scoops += new_scoops[:self.max_scoops - len(self.scoops)]

    def flavours(self):
        return [scoop.flavour
                for scoop in self.scoops]

    def __len__(self):
        return len(self.scoops)

    def __repr__(self):
        return 'Bowl with:\n' + '\n'.join(f'\t{i}) {scoop}'
                                          for i, scoop in
                                          enumerate(self.scoops, start=1))
        # generator expression works similar to list comprehension


class BigBowl(Bowl):
    max_scoops = 5


s1, s2, s3 = Scoop('Chocolate'), Scoop('Vanilla'), Scoop('Coffee')

b = Bowl()
b.add_scoops(s1, s2, s3)
print(f'Number of scoops in the bowl: {len(b)}')

b_1 = BigBowl()
b_1.add_scoops(s1, s2, s3, s1, s2)
print(f'Number of scoops in the bowl: {len(b_1)}')

print(s1)
print(b)
print(b_1)


# (3)
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

    def __len__(self):
        return sum(item[1]
                   for item in self.cart.values())

    def __repr__(self):
        return ('Items in cart:\n' +
                '\n'.join(f'\t{key.title(): <15}x{value[1]: <3} '
                          f'@ £{value[0]: <3}: £{value[0] * value[1]}'
                          for key, value in self.cart.items()) +
                f'\n-----------------------------------' +
                f'\nTotal price (£): {self.total():18}')


sc = ShoppingCart()
sc.add('book', 30, 1)
sc.add('toothbrush', 3, 4)

print(len(sc))
print(sc)
