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

#przykład 2

def calc(x,l,k=4,n=3.33333,t=0):
    return l+x**3/math.sqrt(k-1)*n + t


print(calc(2,1,2,1))
print(calc(2,1,2))
print(calc(2,1))
print(calc(3,2,n=10,t=2))
