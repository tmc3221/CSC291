import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    R = int(next(it))
    C = int(next(it))

    grid = [[0]*C for _ in range(R)]
    row_pop = [0]*R
    col_pop = [0]*C

    for i in range(R):
        for j in range(C):
            v = int(next(it))
            grid[i][j] = v
            row_pop[i] += v
            col_pop[j] += v


    # Find weighted median row
    total_row = sum(row_pop)
    target_row = (total_row + 1) // 2  # half
    # Round up
    acc = 0
    best_r = 0
    for i in range(R):
        acc += row_pop[i]
        if acc >= target_row:
            best_r = i
            break

    # Find the weighted median column
    total_col = sum(col_pop)
    target_col = (total_col + 1) // 2 # int div
    acc = 0

    best_c = 0


    for j in range(C):
        acc += col_pop[j]
        if acc >= target_col:
            best_c = j
            break

    # best r and best c
    total_cost = 0
    for i in range(R):
        di = abs(i - best_r)
        for j in range(C):
            dj = abs(j - best_c)
            total_cost += grid[i][j] * (di + dj)

    print(total_cost)

if __name__ == "__main__":
    main()

