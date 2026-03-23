n = int(input())

def modinv(a, p):
    return pow(a, p - 2, p)

for _ in range(n):
    p, s = input().split()
    p = int(p)
    m = len(s)

    vals = []
    for c in s:
        if c == '*':
            vals.append(0)
        else:
            vals.append(ord(c) - ord('a') + 1)

    mat = []
    for i in range(1, m + 1):
        row = []
        for j in range(m):
            row.append(pow(i, j, p))
        row.append(vals[i - 1])
        mat.append(row)

    for col in range(m):
        for row in range(col, m):
            if mat[row][col] != 0:
                mat[col], mat[row] = mat[row], mat[col]
                break

        inv = modinv(mat[col][col], p)
        for j in range(col, m + 1):
            mat[col][j] = (mat[col][j] * inv) % p

        for row in range(m):
            if row != col and mat[row][col] != 0:
                factor = mat[row][col]
                for j in range(col, m + 1):
                    mat[row][j] = (mat[row][j] - factor * mat[col][j]) % p

    ans = []
    for i in range(m):
        ans.append(str(mat[i][m]))

    print(" ".join(ans))
