from collections import defaultdict, Counter

# using a dict as a counter

word = "mississippi"
counter = {}

for letter in word:
    if letter not in counter:
        counter[letter] = 0

    counter[letter] += 1

print(f"dict: {counter}")

# can be done with defaultdict

counter = defaultdict(int)

for letter in word:
    counter[letter] += 1

print(f"defaultdict: {counter}")

# using counter

print(f"counter: {Counter(word)}")

# counter can count any hashable iterable type

print(Counter([1, 1, 2, 3, 3, 3, 4]))

# similar methods to dict
# update does += instead of =

letters = Counter(word)
print(letters)

letters.update(m=3, i=4)
print(letters)

# can add new key count pair
letters.update({"a": 2})
print(letters)

# can update with another counter
letters.update(Counter(["s", "s", "p"]))
print(letters)

# default values of zero
letters = Counter(word)
print(letters["a"])

# inventory example, using update, subtract, and + / -

inventory = Counter(dogs=23, cats=14, pythons=7)
print(inventory)

adopted = Counter(dogs=2, cats=5, pythons=6)
inventory.subtract(adopted)

print(inventory)

new_pets = {"dogs": 4, "cats": 1}
inventory.update(new_pets)

print(inventory)

inventory -= Counter(dogs=2, cats=3, pythons=1)

print(inventory)

new_pets = {"dogs": 4, "pythons": 2}
inventory += new_pets

print(inventory)
