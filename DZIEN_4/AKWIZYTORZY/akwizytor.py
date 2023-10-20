from decimal import Decimal

class Akwizytor:
    """
    Pracownik, którego wynagrodzenie jest wyłącznie prowizją
    od sprzedaży
    """

    def __init__(self, imie,nazwisko,nr_ubezpieczenia,sprzedaz,prowizja):
        self._imie = imie
        self._nazwisko = nazwisko
        self._nr_ubezpieczenia = nr_ubezpieczenia
        self.sprzedaz = sprzedaz
        self.prowizja = prowizja


    @property
    def imie(self):
        return self._imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @property
    def nr_ubezpieczenia(self):
        return self._nr_ubezpieczenia

    @property
    def sprzedaz(self):
        return self._sprzedaz

    @sprzedaz.setter
    def sprzedaz(self,kwota):
        if kwota<Decimal('0.00'):
            raise ValueError('Wartość sprzedaży nie może być ujemna')
        self._sprzedaz = kwota

    @property
    def prowizja(self):
        return self._prowizja

    @prowizja.setter
    def prowizja(self, procent):
        if not (Decimal('0.0')<procent<=Decimal('30.0')):
            raise ValueError('Prowizja nie może być ujemna i nie może przekraczać wartości 30%')
        self._prowizja = procent

    @property
    def wynagrodzenie(self):
        return self.sprzedaz * (self.prowizja/Decimal('100.0'))
    
    def __repr__(self):
        return (f'Akwizytor: ' +
                f'{self.imie} {self.nazwisko}\n'
                f'numer ubezpiecznia: {self.nr_ubezpieczenia}\n'
                f'sprzedaż: {self.sprzedaz:.2f}\n'
                f'prowizja: {self.prowizja:.2f}'
                )
    

