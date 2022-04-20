# Example code from Chapter 7

# Data Structures
# 1. Dictionaries
# 2. Lists / arrays
# 3. Sets

# Lists: full list
lst = [1, 1, 11, 7]
print(lst)
lst.append(2)
print(lst)
lst.remove(11)
print(lst)
lst.sort()
print(lst)

# Sets: Distinct items
st = {1, 1, 11, 7}
st.add(1)
print(st)

# Dictionaries: list of named variables
d = {
    'bob': 0,
    'sarah': 0,
    'defeated_by': {'paper', 'wolf'},
    'defeats': {'scissors', 'sponge'},
}

print(d['bob'])
d['bob'] += 1
print(d['bob'])
print(d)
d['michael'] = 7
print(d)
print(f"You are defeated by {d['defeated_by']}")
print(d.get('other', 42))  # obtains key if it is in the dictionary, otherwise the second input is returned
