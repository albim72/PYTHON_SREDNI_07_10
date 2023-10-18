from figura import Figura
from kwadrat import Kwadrat

class Prostokat(Figura):
    def __new__(cls,szer:float,wys:float):
        if szer == wys:
            return Kwadrat(bok=szer)
        return object.__new__(Prostokat)
    
    def policz_pole(self):
        return self.a * self.b
