#funkcja silnia n!=1*2*3*...*n dla n>=0
#double -> max: 1.8E+308
#n??? n=171

import sys
from silniaerror import SilniaError
print(sys.version)

sys.set_int_max_str_digits(0x1_000_000)

def silnia(n):
    if n<0:
        raise SilniaError(n)
    wynik=1
    for i in range(1,n+1):
        wynik *= i
    return wynik

try:
    n = int(input("podaj wartość argumentu n funkcji silnia: "))
    print(f"wynik funkcji silnia dla n={n} wynosi: {silnia(n)}")
except SilniaError as inf:
    print(inf)
