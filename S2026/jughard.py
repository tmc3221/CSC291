import math


t = int(input())

for _ in range(t):
    a, b, d = map(int, input().split())
    if d % math.gcd(a, b) == 0:
        print("Yes")
    else:
        print("No")
