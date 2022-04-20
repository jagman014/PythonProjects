words = [7742, 11539, 16898, 13447, 4608, 6628, 2683, 6156, 2623, 6948]
views = [8368, 5901, 3978, 3329, 2611, 2096, 1515, 1177, 814, 467]

import statistics

print(statistics.covariance(words, views))

print(statistics.correlation(words, views))

print(statistics.linear_regression(words, views))

lr = statistics.linear_regression(words, views)

print(lr.slope)

print(10000 * lr.slope + lr.intercept)
