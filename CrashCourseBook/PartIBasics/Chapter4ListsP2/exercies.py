# 4.3
for i in range(1, 21):
    print(i)

# 4.4
million = list(range(1, 1000001))
for i in million:
    print(i)

# 4.5
print(min(million))
print(max(million))
print(sum(million))

# 4.6
odd_numbers = list(range(1, 21, 2))
for i in odd_numbers:
    print(i)

# 4.7
threes = list(range(3, 31, 3))
for i in threes:
    print(i)

# 4.8
cubes = []
for i in range(1, 11):
    i = i ** 3
    cubes.append(i)
print(cubes)

# 4.9
cubes1 = [i ** 3 for i in range(1, 11)]
print(cubes1)
