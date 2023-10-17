#przykład 1

def witaj(imie):
    return f'dziękujemy za założenie konta: {imie}'

def egazmin(imie,punkty,zaliczono):
    return f'osoba egzaminowana: {imie}, liczba punktów: {punkty}, zaliczenie: {zaliczono}'

def wynik(punkty,bonus):
    if punkty>60:
        return punkty+bonus
    else:
        return punkty

def osoba(funkcja,*args):
    return funkcja(*args)


print(osoba(witaj,"Leon"))
print(osoba(egazmin,"Olga",67,True))
print(osoba(wynik,88,5))
print(osoba(wynik,40,5))
