# palindrome like problem
# n /2

import sys

# Constraint
MOD = 10**9 + 7

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    L, R = map(int, data)

    ans = 0
    C = 0           # current ceiling``(N/2)
    pow5 = 1        
    pow2 = 1        

    for N in range(1, R + 1):
        newC = (N + 1) // 2
        if newC > C:
            # C increases by 1 each time this happens
            C = newC
            pow5 = (pow5 * 5) % MOD
            pow2 = (pow2 * 2) % MOD

        if N >= L:
            ans = (ans + pow5 + pow2) % MOD

    print(ans)

if __name__ == "__main__":
    main()

