# Exercise
import os

current_directory = os.path.dirname(__file__)
file = os.path.relpath('..\exercise-files\shoe-data.txt',
                       current_directory)


def shoe_dict(line):
    brand, colour, size = line.strip().split('\t')
    return {'brand': brand,
            'colour': colour,
            'size': size}


inventory = [shoe_dict(line)
             for line in open(file)]

for shoe in inventory:
    print(f"{shoe['colour'].title(): <7}{shoe['brand']:.<15}size: {shoe['size']}")
