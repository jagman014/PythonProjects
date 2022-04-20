from collections import OrderedDict

# dicts in 3.6+ are ordered
# however, OrderedDict allows for more control over the order
# equality tests also check ordering between objects

life_stages = OrderedDict()

life_stages["childhood"] = "0-9"
life_stages["adolescence"] = "9-18"
life_stages["adulthood"] = "18-65"
life_stages["old"] = "+65"

for stage, years in life_stages.items():
    print(stage, "->", years)

letters = OrderedDict(b=2, d=4, a=1, c=3)
print(letters)

# move b to the right end

letters.move_to_end("b")
print(letters)

# move b to left end

letters.move_to_end("b", last=False)
print(letters)

# sort by key

for key in sorted(letters):
    letters.move_to_end(key)

print(letters)

# dicts only compare content, ordereddicts also compare order

letters_0 = dict(a=1, b=2, c=3, d=4)
letters_1 = dict(b=2, a=1, d=4, c=3)

print(letters_0 == letters_1)

letters_0 = OrderedDict(a=1, b=2, c=3, d=4)
letters_1 = OrderedDict(b=2, a=1, d=4, c=3)

print(letters_0 == letters_1)
