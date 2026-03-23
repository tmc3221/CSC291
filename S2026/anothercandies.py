t = int(input())

for _ in range(t):
    input()
    children = int(input())
    total = 0

    for _ in range(children):
        total += int(input())

    if total % children == 0:
        print("YES")
    else:
        print("NO")

