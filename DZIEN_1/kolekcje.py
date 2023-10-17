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

