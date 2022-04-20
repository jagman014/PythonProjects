def main():
    square(float(input('Square a number? ')))
    print_print(str(input('What print? ')))
    half(float(input('Half what? ')))
    quadruple(float(input('What quadruple? ')))
    mith(float(input('1: ')), float(input('2: ')), float(input('3: ')), float(input('4: ')), float(input('5: ')))
    mith(float(input('1: ')), float(input('2: ')), float(input('3: ')), float(input('4: ')))
    mith(float(input('1: ')), float(input('2: ')), float(input('3: ')))


def square(number):
    squared_number = number ** 2
    print(f'{squared_number}\n')


def print_print(string):
    print(string + '\n')


def half(number):
    halved_number = number / 2
    print(f'{halved_number}\n')


def quadruple(number):
    quad_number = number * 4
    print(f'{quad_number}\n')


def mith(x, y, z, u=None, v=None):
    if u and v:
        print(f'{x * y * z * u * v}\n')
    elif u:
        print(f'{x + y + z + u}\n')
    else:
        print(f'{x - y - z}\n')


if __name__ == '__main__':
    main()
