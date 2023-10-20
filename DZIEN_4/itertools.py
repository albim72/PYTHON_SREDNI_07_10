import math
import operator
import time
import itertools

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
