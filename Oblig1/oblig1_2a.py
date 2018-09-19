
def binomialkoeffisient(n, i):
    produkt = 1
    for j in xrange(1, n-i+1):
        produkt *= (float(i)+j)/j

    return produkt

print binomialkoeffisient(9998, 4)
print binomialkoeffisient(100000, 70)
print binomialkoeffisient(1000, 50000)
#4.16083629103e+14
#8.14900007814e+249
#2.70288240945e+299
