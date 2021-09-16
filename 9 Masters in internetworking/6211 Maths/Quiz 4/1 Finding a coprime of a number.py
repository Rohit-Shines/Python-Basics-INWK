

from math import gcd
# find coprimes of c within range the range 0 to c.
def find_coprimes(c):
    coprimes = []
    for x in range(c):
        y = gcd(x, c)
        if y == 1:
            coprimes.append(x)
    return coprimes
print(find_coprimes(5))