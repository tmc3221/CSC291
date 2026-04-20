import sys
from collections import deque

input = sys.stdin.readline

n, m, s, t = map(int, input().split())

adj = [[] for _ in range(n)]
to = []
cap = []
orig = []

def add_edge(u, v, c):
    idx = len(to)
    to.append(v)
    cap.append(c)
    orig.append(c)
    adj[u].append(idx)

    to.append(u)
    cap.append(0)
    orig.append(0)
    adj[v].append(idx ^ 1)

    return idx

original_edges = []

for _ in range(m):
    u, v, c = map(int, input().split())
    idx = add_edge(u, v, c)
    original_edges.append((u, v, idx))

level = [-1] * n
ptr = [0] * n

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

flow = 0
INF = 10**18

while bfs():
    for i in range(n):
        ptr[i] = 0
    while True:
        pushed = dfs(s, INF)
        if pushed == 0:
            break
        flow += pushed

flow_map = {}
for u, v, idx in original_edges:
    f = orig[idx] - cap[idx]
    if f > 0:
        flow_map[(u, v)] = flow_map.get((u, v), 0) + f

result = [(u, v, f) for (u, v), f in flow_map.items() if f > 0]

print(n, flow, len(result))
for u, v, f in result:
    print(u, v, f)
