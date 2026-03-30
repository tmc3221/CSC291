import sys, math

for line in sys.stdin:
    ans = 1
    for x in map(int, line.split()):
        ans = ans * x // math.gcd(ans, x)
    print(ans)
