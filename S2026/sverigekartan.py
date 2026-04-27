from collections import deque
import sys

def bfs(grid, visited, start, n, m):
    q = deque([start])
    visited[start[0]][start[1]] = True
    count = 1

    while q:
        x, y = q.popleft()

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy

            if (
                0 <= nx < n and
                0 <= ny < m and
                not visited[nx][ny] and
                grid[nx][ny] != "."
            ):
                visited[nx][ny] = True
                q.append((nx, ny))
                count += 1

    return count


def main():
    input = sys.stdin.readline

    n = int(input())
    m = int(input())
    q = int(input())

    grid = []
    sx = sy = -1

    for i in range(n):
        row = list(input().strip())
        grid.append(row)
        for j, c in enumerate(row):
            if c == "S":
                sx, sy = i, j

    visited = [[False] * m for _ in range(n)]
    landmass = bfs(grid, visited, (sx, sy), n, m)

    print(landmass)

    for _ in range(q):
        x, y = map(int, input().split())
        x -= 1
        y -= 1

        grid[x][y] = "#"

        # Skip
        if visited[x][y]:
            print(landmass)
            continue

        # Check whether it touches the current reachable landmass before running BFS
        touches_sweden = False
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:
                touches_sweden = True
                break

        # Only now do BFS from the new square       
        if touches_sweden:
            landmass += bfs(grid, visited, (x, y), n, m)

        print(landmass)


if __name__ == "__main__":
    main()
