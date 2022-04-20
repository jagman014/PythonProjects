# Exercise from Chapter 5
print('----------------------------')
print('     Is It Even Or Odd?!')
print('----------------------------')

guess = 1

while guess != 0:
    guess = int(input('Input a non-zero integer number: '))
    val = guess % 2

    if val == 0 and guess != 0:
        print('Your number is EVEN!')
    elif val != 0:
        print('Your number is ODD!')
    else:
        print("That's Zero, Goodbye!")
        break
