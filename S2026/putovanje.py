n, c = map(int, input().split())
arr = list(map(int, input().split()))

# arr is the fruits
max_fruits = 0

# i - our starting point
for i in range(n):
    current_stomach = 0
    eaten = 0

    # j - how far off from i
    for j in range(n - i):
        fruit = arr[i + j]

        # if we can eat it
        if current_stomach + fruit <= c:
            current_stomach += fruit
            eaten += 1

    max_fruits = max(max_fruits, eaten)

print(max_fruits)

