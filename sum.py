from collections import deque
from math import isqrt

t = int(input())

for _ in range(t):
    target = int(input())
    result = deque()
    sum_n = 0   # 
    found = False

    max_L = (1 + isqrt(1 + 8 * target)) // 2

    for L in range(2, max_L + 1):
        numerator = target - (L * (L - 1) // 2)
        if numerator <= 0:
            break
        if numerator % L == 0:
            a = numerator // L
            if a >= 1:
                result.clear()
                for x in range(a, a + L):
                    result.append(x)
                print(f"{target} = " + " + ".join(map(str, result)))
                found = True
                break

    if not found:
        print("IMPOSSIBLE")

