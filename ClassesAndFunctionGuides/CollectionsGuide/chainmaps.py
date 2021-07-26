from collections import ChainMap

# maps multiple dicts into one view
# search for key, depends on order entered into chainmap

cmd_proxy = {}  # the user doesn't provide a proxy
local_proxy = {"proxy": "proxy.local.com"}
global_proxy = {"proxy": "proxy.global.com"}

config = ChainMap(cmd_proxy, local_proxy, global_proxy)

print(config)
print(config["proxy"])

# maps holds the internal listing of the mapping

numbers = {"one": 1, "two": 2}
letters = {"a": "A", "b": "B"}

alpha_nums = ChainMap(numbers, letters)
print(alpha_nums.maps)

# can update this list of the mapping

dad = {"name": "John", "age": 35}
mum = {"name": "Jane", "age": 31}

family = ChainMap(mum, dad)
print(family)

# new_child appends new map to front of the mapping list

son = {"name": "Mike", "age": 0}
family = family.new_child(son)

for person in family.maps:
    print(person)

# all maps apart from the first one

print(family.parents)

# all dict methods act on the first mapping only

alpha_nums = ChainMap(numbers, letters)
print(alpha_nums)

alpha_nums["c"] = "C"
print(alpha_nums)

print(alpha_nums.pop("two"))
print(alpha_nums)

# del alpha_nums["a"] -> error no key "a" in the first map

alpha_nums.clear()
print(alpha_nums)

# need to mutate mappings within .maps to edit other mappings
