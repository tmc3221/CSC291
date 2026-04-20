import sys
from collections import deque

input = sys.stdin.readline

n, m, s, t = map(int, input().split())

adj = [[] for _ in range(n)]
to = []
cap = []

def add_edge(u, v, c):
    idx = len(to)
    to.append(v)
    cap.append(c)
    adj[u].append(idx)

    to.append(u)
    cap.append(0)
    adj[v].append(idx ^ 1)

for _ in range(m):
    u, v, c = map(int, input().split())
    add_edge(u, v, c)

level = [-1] * n
ptr = [0] * n

# Basic bfs
def bfs():
    for i in range(n):
        level[i] = -1
    level[s] = 0
    q = deque([s])

    while q:
        u = q.popleft()
        for ei in adj[u]:
            v = to[ei]
            if cap[ei] > 0 and level[v] == -1:
                level[v] = level[u] + 1
                q.append(v)

    return level[t] != -1

# Basic dfs
def dfs(u, pushed):
    if pushed == 0:
        return 0
    if u == t:
        return pushed

    while ptr[u] < len(adj[u]):
        ei = adj[u][ptr[u]]
        v = to[ei]

        if cap[ei] > 0 and level[v] == level[u] + 1:
            tr = dfs(v, min(pushed, cap[ei]))
            if tr > 0:
                cap[ei] -= tr
                cap[ei ^ 1] += tr
                return tr

        ptr[u] += 1

    return 0

INF = 10**18

while bfs():
    for i in range(n):
        ptr[i] = 0
    while True:
        pushed = dfs(s, INF)
        if pushed == 0:
            break

# Find all vertices reachable from s in residual graph
visited = [False] * n
q = deque([s])
visited[s] = True

while q:
    u = q.popleft()
    for ei in adj[u]:
        v = to[ei]
        if not visited[v] and cap[ei] > 0:
            visited[v] = True
            q.append(v)

result = [i for i in range(n) if visited[i]]

print(len(result))
for v in result:
    print(v)
