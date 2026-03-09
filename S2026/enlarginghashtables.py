import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

while True:
    n = int(input())
    if n == 0:
        break

    candidate = 2 * n + 1
    while not is_prime(candidate):
        candidate += 1

    if is_prime(n):
        print(candidate)
    else:
        print(f"{candidate} ({n} is not prime)")
