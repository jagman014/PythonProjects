from collections import defaultdict

favourites = {
    "pet": "dog",
    "color": "blue",
    "language": "Python"
}

# can set default for missing values in dicts,
# similar thing can be done with get method

print(favourites)
print(favourites.setdefault("fruit", "apple"))
print(favourites.setdefault("pet", "cat"))

# can be easily handed by defaultdict
# missing keys auotmatically handled
# give type to defaultdict to infulence how missing vals are handled
# defaultdict subclasses dict, can be interacted as a dict

counter = defaultdict(int)
print(counter)

counter["dogs"]
print(counter)

counter["dogs"] += 1
counter["dogs"] += 1
counter["dogs"] += 1

counter["cats"] += 1
counter["cats"] += 1

print(counter)

# use defaultdict to group

pets = [
    ("dog", "Affenpinscher"),
    ("dog", "Terrier"),
    ("dog", "Boxer"),
    ("cat", "Abyssinian"),
    ("cat", "Birman")
]

group_pets = defaultdict(list)

for pet, breed in pets:
    group_pets[pet].append(breed)

for pet, breeds in group_pets.items():
    print(pet, "->", breeds)
