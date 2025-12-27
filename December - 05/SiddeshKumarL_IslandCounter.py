

from collections import deque

R, C = map(int, input().split())

grid = []
for _ in range(R):
    grid.append(list(map(int, input().split())))

visited = [[False] * C for _ in range(R)]

def bfs(sr, sc):
    queue = deque()
    queue.append((sr, sc))
    visited[sr][sc] = True

    while queue:
        r, c = queue.popleft()

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < R and 0 <= nc < C:
                if not visited[nr][nc] and grid[nr][nc] == 1:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

islands = 0

for i in range(R):
    for j in range(C):
        if grid[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            islands += 1

print(islands)
