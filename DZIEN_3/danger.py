mojkod = '''
a=5
b=4
print(f'a x b = {a*b}')
'''

exec(mojkod)

import os
code = input('Co chcesz disiaj zrobić? ')
exec(code)


def policz_obwod(a):
    return 4*a

def policz_pole(a):
    return a**2

expr = input("Wpisz funkcję: ")

for a in range(6,25,5):
    if (expr == 'policz_obwod(a)'):
        print(f"jeśli długość boku wynosi: {a}, obwód = {eval(expr)}")
    elif (expr == 'policz_pole(a)'):
        print(f"jeśli długość boku wynosi: {a}, pole = {eval(expr)}")
    else:
        print('Zle podana funkcja!')
        break

a = "68"

print(a*11)
print(eval(a)*11)
print(float(a)*11)
