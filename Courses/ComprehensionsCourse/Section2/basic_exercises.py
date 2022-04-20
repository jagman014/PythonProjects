# Exercises

# (1)
my_list = [10, 20, 30]
string = '*'.join([str(item)
                   for item in my_list])

print(string)

# (2)
hex_numbers = input('Enter hex numbers separated by spaces: ').split()
hex_sum = sum([int(num, 16)
               for num in hex_numbers])

print(f'Here is the decimal sum: {hex_sum}')

# (3)
sentence = input('Enter a sentence: ').split()
word_sum = sum([len(word)
                for word in sentence])

print(f'Here is a sum of the number of characters: {word_sum}')
