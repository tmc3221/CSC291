import sys

def main():
    it = iter(sys.stdin.read().strip().split())
    try:
        n = int(next(it))
    except StopIteration:
        return

    pts = []
    for _ in range(n):
        x = int(next(it))
        y = int(next(it))
        pts.append((x, y))

    INF = 10**18
    used = [False] * n
    dist = [INF] * n
    dist[0] = 0  # start MST 

    total = 0




    for _ in range(n):
        # pick next vertex with minimal d
        u = -1
        best = INF
        for i in range(n):
            if not used[i] and dist[i] < best:
                best = dist[i]
                u = i
        used[u] = True
        total += dist[u]

        xu, yu = pts[u]
        for v in range(n):
            if not used[v]:
                xv, yv = pts[v]
                w = abs(xu - xv) + abs(yu - yv)
                if w < dist[v]:
                    dist[v] = w

    # each move is forth and back, so multiply by 2
    print(2 * total)

if __name__ == "__main__":
    main()

