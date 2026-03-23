def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

while True:
    n, t = map(int, input().split())
    if n == 0 and t == 0:
        break

    for _ in range(t):
        x, op, y = input().split()
        x = int(x)
        y = int(y)

        if op == '+':
            print((x + y) % n)
        elif op == '-':
            print((x - y) % n)
        elif op == '*':
            print((x * y) % n)
        else:
            g, inv, _ = egcd(y, n)
            if g != 1:
                print(-1)
            else:
                inv %= n
                print((x * inv) % n)
