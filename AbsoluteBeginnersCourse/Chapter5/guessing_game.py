# Initial coding game setup during chapter 5
import random

print('----------------------------')
print('     M&M Guessing Game')
print('----------------------------')
print("Guess the number of M&Ms and you get a free lunch!\n")

mm_count = random.randint(1, 100)
attempt_limit = 5
attempts = 0

while attempts < attempt_limit:
    guess = int(input('How many M&Ms are in the jar? '))
    attempts += 1

    if mm_count == guess:
        print(f'You won the free lunch!! It was {guess}.')
        break
    elif mm_count < guess:
        print("Sorry that's too HIGH!")
    else:
        print("Sorry that's too LOW!")

print(f"Bye, you're done in {attempts} tries!")
