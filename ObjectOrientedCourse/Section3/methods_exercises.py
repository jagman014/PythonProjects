# Exercises

# (1)
class Scoop:
    def __init__(self, flavour):
        self.flavour = flavour


class Bowl:
    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        self.scoops += new_scoops

    def flavours(self):
        return [scoop.flavour
                for scoop in self.scoops]


s1, s2, s3 = Scoop('Chocolate'), Scoop('Vanilla'), Scoop('Coffee')

b = Bowl()
b.add_scoops(s1, s2, s3)
print(b.flavours())


# (2)
class Person:
    def __init__(self, name, email, number):
        self.name = name
        self.email = email
        self.number = number
        self.accounts = []

    def add_account(self, *new_accounts):
        self.accounts += new_accounts

    def all_balances(self):
        return [account.balance()
                for account in self.accounts]

    def current_total_balance(self):
        return round(sum(self.all_balances()), 2)

    def average_transaction_amount(self):
        averages = [account.average_transaction()
                    for account in self.accounts]
        return round(sum(averages) / len(averages), 2)


class BankAccount:
    def __init__(self):
        self.transactions = []

    def transact(self, *new_transaction):
        self.transactions += new_transaction

    def balance(self):
        return round(sum(self.transactions), 2)

    def average_transaction(self):
        return round(self.balance() / len(self.transactions), 2)


account_1 = BankAccount()
account_2 = BankAccount()

account_1.transact(1.00, -1.25, 55.32, 65.11, -100.50)
account_2.transact(99.21, -555.22, 785.31, -1234.99, 2.00)

alice = Person('alice', 'alice@alice.com', '+441238569124')
alice.add_account(account_1, account_2)

print(alice.all_balances())
print(alice.current_total_balance())
print(alice.average_transaction_amount())


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


sc = ShoppingCart()
sc.add('book', 30, 1)
sc.add('toothbrush', 3, 4)

print(sc.cart)
print(sc.total())

sc.remove('toothbrush')
print(sc.cart)

sc.add('toothbrush', 3, 1)
print(sc.cart)

sc.remove('book')
print(sc.cart)
