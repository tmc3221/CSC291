t = int(input())

pos = {
    '1': (0, 0), '2': (0, 1), '3': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '7': (2, 0), '8': (2, 1), '9': (2, 2),
    '0': (3, 1)
}

def ok(x):
    s = str(x)
    for i in range(len(s) - 1):
        r1, c1 = pos[s[i]]
        r2, c2 = pos[s[i + 1]]
        if r2 < r1 or c2 < c1:
            return False
    return True

for _ in range(t):
    n = int(input())

    d = 0
    while True:
        if n - d >= 0 and ok(n - d):
            print(n - d)
            break
        if ok(n + d):
            print(n + d)
            break
        d += 1

