#przykład 1

def liczby():
    for i in range(17):
        yield i*2

print(liczby())
for p in liczby():
    print(p)

#przykład 2
def wznowienie(n,k):
    print("wstrzymanie działania 1")
    yield 1001
    print("wznowienie działania 2")

    print("wstrzymanie działania 2")
    yield n+k
    print("wznowienie działania 3")

    print("wstrzymanie działania 3")
    yield n-k
    print("wznowienie działania 4")

    print("wstrzymanie działania 4")
    yield n*k
    print("wznowienie działania 5")

    print("wstrzymanie działania 5")
    yield n/k
    print("wznowienie działania 6")

print(wznowienie(5,8))

for i in wznowienie(7,3):
    print("_"*30)
    print(f'zwrócono wartość: {i}')

#przykład3

def gen():
    x=0
    while True:
        y = yield x
        if y is None:
            x = x+1
        else:
            x=y

g = gen()

print(next(g))
print(next(g))
print(next(g))

print(g.send(119))
print(next(g))
print(next(g))


