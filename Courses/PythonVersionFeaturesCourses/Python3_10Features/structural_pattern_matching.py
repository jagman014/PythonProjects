# Match case statements
# case statements cannot fall through like in c++

# simple literal matching
def greet(name):
    match name:
        case "Guido":
            print("I'm not worthy")
        
        case _:
            # _ is a wildcard, like default in c++
            print(f"Hello {name}")

greet('Jag')
greet('Guido')

# more complex example
from dataclasses import dataclass


@dataclass
class Card:
    rank: str
    suit: str


def is_red(card):
    match card:
        # guard statement
        case Card(suit=suit) if suit in "♢♡":
            return True

        case Card():
            return False

        case _:
            raise ValueError(f"{card} is not a Card object")


print(is_red(Card("2", "♡")))
print(is_red(Card("K", "♧")))
# print(is_red("card"))


# recursive example
def sum_list(numbers):
    match numbers:
        case []:
            return 0
        
        # type matching within match / case
        case [int(first) | float(first), *rest]:
            return first + sum_list(rest)

        case _:
            raise ValueError("Can only sum lists of numbers")


print(sum_list([1, 3, 9]))
print(sum_list([1, 3.14, 99]))
# print(sum_list(139))
# print(sum_list(['a', 'b']))


# rewriting fizzbuzz
def fizzbuzz_old(number):
    if (number % 3 == 0) and (number % 5 == 0):
        return "FizzBuzz"

    elif number % 5 == 0:
        return "Buzz"
    
    elif number % 3 == 0:
        return "Fizz"
    
    else:
        return str(number)


print(fizzbuzz_old(3))
print(fizzbuzz_old(14))
print(fizzbuzz_old(15))
print(fizzbuzz_old(65))


def fizzbuzz_new(number):
    match (number % 3, number % 5):
        case (0, 0):
            return "FizzBuzz"
        
        case (_, 0):
            return "Buzz"
        
        case (0, _):
            return "Fizz"
        
        case _:
            return str(number)


print(fizzbuzz_new(3))
print(fizzbuzz_new(14))
print(fizzbuzz_new(15))
print(fizzbuzz_new(65))


# sort function example
def psort(seq):
    match seq:
        # checks for empty list | single item in list
        case [] | [_]:
            return seq
        
        # checks if the first is less than the second
        case [x, y] if x <= y:
            return seq
        
        # only happens if the previous fails, if second is less than first
        case [x, y]:
            return [y, x]
        
        # already sorted case
        case [x, y, z] if x <= y <= z:
            return seq
        
        # reverse is checked
        case [x, y, z] if x >= y >= z:
            return [z, y, x]
        
        # first item extracted, then two lists
        # those less than or equal to first, and those greater than first
        # passed recursively to psort(), then combined and returned
        case [p, *rest]:
            a = psort([x for x in rest if x <= p])
            b = psort([x for x in rest if p < x])
            return a + [p] + b


from random import randint

a = [randint(0, 10) for _ in range(20)]
b = psort(a)

print(f"Before: {a}")
print(f"After: {b}")

# complex pattern matching allowed
# use of 'as' keyword possible
# dot notation treated as a literal instead of a capture
