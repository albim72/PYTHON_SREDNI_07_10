from dataclasses import dataclass,field,astuple
@dataclass
class Fruit:
    nazwa:str
    cena:int
@dataclass
class Fruits:
    names:list = field(default_factory=lambda :[])
    colors:list = field(default_factory=lambda :[])
    cechy:list=field(default_factory=lambda :astuple(Fruit("kiwi",34)))

fr1 = Fruits()
fr1.names.append('Jabłko')
fr1.names.append('Gruszka')
fr1.names.append('Banan')

print(fr1)
fr2 = Fruits(['Truskawka','Jagoda','Kiwi'])
fr2 = Fruits
print(fr2)
