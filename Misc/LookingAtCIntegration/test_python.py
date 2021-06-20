import time

start = time.time()

for i in range(100):
    if i % 2 == 0:
        print(i)

end = time.time()

print('\n', end - start)
# 0.035117149353027344 s
