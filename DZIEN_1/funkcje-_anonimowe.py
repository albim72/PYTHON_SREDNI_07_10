print((lambda e:e+2)(56))
b = lambda u,w:2*u+w
print(b(2,7))
print(b("blue","color"))

h = lambda a,b,c=1:(a+b)/c

print(h(5,12,6))
print(h(5,12))

def multi(n):
    return lambda a:a*n

print(multi(7)(11))

liczba = [3,12,66,-23,0,116,-8,2,15,999,-34,189,14,-2,0,90]

parzysta = list(filter(lambda x:x%2==0,liczba))
print(parzysta)

cube = list(map(lambda x:x**3,liczba))
print(cube)

cube = set(map(lambda x:x**3,liczba))
print(cube)
