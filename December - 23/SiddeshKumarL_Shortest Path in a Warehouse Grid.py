from collections import deque

m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]

if grid[0][0] == 1 or grid[m-1][n-1] == 1:
    print(-1)
else:
    dist = [[-1]*n for _ in range(m)]
    dist[0][0] = 0
    q = deque([(0, 0)])
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    while q:
        x, y = q.popleft()
        if x == m-1 and y == n-1:
            break
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    print(dist[m-1][n-1])
