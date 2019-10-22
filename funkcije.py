def pozdrav(ime, priimek): #glava funkcije   #ime je argument funkcije, podobno kot spremenljivka
    print("Pozdravljen, " + ime + " " + priimek)   #telo funkcije


pozdrav("Miha", "Frece")    #kot print
pozdrav("Mojca", "Cimerman")
pozdrav("Janko", "Novak")


def obseg_kroga(polmer):
    pi = 3.1415926535
    obseg = 2 * pi * polmer
    return obseg

obseg5 = obseg_kroga(5)
print("Obseg kroga s polmerom je " + str(obseg5))

