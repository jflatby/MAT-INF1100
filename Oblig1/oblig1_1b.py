from math import sqrt

x = [1, 1-sqrt(2)]
for n in range(0, 99):
    x.append(2 * x[n+1] + x[n])
print x
