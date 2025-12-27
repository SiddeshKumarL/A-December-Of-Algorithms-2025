# December 27 - Signal Propagation in a Network
import heapq

N = int(input().strip())
M = int(input().strip())
adj = [[] for _ in range(N)]
for _ in range(M):
    u, v, t = map(int, input().split())
    adj[u].append((v, t))
S = int(input().strip())

INF = 10**18
dist = [INF]*N
dist[S] = 0
pq = [(0, S)]
while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v, w in adj[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

if any(d == INF for d in dist):
    print(-1)
else:
    print(max(dist))
