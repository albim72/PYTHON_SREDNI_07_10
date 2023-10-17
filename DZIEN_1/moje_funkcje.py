import math

#przykład nr 1

def g(x):
    return x*math.sqrt(x)

n=100
def policz(a,b,c,y=5):
    global n
    n = (a+b)*y-c + n - g(b)
    return n

print(policz(4,7,2,6))
print(policz(6.7,3,6.88,2))
print(policz(6.7,3,6.88))
print(n)
