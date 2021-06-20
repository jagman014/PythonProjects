# new inclusion of LCM and multiple GCD
from math import gcd, lcm
from functools import reduce

print(gcd(49, 14))
print(lcm(49, 14))

# multiple GCD before 3.9
print(reduce(gcd, [273, 1729, 6048]))

# now in 3.9
print(gcd(273, 1729, 6048))
