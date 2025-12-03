import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    n = int(next(it))  #  instruments
    m = int(next(it))  # inotes

    # For each instrument store the set of notes it can play
    can_play = []
    for _ in range(n):
        k = int(next(it))
        notes = set()
        for _ in range(k):
            notes.add(int(next(it)))
        can_play.append(notes)

    tune = [int(next(it)) for _ in range(m)]

    INF = 10**9
    # dp for previous note
    prev = [INF] * n

    # Initialize for first note
    # we want to find 0 switches
    first_note = tune[0]
    for i in range(n):
        if first_note in can_play[i]:
            prev[i] = 0

    # Begun processing notes
    for idx in range(1, m):
        note = tune[idx]
        best_prev = min(prev)
        cur = [INF] * n
        for i in range(n):
            if note in can_play[i]:
                # stay on i or switch from best instrument
                stay = prev[i]
                switch = best_prev + 1
                cur[i] = min(stay, switch)
        prev = cur

    ans = min(prev)
    print(ans)

if __name__ == "__main__":
    main()

