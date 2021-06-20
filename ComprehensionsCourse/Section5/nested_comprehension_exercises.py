# Exercises
import os

# (1)
places = {'Israel': ['Jerusalem', 'Tel Aviv'],
          'USA': ['Boston', 'New York', 'Chicago'],
          'China': ['Beijing', 'Shanghai']}

locations = [(value, key)
             for key in places
             for value in places[key]]

print(locations)


# (2)
def sum_to_n(n):
    return [(x, y)
            for x in range(n + 1)
            for y in range(n + 1)
            if x + y == n]


print(sum_to_n(5))

# (3)
current_directory = os.path.dirname(__file__)
file = os.path.relpath('..\exercise-files\mini-access-log.txt',
                       current_directory)

unique_octets = {octet
                 for ip in open(file)
                 for octet in ip.split()[0].split('.')}

print(unique_octets)
