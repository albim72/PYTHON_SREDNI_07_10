from dataclasses import dataclass,astuple,asdict,field

@dataclass
class Person:
    city:str
    firstname:str = "Jan"
    lastname:str = "Kot"
    age:int = 30
    job:str = "Data Developer"
    full_name:str = field(init=False,repr=False)


    def __repr__(self):
        return f"Pracownik {self.firstname} {self.lastname}, stanowisko: {self.job}, wiek: {self.age}"

    def __post_init__(self):
        self.full_name = self.firstname + " " + self.lastname

os1 = Person("Kraków",age="trzydzieści")
print(os1)
print(os1.full_name)

os2 = Person("Kielce","Olga","Nowak",23,"sekretarka")
print(os2)
print(os2.full_name)

print(astuple(os2))
print(asdict(os2))
