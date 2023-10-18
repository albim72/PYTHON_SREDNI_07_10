class Address:
    def __init__(self,street,city,country):
        self.street = street
        self.city = city
        self.country = country

class Person:
    def __init__(self,name,adress):
        self.name = name
        self.adress = adress

    def getname(self):
        return self.name

class Employee:
    def __init__(self,name,address,employee_id):
        self.employee_id = employee_id
        self.person = Person(name,address)



address = Address("Złota 5/2 12-800","Kraków","Polska")
employee = Employee("Jan Kot",address,34535)

print(employee.person.name)
print(employee.person.adress.city)
print(employee.employee_id)
print(employee.person.getname())




