from functools import partial

def power(a,b):
    return a**b

pow2 = partial(power,b=2)
pow4 = partial(power,b=4)
power_of_5 = partial(power,5)

print(power(2,3))
print(pow2(2))
print(pow4(2))
print(power_of_5(2))

print(f'funkcja użyta w partial pow2: {pow2.func}')
print(f'domyślne słow kluczowe w partial pow2: {pow2.keywords}')
print(f'domyślne argumenty w partial power_of_5: {pow2.args}')
