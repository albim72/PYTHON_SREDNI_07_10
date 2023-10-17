#import dane
#import dane as dn
from dane import nrfilii as nf
from dane import book as bk
from funkcje.bfunkcje import czytaj_liste,czytaj_slownik

from klasa.bklasa import CDane

print("____________ dane _________________")
print(nf)
print(bk)

print("____________ dane przez funkcje _________________")
czytaj_liste(nf)
czytaj_slownik(bk)

print("____________ dane przez klasę _________________")
cd = CDane(nf,bk)
cd.rdl()
cd.rdd()
