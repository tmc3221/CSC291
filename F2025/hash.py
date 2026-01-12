import sys

def ask(c, r):
    # send query and read reply
    print(f"? {c} {r}", flush=True)
    line = sys.stdin.readline()
    if not line:
        sys.exit(0)  
    return int(line.strip())

def main():
    line = sys.stdin.readline()
    if not line:
        return
    n = int(line)

    r = 1  # arbitrary starting room number

    c = ask(n, r)
    if c == n:
        print(f"! {c} {r}", flush=True)
        return

    # Second query: r2 = f^(n-c)(r)
    k = n - c
    r2 = ask(k, r)

    print(f"! {c} {r2}", flush=True)

if __name__ == "__main__":
    main()

