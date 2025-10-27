import math

target = float(input())
ln_t = math.log(target)

def g(x):
    return x * math.log(x)

low = 1.0 / math.e
high = max(target, 1.0)
while g(high) < ln_t:
    high *= 2.0

while True:
    mid = (low + high) / 2.0
    val = g(mid)
    if abs(val - ln_t) <= 1e-12:
        print(f"{mid:.10f}")
        break
    elif val > ln_t:
        high = mid
    else:
        low = mid

