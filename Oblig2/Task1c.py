import matplotlib.pyplot as plt
from Task1a import acceleration
from Task1b import distance

t = []
v = []
infile = open("running.txt","r")
for line in infile:
    tnext, vnext = line.strip().split(",")
    t.append(float(tnext))
    v.append(float(vnext))
infile.close()

#Plotter Akselerasjon:
a = acceleration(t, v)
plt.plot(t, a)
plt.xlabel("t")
plt.ylabel("a")
plt.legend(["Acceleration"])
plt.savefig("a.pdf")
plt.show()


#Plotter Avstand:
s = distance(t, v)
plt.plot(t, s)
plt.xlabel("t")
plt.ylabel("s")
plt.legend(["Distance"])
plt.savefig("s.pdf")
plt.show()

