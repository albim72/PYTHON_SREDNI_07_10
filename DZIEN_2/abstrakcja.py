from abc import ABC,abstractmethod

class Prototyp(ABC):
    def __init__(self,x):
        self.x = x

    def msg(self):
        return "to jest metoda nieabstrakcyjna!!"

    @abstractmethod
    def policz(self):
        pass

    @abstractmethod
    def policz_x(self):
        return self.x*7


class Regular(Prototyp):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def policz(self):
        return 1006

    def policz_x(self):
        return super().policz_x() + self.y*3


re = Regular(3,5)
print(f'wynik policz() = {re.policz()}')
print(f'wynik policz_x() = {re.policz_x()}')
print(re.msg())
