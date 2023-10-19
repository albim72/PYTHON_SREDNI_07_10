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
        self.waga = kg

    @property
    def wzrost(self):
        return self._wzrost

    @wzrost.setter
    def wzrost(self, cm):
        self._wiek = cm
        
    
        
        
        
        
        
        
