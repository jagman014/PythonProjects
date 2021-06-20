# Example
computers = [{'brand': 'Apple', 'year': 2014},
             {'brand': 'HP', 'year': 2016},
             {'brand': 'Lenovo', 'year': 2016},
             {'brand': 'Apple', 'year': 2010}]

for computer in computers:
    print(f'{computer["brand"]}, from {computer["year"]}')
print()


# better implementation
class Computer:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year


c1 = Computer('Apple', 2014)
c2 = Computer('HP', 2016)
c3 = Computer('Lenovo', 2016)
c4 = Computer('Apple', 2010)

my_computers = [c1, c2, c3, c4]

for computer in my_computers:
    print(f'{computer.brand}, from {computer.year}')


# Example 2
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


all_books = []

while True:
    title = input('Enter title or <return> to stop: ').strip()
    if not title:
        break

    author = input('Enter author: ').strip()
    price = float(input('Enter price: '))

    all_books.append(Book(title, author, price))

print(all_books)
