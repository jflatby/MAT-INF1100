def acceleration(t, v): #Der t og v er lister
    a = [0]

    for i in range(1, len(t)):
        deltaT = t[i] - t[i-1]
        deltaV = v[i] - v[i-1]
        a.append(deltaV/deltaT)

    return a
