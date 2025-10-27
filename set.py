# diamonds
# squiggles
# ovals

# solid
# striped
# open

# red
# green
# purple

# Either all are the same or one is diff

# A how many symbols
# B Shape
# C How its filled in
# D color

class Card:
    def __init__(self, amount, shape, filling, color, idx):
        self.amount = amount
        self.shape = shape
        self.filling = filling
        self.color = color
        self.idx = idx

def ok(a, b, c):
    return (a == b == c) or (len({a, b, c}) == 3)

def is_set(c1, c2, c3):
    return (
        ok(c1.amount, c2.amount, c3.amount) and
        ok(c1.shape, c2.shape, c3.shape) and
        ok(c1.filling, c2.filling, c3.filling) and
        ok(c1.color, c2.color, c3.color)
    )

cards = []
for i in range(4):
    parts = input().split()
    for j in range(3):
        s = parts[j]
        cards.append(Card(int(s[0]), s[1], s[2], s[3], i*3 + j + 1))

res = []
n = len(cards)
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if is_set(cards[i], cards[j], cards[k]):
                res.append(tuple(sorted((cards[i].idx, cards[j].idx, cards[k].idx))))

if not res:
    print("no sets")
else:
    for a, b, c in sorted(res):
        print(a, b, c)

