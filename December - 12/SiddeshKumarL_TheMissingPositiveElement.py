n = int(input().strip())
arr = list(map(int, input().split()))

for i in range(n):
    while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
        correct_idx = arr[i] - 1
        arr[i], arr[correct_idx] = arr[correct_idx], arr[i]

missing = duplicate = -1
for i in range(n):
    if arr[i] != i + 1:
        missing = i + 1
        duplicate = arr[i]
        break

print(f"Missing Number: {missing}")
print(f"Duplicate Number: {duplicate}")
