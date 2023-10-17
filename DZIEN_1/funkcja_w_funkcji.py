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


#przykład 2

def rejestracja(oplata):
    def lista_zawodnikow():
        return "jesteś na liście zawodników! Opłata wniesiona"

    def brak():
        return "brak wpłaty, uzupełnij w ciągu 3 dni!"

    def error():
        return "błąd w kodzie opłaty. Ponów!"

    if oplata == 1:
        return lista_zawodnikow
    elif oplata == 0:
        return brak
    else:
        return error


print(rejestracja(1)())
print(rejestracja(45)())
print(rejestracja(0)())

# przykład 3  list comprehension
biglista = [2*i+1 for i in range(100_000) if i%2!=0]
# print(biglista)

#przykład4
def startstop(funkcja):
    def wrapper(*args):
        print("_" * 40)
        print("uruchomienie procesu....")
        funkcja(*args)
        print("zakończenie procesu!")
    return wrapper

