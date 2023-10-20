numbers = [8,3,1,2,5,4,7,6,7,2,5,8,6,2]
group1 = {2,3,5,7}
group2 = {3,6,8}

class Sorter:
    def __init__(self,group):
        self.group = group
        self.found = False

    def __call__(self,x):
        if x in self.group:
            self.found = True
            return (0,x)
        return (1,x)

so1 = Sorter(group1)
numbers.sort(key=so1)
print(numbers)

so2 = Sorter(group2)
numbers.sort(key=so2)
print(numbers)
