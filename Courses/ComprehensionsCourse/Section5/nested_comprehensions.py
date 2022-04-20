# Example

my_list = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

# one solution
listed = sum(my_list, [])
print(listed)

# nested comprehension method
listed_1 = [item
            for sublist in my_list
            for item in sublist]

print(listed_1)

# words similar to nested for loops
coordinates = [(x, y)
               for x in range(5)
               for y in range(5)]

print(coordinates)

# again you can add a conditional
even_x_odd_y_coords = [(x, y)
                       for x in range(5)
                       if not x % 2
                       for y in range(5)
                       if y % 2]

print(even_x_odd_y_coords)
