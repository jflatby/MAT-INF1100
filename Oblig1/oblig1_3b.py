from random import random
antfeil = 0; N = 10000
x0 = y0 = z0 = 0.0
feil1 = feil2 = 0.0

for i in range(N):
    x = random(); y = random();
    res1 = (x+y)*(x-y)
    res2 = x**2-y**2
    
    if res1 != res2:
        antfeil += 1
        x0 = x; y0 = y
        feil1 = res1
        feil2 = res2
        
print (100. * antfeil/N)
print (x0, y0, feil1 - feil2)
