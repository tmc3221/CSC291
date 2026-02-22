import sys
from collections import deque

def solve():
    input = sys.stdin.readline # Takein whole line sperate by n and m
    n, m = map(int, input().split())


    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        g[a].append((b, c))
        g[b].append((a, c))
        # Creaate graph a -> b weight c and b -> a weight c

    INF = 10**18 # Upper limit
    dist = [INF] * (n + 1)
    dist[1] = 0
    dq = deque([1])
    
    # Main loop
    while dq:
        u = dq.popleft()
        du = dist[u]
        for v, w in g[u]:
            nd = du + w
            if nd < dist[v]:
                dist[v] = nd
                if w == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)

    print(dist[n])

if __name__ == "__main__":
    solve()
