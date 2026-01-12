import sys
import math

def main():
    data = sys.stdin.read().strip()
    if not data:
        return
    r = int(data)
    rr = r * r

    total = 0
    for x in range(r + 1):
        y_max = math.isqrt(rr - x * x)
        if x == 0:
            total += 2 * y_max + 1
        else:
            total += 4 * y_max + 2

    print(total)

if __name__ == "__main__":
    main()

