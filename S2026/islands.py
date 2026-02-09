# Input - Grid
# C - cloud, cant tell
# L - Land
# W - Water

# Output - Min number of islands
import sys

def solve():
    length, width = map(int, input().split())

    grid = [list(sys.stdin.readline().strip()) for _ in range(length)]
    visited = [[False for _ in range(width)] for _ in range(length)]

    def dfs(i, j):
        if i < 0 or i >= length or j < 0 or j >= width or visited[i][j] or grid[i][j] == 'W':
            return

        visited[i][j] = True

        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(i + di, j + dj)

    islands = 0
    
    for i in range(length):
        for j in range(width):
            if grid[i][j] == 'L' and not visited[i][j]:
                islands += 1
                dfs(i, j)

    print(islands)

if __name__ == "__main__":
    solve()
        
