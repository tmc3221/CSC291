import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    A = list(map(int, data[1:]))

    sumA = sum(A)
    minA = min(A)

    ans = sumA + (n - 2) * minA
    print(ans)

if __name__ == "__main__":
    main()
