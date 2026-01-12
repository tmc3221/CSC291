import sys

def main():
    it = iter(sys.stdin.read().strip().split())
    T = int(next(it))
    out_lines = []

    for case in range(1, T + 1):
        n = int(next(it))
        nums = [int(next(it)) for _ in range(n)]

        out_lines.append(f"Case #{case}:")

        sum_to_mask = {}
        found = False

        for mask in range(1, 1 << n):
            s = 0
            # Compute sum 
            for i in range(n):
                if mask & (1 << i):
                    s += nums[i]

            if s in sum_to_mask:
                # We found two different subsets with the same sum
                first_mask = sum_to_mask[s]
                second_mask = mask

                # Build the lines for outputh
                subset1 = []
                subset2 = []
                for i in range(n):
                    if first_mask & (1 << i):
                        subset1.append(str(nums[i]))
                    if second_mask & (1 << i):
                        subset2.append(str(nums[i]))

                out_lines.append(" ".join(subset1))
                out_lines.append(" ".join(subset2))
                found = True
                break
            else:
                sum_to_mask[s] = mask

        if not found:
            # Edge Case
            out_lines.append("Impossible")

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()

