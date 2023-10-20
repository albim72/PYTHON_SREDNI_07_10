import math
import operator
import time
import itertools
from itertools import product

#przykład 1
L1 = [1,2,3]
L2 = [2,3,4]

t1 = time.time()

a,b,c = map(operator.mul,L1,L2)

t2 = time.time()

print(f"wynik dla wartości L1 i L2: {a},{b},{c}")
print(f"czas wykonania funkcji: {t2-t1} s")

#a,b,c = math.prod(L1,L2)
for i in range(3):
    print(L1[i]*L2[i],end = " ")

#przykład 2
print()
print("*"*50)

for i in itertools.count(5,5):
    if i==135:
        break
    else:
        print(i, end = " ")
print()
print("*"*50)
#przykład 3
count = 0
for i in itertools.cycle('ABCDE'):
    if count > 7:
        break
    else:
        print(i, end=" ")
        count += 1

print()
print("*"*50)
#przykład 4

cykl = ['sen','dieta','trening siłowy','trening wysiłkowy','badania']

iterators = itertools.cycle(cykl)

for i in range(18):
    print(next(iterators),end=" ")

print()
print("*"*50)
#przykład 5

print(f'szybkie wyświetlenie wartości: {list(itertools.repeat(25,16))}')

print()
print("*"*50)
#przykład 6

print(f"iloczyn kartezjański z użyciem kontenrów: {list(product(['trening','psychika','walka'],['2','5']))}")
print("\n")
print(f"iloczyn kartezjański z użyciem kontenrów - drugi przypadek: {list(product('ABC',[4,6,8,9]))}")
print("\n")
print(f"iloczyn kartezjański z użyciem reapeat: {list(product([1,3,5],repeat=4))}")

