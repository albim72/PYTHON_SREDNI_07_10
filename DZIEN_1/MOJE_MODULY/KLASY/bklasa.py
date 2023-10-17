from funkcje.bfunkcje import *

class CDane:
    def __init__(self,lista,slownik):
        self.lista = lista
        self.slownik = slownik
        
    def rdl(self):
        return czytaj_liste(self.lista)
    
    def rdd(self):
        return czytaj_slownik(self.slownik)
