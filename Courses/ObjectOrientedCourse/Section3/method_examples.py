# Example

class Book:
    # can set default values if none provided,
    # useful when editing code after assignments
    def __init__(self, title, author, price=30):
        self.title = title
        self.author = author
        self.price = price

    def nice_author_name(self):
        return ', '.join(reversed(self.author.split()))

    def vat_price(self):
        return round(self.price * 1.2, 2)


# "has-a" relationship -- composition
# Bookshelf "has-a" book

class Bookshelf:
    def __init__(self):
        self.books = []

    def add_books(self, *args):
        self.books += args

    def total_price(self):
        return sum([book.price
                   for book in self.books])


b_1 = Book('Title1', 'John Smith')
b_2 = Book('Title2', 'David Cohen')
b_3 = Book('Title3', 'David Cohen', 25)

print(b_1.price)
print(b_3.price)

print(b_1.author)
print(b_1.nice_author_name())

print(b_2.vat_price())
print(b_3.vat_price())

shelf = Bookshelf()
shelf.add_books(b_1, b_2, b_3)

print(shelf.books)
print(shelf.books[0].title)

print(shelf.total_price())
