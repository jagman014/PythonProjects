lst = [1, 2, 5, 8]

while True:
    x = input("Guess a number between 1 - 10 (Type q to quit): ")
    if x == 'q':
        break
    if int(x) in lst:
        print('You guessed correctly')
    else:
        print('You guessed wrong')

num = [8, 19, 148, 4]
num_2 = [9, 1, 33, 83]
multi = []

for i in num:
    for j in num_2:
        multi.append(i * j)

print(multi)
