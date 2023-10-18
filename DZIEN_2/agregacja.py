class Departament:
    def __init__(self,name,employees):
        self.name = name
        self.employees = employees

class Employee:
    def __init__(self,name,department):
        self.name = name
        self.department = department



department = Departament("IT",[])
employee1 = Employee("Janek Kot",department)
employee2 = Employee("Anna Nowak",department)
employee3 = Employee("Jarek Kos",department)
department.employees.append(employee1)
department.employees.append(employee2)
department.employees.append(employee3)

print(department.name)
print(len(department.employees))
print(department.employees[0].name)
print(department.employees[1].name)
print(department.employees[2].name)
