high = 1000
low = 1

while True:
    mid = (low + high) // 2
    print(mid, flush=True)
    user_input = input()

    if user_input == "correct":
       break
    elif user_input == "higher":
        low = mid + 1
    elif user_input == "lower":
        high = mid - 1
