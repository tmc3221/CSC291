from collections import defaultdict
import sys

n, m = map(int, sys.stdin.readline().split())

edges = defaultdict(list)
forced = {}

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())

    if a < 0:
        a = -a
        forced[a] = b
        edges[a].append(b) 
    else:
        edges[a].append(b)

def follow_forced(start):
    seen = set()
    curr = start

    while curr in forced:
        if curr in seen:
            return None  # forced cycle will never stop
        seen.add(curr)
        curr = forced[curr]

    return curr

# Rooms reachable by only forced commands from room 1
main_path = []
seen = set()
curr = 1

while True:
    if curr in seen:
        break
    seen.add(curr)
    main_path.append(curr)

    if curr not in forced:
        break

    curr = forced[curr]

stopping = set()

# No bug used
end = follow_forced(1)
if end is not None:
    stopping.add(end)

# Use the bug once from any room on the forced path
for node in main_path:
    for nb in edges[node]:
        # skip the normal forced edge
        if node in forced and forced[node] == nb:
            continue

        end = follow_forced(nb)
        if end is not None:
            stopping.add(end)

print(len(stopping))
