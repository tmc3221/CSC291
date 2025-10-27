import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

result = []
run_start = nums[0]
prev = nums[0]
run_len = 1

for x in nums[1:]:
    if x == prev + 1:
        prev = x
        run_len += 1
    else:
        if run_len >= 3:
            result.append(f"{run_start}-{prev}")
        elif run_len == 2:
            result.append(str(run_start))
            result.append(str(prev))
        else:  # run_len == 1
            result.append(str(run_start))
        run_start = x
        prev = x
        run_len = 1

if run_len >= 3:
    result.append(f"{run_start}-{prev}")
elif run_len == 2:
    result.append(str(run_start))
    result.append(str(prev))
else:
    result.append(str(run_start))

print(" ".join(result))
