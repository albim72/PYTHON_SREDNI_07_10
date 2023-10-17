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
