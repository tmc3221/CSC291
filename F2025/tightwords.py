import sys
import math

def main():
    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        k, n = map(int, line.split())
        if n == 1:
            # all (k+1) words of length 1 are considered to be tight
            out.append("100.000000000")
            continue

        # dp for current and previous length
        prev = [1.0] * (k + 1)  # length = 1
        for _ in range(2, n + 1):
            cur = [0.0] * (k + 1)
            for d in range(k + 1):
                val = prev[d]
                if d > 0:
                    val += prev[d - 1]
                if d < k:
                    val += prev[d + 1]
                cur[d] = val
            prev = cur

        tight_total = sum(prev)
        total_words = (k + 1) ** n
        percentage = 100.0 * tight_total / total_words

        out.append(f"{percentage:.9f}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

