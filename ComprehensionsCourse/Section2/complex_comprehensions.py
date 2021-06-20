# Examples
d = {'a': 1, 'b': 2, 'c': 3}

keys = [item
        for item in d]
print(keys)  # can do d.keys, but doesn't return a list

values = [d[item]
          for item in d]
print(values)

tuple_of_d = [(item, d[item])
              for item in d]
print(tuple_of_d)

extra_bit = [key * d[key]
             for key in d]
print(extra_bit)

# better version of above
tuple_of_d_1 = [item
                for item in d.items()]
print(tuple_of_d_1)

extra_bit_1 = [key * value
               for key, value in d.items()]
print(extra_bit_1)


def reverse_word(word):
    return word[::-1]


words = input('Enter some words: ').split()

rev_words = ' '.join([reverse_word(word)
                      for word in words])
print(rev_words)

# can also open(file), but better to use with statements
# can add a conditional after iteration
