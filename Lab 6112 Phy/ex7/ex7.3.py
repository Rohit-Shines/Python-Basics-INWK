import math
i=0
j=0
term=1
while term>1e-15:
    term= (math.factorial(4 * j) * (1103 + 26390 * j)) / ((math.factorial(j)) ** 4 * 396 ** (4 * j))
    i= i + term
    j= j + 1

c=9801/(2 * 2 ** .5 * i)
print('Value of pi :{:.15f}'.format(math.pi))
print('Calculated value of pi: {:.15f}'.format(c)