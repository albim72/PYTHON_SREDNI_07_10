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


