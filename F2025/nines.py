def nines(counts):
    total = sum(counts)
    
    # Check for any odd digit except 5 that appears at least once
    odd_digits = [1, 3, 7, 9]
    odd_present = any(counts[d] > 0 for d in odd_digits)
    
    # Check if 5 appears AND any even digit appears
    even_digits = [2, 4, 6, 8]
    five_with_even = counts[5] > 0 and any(counts[d] > 0 for d in even_digits)
    
    if odd_present or five_with_even:
        return 1
    return total


n = int(input())
freq = [0] * 10   
for _ in range(n):
    digit = int(input())
    freq[digit] += 1

print(nines(freq))

