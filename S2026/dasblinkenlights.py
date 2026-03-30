import math

p, q, s = map(int, input().split())

lcm = (p * q) // math.gcd(p, q)

if lcm <= s:
    print("yes")
else:
    print("no")
