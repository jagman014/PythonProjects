number = input("Give me an integer number: ")

try:
    print(int(number))
except ValueError:
    print("That's not an integer numeral.")
