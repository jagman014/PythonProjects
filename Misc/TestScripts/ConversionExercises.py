# %% Problem 1
import numpy as np
import matplotlib.pyplot as plt

N = int(input('How many numbers? (+ve Integer) '))
a = []

for i in range(0, N):
    a.append(int(input('Enter number %d: ' % (i + 1))))

Sum = np.sum(a)
Mean = np.average(a)
Med = np.median(a)

print('The total sum is:', Sum, '\nThe mean is:', Mean,
      '\nThe Median is:', Med)
# %% Problem 2

R = np.random.randint(1, 13, 1200)
x, y = np.unique(R, return_counts=True)
Count = dict(zip(x, y))

plt.figure(1)

n, bins, patches = plt.hist(R, len(x), density=1)
plt.show()
# %% Problem 3

P = []
x = [0]

P0 = ((-1) ** 0) / ((2 * 0) + 1)
P.append(P0)
diff = abs(np.pi - (4 * P[0]))
i = 1

while diff >= 0.01:
    Pi = ((-1) ** i) / ((2 * i) + 1)
    P.append(Pi + P[i - 1])
    x.append(i)
    diff = abs(np.pi - (4 * P[i]))
    i += 1

P = 4 * np.asarray(P)

plt.figure(2)
plt.plot(x, P)
plt.xlabel('Iterations')
plt.ylabel('Value of $\pi$')
plt.show()
# %% Problem 4
