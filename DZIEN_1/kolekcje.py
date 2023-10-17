print("kolekcje języka Python")

a = 55
print(a)
print(type(a))

a = "zielone"
print(a)
print(type(a))

b:float = "abc"
print(b)
print(type(b))

b = True
print(b)
print(type(b))

#komentarz standardowy
"""
komentarz dokumentacyjny /pierwszy komentarz w danej strukturze/ -  wielolinowy
abc
"""
'''
komentarz wielolinowy
xyz
'''

imiona = ["Jan","Monika","Leon","Olaf","Halina","Jan","Nadia","Leon"]
print(imiona)

# CTRL + D  duplikacja linii - bloku
print(imiona[0])
print(imiona[1])
print(imiona[2:5])
print(imiona[-1])

parzyste = imiona[::2]
print(parzyste)

im = imiona[2]
print(im)
print(im[::-1])

import copy

team = imiona
t1 = list(imiona)
t2 = imiona[:]
t3 = copy.deepcopy(imiona)

print(type(team))
print(f'lista imion: {imiona}')
print(f'lista team: {team}')

imiona[2:4] = ["Feliks","Paweł","Roma","Daria"]

print(f'lista imion po zmianie: {imiona}')
print(f'lista team po zmianie: {team}')
print(f'lista t1 po zmianie: {t1}')
print(f'lista t2 po zmianie: {t2}')
print(f'lista t3 po zmianie: {t3}')

#krotka -> lista niemutowalna
miasta = ("Kraków","Tarnów","Gdańsk","Wrocław","Kraków","Warszawa",434)

print(miasta)
print(miasta.count("Kraków"))
print(miasta.count(434))
print(len(miasta))
print(miasta[0:3])

#zbiór -> set

kolory = {"zielony","czerwony","niebieski","biały","czarny","brązowy","biały"}
print(kolory)
print(kolory)
print(kolory)

setcity = set(miasta)
miasta = tuple(setcity)
print(miasta)

kolory.remove("brązowy")
print(kolory)

kolory.discard("biały")
print(kolory)

#słownik -> dict
osoba = {
    "imię":"Jan",
    "nazwisko":"Kowal",
    "wiek":56,
    "miasto":"Rzeszów",
    "miasto urodzenia":"Rzeszów",
    "nazwisko":"Kobus"
}

print(osoba)
print(type(osoba))
print(osoba["imię"])
osoba["miasto"] = "Sanok"
print(osoba)
osoba["zawód"] = "Programista"
print(osoba)

print(osoba.keys())
print(osoba.values())
print(osoba.items())

print("_____________ Items ______________")
for x,y in osoba.items():
    print(f"{x} : {y}")
