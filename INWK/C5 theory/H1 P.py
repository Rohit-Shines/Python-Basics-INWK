import math as m  # math library
import numpy as np  # numpy library
import matplotlib.pyplot as plt  # for graphical representations
import random as r  # for random values in a range

# arrays and dictionary to store values for future use
Y = []
X = []
a = {}


# user define functions to implement formula
def numerator(mu, y):
    N = float(m.log((1 + (mu * abs(y)))))
    return N


def denominator(mu):
    D = m.log(1 + mu)
    return D


def calculate(mu, x):
    y = float(((numerator(mu, x) / denominator(mu)) * np.sign(x)))
    return y


# another 2-d array to store and sort the key value pairs
pl = []
ch = input("If you are a receiver press A, otherwise B for sender: ")
if ch == 'A':
    mu = 0.1
    for x in range(1000):
        x = r.uniform(0, 1)
        X.append(x)
        X.sort()
        op = calculate(mu, x)
        pl.append([x, op])
        Y.append(op)
    pl.sort()
    X = []
    Y = []
    for i in pl:
        X.append(i[0])
        Y.append(i[1])

elif ch == 'B':
    mu = float(input("enter the value of mu: "))
    for x in range(1000):
        x = r.uniform(0, 1)  # this will generate random values
        X.append(x)  # this will add elements to the array X
        X.sort()  # sorting of values
        op = calculate(mu, x)
        pl.append([x, op])  # stores key value pair
        Y.append(op)
    pl.sort()  # sorts the values with respect to the value of x

    X = []
    Y = []
    for i in pl:
        X.append(i[0])
        Y.append(i[1])

print(pl)
plt.clf()
# plot 1
plt.xlabel('x')
plt.ylabel('y(x)')
plt.subplot(2, 1, 1)
plt.plot(X, Y)
plt.show()
# plot 2
plt.subplot(2, 1, 2)
plt.stem(X, Y)
plt.show()
