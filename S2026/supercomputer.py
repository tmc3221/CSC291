import sys

def solve():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    q = int(data[1])
    bit = [0] * (n + 1)   # Fenwick counts of 1s
    arr = bytearray(n + 1)

    def add(i, delta):
        while i <= n:
            bit[i] += delta
            i += i & -i

    def prefix(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    out = []
    p = 2

    out_append = out.append
    add_local = add
    prefix_local = prefix
    arr_local = arr

    for _ in range(q):
        op = data[p]
        p += 1

        if op == b'F':
            i = int(data[p]); p += 1

            if arr_local[i] == 0:
                arr_local[i] = 1
                add_local(i, 1)
            else:
                arr_local[i] = 0
                add_local(i, -1)

        else:
            a = int(data[p]); b = int(data[p+1]); p += 2

            if a > b:
                a, b = b, a
            out_append(str(prefix_local(b) - prefix_local(a - 1)))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
