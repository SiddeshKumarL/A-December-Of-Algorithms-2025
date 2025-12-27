from collections import deque

V, E = map(int, input().split())
adj = [[] for _ in range(V)]
for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

state = list(map(int, input().split()))
dist = [-1] * V
q = deque()

for i in range(V):
    if state[i] == 1:
        dist[i] = 0
        q.append(i)

while q:
    u = q.popleft()
    for v in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)

if any(d == -1 for d in dist):
    print(-1)
else:
    print(max(dist))
