# December 26 - Mountain Climber – Longest Ascending Path
import sys
sys.setrecursionlimit(10**7)

M, N = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(M)]
dp = [[0]*N for _ in range(M)]
dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def dfs(x, y):
    if dp[x][y] != 0:
        return dp[x][y]
    best = 1
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <= nx < M and 0 <= ny < N and mat[nx][ny] > mat[x][y]:
            best = max(best, 1 + dfs(nx, ny))
    dp[x][y] = best
    return best

ans = 0
for i in range(M):
    for j in range(N):
        ans = max(ans, dfs(i, j))
print(ans)
