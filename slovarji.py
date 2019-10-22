seznam = ["Ljubljana", "Zagreb", "Dunaj"]

slovar = {"kljuc1": "vrednost", "kljuc2":"vrednost2"}

#Izpis slovarja
print(slovar)

#Izpis elementa z nekim ključem
print(slovar["kljuc2"])
#python ne podpira št ki se začnejo z 0
#števila pustimo števila, razen če je osebna številka npr emšo,tel

uporabnik1 = {
    "ime": "Miha",
    "priimek": "Novak",
    "letnica_rojstva": 1979
}

uporabnik2 = {
    "ime": "Mojca",
    "priimek": "Kovač",
    "letnica_rojstva": 1989
}

uporabnik1["priimek"] = "Kovač"

print(uporabnik1["priimek"])
print(uporabnik2["priimek"])

uporabniki = [uporabnik1, uporabnik2]

for i in range(2):
    novo_ime = input("Vpiši ime: ")
    nov_priimek = input ("Vpiši priimek: ")
    nova_letnica_rojstva = int(input("Vpiši letnico rojstva: "))

    nov_uporabnik = {
        "ime": novo_ime,
        "priimek": nov_priimek,
        "letnica_rojstva": nova_letnica_rojstva
    }

    uporabniki.append(nov_uporabnik)

for uporabnik in uporabniki:     #namesto uporabnik bi lahko uporabili tudi karkoli x, i...
    print("Izpis uporabnika:")
    print("\tIme je " + uporabnik["ime"] + " " + uporabnik["priimek"])
    print("\tLetnica rojstva: " + str(uporabnik["letnica_rojstva"]))



