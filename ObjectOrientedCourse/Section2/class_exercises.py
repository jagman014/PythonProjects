# Exercises

# (1)
class Scoop:
    def __init__(self, flavour):
        self.flavour = flavour


ice_creams = [Scoop('chocolate'), Scoop('vanilla'), Scoop('caramel')]

for ice_cream in ice_creams:
    print(ice_cream.flavour)


# (2)
class Person:
    def __init__(self, name, email, number):
        self.name = name
        self.email = email
        self.number = number


alice = Person('alice', 'alice@alice.com', '+441238569124')
bob = Person('bob', 'bob@bob.com', '+441345682975')
charles = Person('charles', 'charles@charles.com', '+443546829753')

for person in [alice, bob, charles]:
    print(f'Name: {person.name:.<10}E-mail: {person.email:.<25}'
          f'Phone Number: {person.number}')

charles.email = 'test@test.com'

for person in [alice, bob, charles]:
    print(f'Name: {person.name:.<10}E-mail: {person.email:.<25}'
          f'Phone Number: {person.number}')


# (3)
class BankAccount:
    def __init__(self):
        self.transactions = []

    def transact(self, *args):
        for arg in args:
            self.transactions.append(arg)


account_1 = BankAccount()
account_2 = BankAccount()

account_1.transact(1.00, -1.25, 55.30, 65.1, -100.50)
account_2.transact(99.21, -555.22, 785.3, -1234.99, 2.00)

accounts = [account_1, account_2]

for account in accounts:
    num_transactions = len(account.transactions)
    balance = sum(account.transactions)
    ave_transactions = balance / num_transactions

    print(f'You have made {num_transactions} transactions to your account.')
    print(f'With an average of {ave_transactions:.2f} per transaction, and a'
          f' current balance of {balance:.2f}')
