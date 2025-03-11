import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

m,n,k = map(int,input().split())

graph = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
score = []
for _ in range(k):
    a,b,c,d = map(int,input().split())

    for i in range(b,d):
        for j in range(a,c):
            graph[j][i] = 1

def dfs(x,y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    cnt = 1
    if not visited[y][x] and graph[y][x] == 0:
        visited[y][x] = True
        cnt += dfs(x-1,y)
        cnt += dfs(x+1,y)
        cnt += dfs(x,y-1)
        cnt += dfs(x,y+1)
        return cnt
    return False

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 0:
            score.append(dfs(j,i))
score.sort()
print(len(score))
print(*score)