import os

if os.path.exists("bmi.txt"):
    os.remove("bmi.txt")
    print("Plik z danymi archiwalnymi został usunięty!")
else:
    print("plik nie istnieje! Zostanie utworzony nowy!")

class Osoba:
    def __init__(self,imie,nazwisko,wiek,waga,wzrost):
        self.imie = imie
        self.nazwisko = nazwisko
        self._wiek = wiek
        self._waga = waga
        self._wzrost = wzrost

    @property
    def wiek(self):
        return self._wiek

    @wiek.setter
    def wiek(self,lata):
        self._wiek = lata

    @property
    def waga(self):
        return self._waga

    @waga.setter
    def waga(self, kg):
        self._waga = kg

    @property
    def wzrost(self):
        return self._wzrost

    @wzrost.setter
    def wzrost(self, cm):
        self._wzrost = cm


    @property
    def bmi(self):
        return self.waga/(self.wzrost/100)**2

os1 = Osoba("Jan","Kot",66,98,176)
print(f'Osoba: {os1.imie} {os1.nazwisko}')
print(f'bmi ciała: {os1.bmi:.2f}')
with open("bmi.txt","a",encoding="utf-8") as f:
    f.write("pierwszy pomiar: " + str(os1.bmi) + "\n")

os1.waga = 91
print(f'bmi ciała: {os1.bmi:.2f}')
with open("bmi.txt","a",encoding="utf-8") as f:
    f.write("drugi pomiar: " + str(os1.bmi) + "\n")

os1.waga = 87
print(f'bmi ciała: {os1.bmi:.2f}')
with open("bmi.txt","a",encoding="utf-8") as f:
    f.write("trzeci pomiar: " + str(os1.bmi) + "\n")


os1.waga = 82
print(f'bmi ciała: {os1.bmi:.2f}')
with open("bmi.txt","a",encoding="utf-8") as f:
    f.write("czwarty pomiar: " + str(os1.bmi) + "\n")





