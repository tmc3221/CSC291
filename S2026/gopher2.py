import sys
import math

def can_reach(gx, gy, hx, hy, max_dist):
    return math.hypot(gx - hx, gy - hy) <= max_dist + 1e-9

def dfs(gopher_idx, graph, seen, match_to):
    for hole_idx in graph[gopher_idx]:
        if hole_idx in seen:
            continue
        seen.add(hole_idx)

        if match_to[hole_idx] == -1 or dfs(match_to[hole_idx], graph, seen, match_to):
            match_to[hole_idx] = gopher_idx
            return True
    return False

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    i = 0
    out = []

    while i < len(data):
        n = int(data[i]); i += 1
        m = int(data[i]); i += 1
        s = int(data[i]); i += 1
        v = int(data[i]); i += 1

        gophers = []
        for _ in range(n):
            x = float(data[i]); y = float(data[i + 1]); i += 2
            gophers.append((x, y))

        holes = []
        for _ in range(m):
            x = float(data[i]); y = float(data[i + 1]); i += 2
            holes.append((x, y))

        max_dist = s * v

        graph = [[] for _ in range(n)]
        for gi, (gx, gy) in enumerate(gophers):
            for hi, (hx, hy) in enumerate(holes):
                if can_reach(gx, gy, hx, hy, max_dist):
                    graph[gi].append(hi)

        match_to = [-1] * m
        matched = 0

        for gopher_idx in range(n):
            seen = set()
            if dfs(gopher_idx, graph, seen, match_to):
                matched += 1

        out.append(str(n - matched))

    print("\n".join(out))

if __name__ == "__main__":
    solve()
