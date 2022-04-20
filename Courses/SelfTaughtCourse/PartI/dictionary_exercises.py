me = {
    'height': '178 cm',
    'weight': '63 kg',
    'eye colour': 'brown',
    'hair colour': 'brown',
    'nationality': 'British',
    'favourite colour': 'midnight purple'
}

value = input('What do you want to know about me? ')

if value in me:
    print(me[value])
else:
    print('Not found')

