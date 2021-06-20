# Exercises

# (1)
class Scoop:
    def __init__(self, flavour):
        self.flavour = flavour


class Bowl:
    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        self.scoops += new_scoops[:Bowl.max_scoops - len(self.scoops)]

    def flavours(self):
        return [scoop.flavour
                for scoop in self.scoops]


s1, s2, s3 = Scoop('Chocolate'), Scoop('Vanilla'), Scoop('Coffee')

b = Bowl()
b.add_scoops(s1, s2, s3)
print(f'Number of scoops in the bowl: {len(b.scoops)}')

b.add_scoops(s1)
print(f'Number of scoops in the bowl: {len(b.scoops)}')


# (2)
class Loan:
    available_assets = 1000

    def __init__(self, loan_amount):
        if Loan.available_assets >= loan_amount:
            self.loan_amount = loan_amount
            Loan.available_assets -= loan_amount
        else:
            raise ValueError('No enough available assets to loan.')

    def repay(self, pay_amount):
        if pay_amount <= self.loan_amount:
            self.loan_amount -= pay_amount
            Loan.available_assets += pay_amount
        else:
            raise ValueError('That is more than you owe.')


l_1 = Loan(500)
print(f'Available assets: {Loan.available_assets}')

l_2 = Loan(200)
print(f'Available assets: {Loan.available_assets}')

l_1.repay(500)
print(f'Available assets: {Loan.available_assets}')

l_3 = Loan(400)
print(f'Available assets: {Loan.available_assets}')
