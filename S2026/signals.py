import sys

def binary_search(lis, x):
    left, right = 0, len(lis)
    while left < right:
        mid = (left + right) // 2
        if lis[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

def main():
    n = int(sys.stdin.readline())
    ports = [int(sys.stdin.readline()) for _ in range(n)]

    lis = []
    for port in ports:
        idx = binary_search(lis, port)
        if idx == len(lis):
            lis.append(port)
        else:
            lis[idx] = port
    print(len(lis))

if __name__ == "__main__":
    main()

