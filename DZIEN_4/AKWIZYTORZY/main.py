from decimal import Decimal
from akwizytor import Akwizytor
from akwizytornaetacie import Akwizytornaetacie


class FirmaABC:
    def __repr__(self):
        return 'Szef wszystkich szefów...'

    @property
    def wynagrodzenie(self):
        return Decimal('10_000_000.00')


abc = FirmaABC()

s = Akwizytornaetacie('Anna','Kot',767565787,Decimal('12_123_000.00'),
                      Decimal('7.20'),Decimal('8200.00'))

c = Akwizytor('Leon','Rybak',867557567,Decimal('12_145_000.00'),
                      Decimal('8.66'))

liderzy = [c,s,abc]

for lider in liderzy:
    print(lider)
    print(f'{lider.wynagrodzenie:,.2f}\n')
