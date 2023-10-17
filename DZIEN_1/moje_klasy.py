import datetime

class Osoba:
    def __init__(self,imie,rok_ur,waga,wzrost):
        self.imie = imie
        self.wiek = datetime.date.today().year - rok_ur
        self.waga = waga
        self.wzrost = wzrost

    def __repr__(self):
        return (f'osoba -> {self.imie}, wiek: {self.wiek} lat, waga: {self.waga} kg, '
                f'wzrost: {self.wzrost} cm')

    def czypracownik(self):
        return False



os1 = Osoba("Nadia",1978,52,171)
print(os1)

print(f'czy osoba jest pracownikiem? ({os1.czypracownik()})')


print("_"*40)

class Firma:
    def __init__(self,nazwa,branza,miasto):
        self.nazwa = nazwa
        self.branza = branza
        self.miasto = miasto

    def show_firma(self):
        print(f'firma {self.nazwa}, branża: {self.branza}, miasto: {self.miasto}')


class Pracownik(Osoba,Firma):
    def __init__(self, imie, rok_ur, waga, wzrost,nazwa,branza,miasto,
                 stanowisko,wynagrodzenie):
        Osoba.__init__(self,imie, rok_ur, waga, wzrost)
        Firma.__init__(self,nazwa,branza,miasto)
        self.stanowisko = stanowisko
        self.wynagrodzenie = wynagrodzenie

    def print_pracwnik(self):
        print(f'bane pracownika: {self.stanowisko}, wynagrodzenie: {self.wynagrodzenie} zł')

    def czypracownik(self):
        return True

pr1 = Pracownik("Olga",32,56,167,"ABC","IT",
                "Kraków","Dyrektor",11200)
print(pr1)
pr1.print_pracwnik()

print(f'czy osoba jest pracownikiem? ({pr1.czypracownik()})')
