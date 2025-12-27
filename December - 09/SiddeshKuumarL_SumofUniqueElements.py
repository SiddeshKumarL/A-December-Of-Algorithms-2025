def sum_of_unique(nums):
    freq = {}

    for x in nums:
        freq[x] = freq.get(x, 0) + 1

    total = 0
    for x, c in freq.items():
        if c == 1:
            total += x
    return total


n = int(input().strip())

arr = list(map(int, input().split()))

arr = arr[:n]

print(sum_of_unique(arr))
