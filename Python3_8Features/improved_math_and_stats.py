import math
import statistics

# product function
print(math.prod((2, 8, 7, 7)))

# integer sqrt, floors to integer
print(math.isqrt(15))
print(math.sqrt(15))

# euclidean distance between points
point_1 = (16, 25, 20)
point_2 = (8, 15, 14)

print(math.dist(point_1, point_2))

# euclidean norm, hypotenuse
print(math.hypot(*point_1))

# mean as a float
# converts data to floats before computation
data = [9, 3, 2, 1, 1, 2, 7, 9]
print(statistics.fmean(data))

# geometric mean
print(statistics.geometric_mean(data))

# multimode, for data with multiple modes
print(statistics.multimode(data))

# quantiles
print(statistics.quantiles(data, n=4))
