from collections import deque

n = int(input().strip())
q = deque(map(int, input().split()))
sorted_vals = sorted(q)
out = []

for target in sorted_vals:
    idx = 0
    while q[idx] != target:
        idx += 1
    q.rotate(-idx)
    out.append(q.popleft())

print(*out)
