import sys
import math

def solve():
    lines = sys.stdin.read().strip().splitlines()
    i = 0
    out = []

    while i < len(lines):
        n = int(lines[i])
        i += 1

        if n == 0: # End of input
            break

        destinations = []

        for _ in range(n):
            parts = lines[i].split()
            i += 1

            x = float(parts[0])
            y = float(parts[1])

            angle = float(parts[3])
            j = 4

            while j < len(parts):
                cmd = parts[j]
                val = float(parts[j + 1])

                if cmd == "turn":
                    angle += val

                elif cmd == "walk":
                    rad = math.radians(angle)
                    x += val * math.cos(rad)
                    y += val * math.sin(rad)

                j += 2

            destinations.append((x, y))

        avg_x = sum(p[0] for p in destinations) / n
        avg_y = sum(p[1] for p in destinations) / n

        worst = 0.0
        for x, y in destinations:
            dist = math.hypot(x - avg_x, y - avg_y)
            worst = max(worst, dist)

        out.append(f"{avg_x:.10f} {avg_y:.10f} {worst:.10f}")

    print("\n".join(out))

if __name__ == "__main__":
    solve()
