MOD = 10**9 + 7 # bound

n = int(input())
result = 1

for _ in range(n):
    a = int(input())
    result = (result * a) % MOD

print(result)
