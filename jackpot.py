n = int(input())

BILLION = 10**9

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return a // find_gcd(a, b) * b

for i in range(n):
    w = int(input())

    nums = list(map(int, input().split()))


    more = False
    curr = 1
    for x in nums:
        curr = find_lcm(curr, x)
       
        if curr > BILLION:
            more = True
            break

    print("More than a billion." if more else str(curr))
