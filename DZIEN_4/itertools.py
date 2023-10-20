import math
import operator
import time

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
