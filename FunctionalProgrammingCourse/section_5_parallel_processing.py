import collections
import multiprocessing
import os
from pprint import pprint
import time

Scientist = collections.namedtuple('Scientist', ['name', 'field', 'born', 'nobel'])
NameAndAge = collections.namedtuple('NameAndAge', ['name', 'age'])

ada_l = Scientist(name='Ada Lovelace', field='maths', born=1815, nobel=False)
emmy = Scientist(name='Emmy Noether', field='maths', born=1882, nobel=False)
marie = Scientist(name='Marie Curie', field='physics', born=1867, nobel=True)
tu = Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True)
ada_y = Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True)
vera = Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False)
sally = Scientist(name='Sally Ride', field='physics', born=1951, nobel=False)

scientists = (ada_l, emmy, marie, tu, ada_y, vera, sally)


def transform(x):
    print(f'Process {os.getpid()} working record {x.name}')
    time.sleep(1)
    result = tuple(NameAndAge(name=x.name, age=(2020 - x.born)))
    print(f'Process {os.getpid()} done processing record {x.name}')
    return result


def main():
    pprint(scientists)
    print()

    start = time.time()

    pool = multiprocessing.Pool()
    result = pool.map(transform, scientists)

    end = time.time()

    print(f'\nTime to complete: {end - start:.2f} s')
    pprint(result)


if __name__ == '__main__':
    main()
