import sys

# Hlep check what we have theat is connected
def is_connected(n, adj):
    visited = [False] * n
    queue = [0]
    visited[0] = True
    count = 1
    
    while queue:
        u = queue.pop(0)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                count += 1
                queue.append(v)
    
    return count == n

def solve():
    while True:
        line = sys.stdin.readline().split()


        if not line: break
        p, c = map(int, line)

        if p == 0 and c == 0: break

        edges = []
        for _ in range(c):
            edges.append(list(map(int, sys.stdin.readline().split())))

        at_risk = False
        
        # Remove one by one
        for i in range(c):
            # Rebuild adjacency list w/o edge i
            adj = [[] for _ in range(p)]
            for j in range(c):


                if i == j: continue  # Skip number
                u, v = edges[j]
                adj[u].append(v)
                adj[v].append(u)
            
            # If removing this edge disconnects the party then it is a bridge
            if not is_connected(p, adj):
                at_risk = True
                break
        
        print("Yes" if at_risk else "No")

if __name__ == "__main__":
    solve()
