from collections import deque

M, N = map(int, input().split())
grid = [list(input().strip()) for _ in range(M)]

start = None
for i in range(M):
    for j in range(N):
        if grid[i][j] == 'S':
            start = (i, j)
            break
    if start:
        break

dirs = [(1,0), (-1,0), (0,1), (0,-1)]
visited = [[[False]* (1<<10) for _ in range(N)] for __ in range(M)]
sx, sy = start
q = deque()
q.append((sx, sy, 0, 0))
visited[sx][sy][0] = True

res = -1
while q:
    x, y, keys, d = q.popleft()
    if grid[x][y] == 'T':
        res = d
        break
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <= nx < M and 0 <= ny < N:
            cell = grid[nx][ny]
            if cell == '#':
                continue
            new_keys = keys
            if 'a' <= cell <= 'j':
                new_keys |= 1 << (ord(cell) - ord('a'))
            if 'A' <= cell <= 'J':
                if not (keys & (1 << (ord(cell) - ord('A')))):
                    continue
            if not visited[nx][ny][new_keys]:
                visited[nx][ny][new_keys] = True
                q.append((nx, ny, new_keys, d+1))

print(res)
