def bottles_of_beer(bob):
    if bob < 1:
        print('No more bottles of beer on the wall. No more bottles of beer.')

        return

    tmp = bob
    bob -= 1

    print(f'{tmp} bottles of beer on the wall. {tmp} bottles of beer.\n'
          f'Take one down, pass it around, {bob} bottles of beer on the wall\n')

    bottles_of_beer(bob)


bottles_of_beer(99)
