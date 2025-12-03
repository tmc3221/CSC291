import sys
from collections import deque
# BFS

def main():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out_lines = []

    MAX_TIME = 3600 # hour

    for _ in range(t):
        n = int(next(it))
        target = int(next(it))

        buttons = [int(next(it)) for _ in range(n)]

        INF = 10**9
        dist = [INF] * (MAX_TIME + 1)
        dist[0] = 0
        q = deque([0])

        while q:
            cur = q.popleft()
            for b in buttons:
                nxt = cur + b
                if nxt < 0:
                    nxt = 0
                elif nxt > MAX_TIME:
                    nxt = MAX_TIME
                if dist[nxt] > dist[cur] + 1:
                    dist[nxt] = dist[cur] + 1
                    q.append(nxt)



        # Find smallest time >= target with finite distance
        t2 = target
        if t2 > MAX_TIME:
            t2 = MAX_TIME
        while t2 <= MAX_TIME and dist[t2] == INF:
            t2 += 1

        presses = dist[t2]
        extra = t2 - target
        out_lines.append(f"{presses} {extra}")

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()

