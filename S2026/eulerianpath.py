# Use stack to keep track of the path
# When we follow an unused edge we push the next vertex onto the stack

import sys
from collections import deque

# Use stack to keep track of the path
# When we follow an unused edge we push the next vertex onto the stack
def eulerian_path(graph, n, undirected, indeg, outdeg, m):
    start = None
    end = None
    for v in range(n):
        diff = outdeg[v] - indeg[v]
        if diff == 1:
            if start is not None:
                return None
            start = v
        elif diff == -1:
            if end is not None:
                return None
            end = v
        elif diff != 0:
            return None



    # If it's an Euler circuit start anywhere with an outgoing edge
    if start is None:
        for v in range(n):
            if outdeg[v] > 0:
                start = v
                break
    if start is None:
        return [0]



    # ---- required connectivity check (ignore direction) ----
    active = [i for i in range(n) if indeg[i] + outdeg[i] > 0]
    seen = set([active[0]])
    q = deque([active[0]])
    while q:
        u = q.popleft()
        for w in undirected[u]:
            if w not in seen:
                seen.add(w)
                q.append(w)
    if any(x not in seen for x in active):
        return None

    # Stack/path
    stack = [start]
    path = []

    while stack:
        u = stack[-1]
        if graph[u]:                
            v = graph[u].pop()       # directed u -> v
            stack.append(v)
        else:
            path.append(stack.pop()) # backtrack

    path.reverse()



    if len(path) != m + 1:
        return None

    return path


if __name__ == "__main__":
    data = sys.stdin.read().strip().split()
    it = iter(data)
    out_lines = []

    # build each of the graphs
    for a, b in zip(it, it):
        n = int(a)
        m = int(b)
        if m == 0:
            break

        # Build graph like adk
        graph = {i: [] for i in range(n)}
        undirected = [[] for _ in range(n)]
        indeg = [0] * n
        outdeg = [0] * n

        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            graph[u].append(v)          # directed
            undirected[u].append(v)     # for connectivity only
            undirected[v].append(u)
            outdeg[u] += 1
            indeg[v] += 1

        path = eulerian_path(graph, n, undirected, indeg, outdeg, m)
        if path is None:
            out_lines.append("Impossible")
        else:
            out_lines.append(" ".join(map(str, path)))

    print("\n".join(out_lines))
