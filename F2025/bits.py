n = int(input())

for _ in range(n):
    num = input().strip()        
    result = []

    for k in range(1, len(num) + 1):
        prefix_val = int(num[:k])
        result.append(bin(prefix_val).count('1'))

    print(max(result))

