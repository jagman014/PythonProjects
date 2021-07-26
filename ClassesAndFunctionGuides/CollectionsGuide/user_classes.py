from collections import UserDict  # UserList, UserString

# cant modify built-in classes, can only extend them


class LowerDict(dict):
    def __setitem__(self, key, value):
        key = key.lower()
        super().__setitem__(key, value)


ordinals = LowerDict({"FIRST": 1, "SECOND": 2})
ordinals["THIRD"] = 3
ordinals.update({"FOURTH": 4})

# doesn't work as intended due to other underlying methods

print(ordinals)
print(isinstance(ordinals, dict))

# easier implementation with UserDict
# information stored in .data method


class LowerDict(UserDict):
    def __setitem__(self, key, value):
        key = key.lower()
        super().__setitem__(key, value)


ordinals = LowerDict({"FIRST": 1, "SECOND": 2})
ordinals["THIRD"] = 3
ordinals.update({"FOURTH": 4})

print(ordinals)
print(isinstance(ordinals, dict))
