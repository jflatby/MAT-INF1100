def distance(t, v): #Igjen, t og v er lister
    s = [0]

    for i in range(1, len(t)):
        deltaT = t[i] - t[i-1]
        s.append((deltaT * v[i]) + s[i-1])
        """
        Legger til den forrige avstanden(s[i-1]) hver gang slik at hver verdi
        i listen gir avstanden fra startpunktet, som er det oppgaven ber om.
        """
        
    return s


