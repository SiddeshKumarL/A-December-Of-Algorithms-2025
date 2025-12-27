n = int(input().strip())
heights = list(map(int, input().split()))

peaks = []
for i in range(1, n - 1):
    if heights[i] > heights[i - 1] and heights[i] > heights[i + 1]:
        peaks.append(str(i))

if peaks:
    print(" ".join(peaks))
else:
    print(-1)
