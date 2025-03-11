n = int(input())
graph = [list(map(int,input())) for _ in range(n)]
visited = [[False] * (n) for _ in range(n)]
score = []

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return 0
    if visited[x][y] or graph[x][y] == 0:
        return 0
    visited[x][y] = True
    size = 1
    
    size += dfs(x-1,y)
    size += dfs(x+1,y)
    size += dfs(x,y-1)
    size += dfs(x,y+1)
    
    return size

for i in range(n):
    for j in range(n):
        if visited[i][j] == False and graph[i][j] == 1:
            result = dfs(i,j)
            score.append(result)

score.sort()

print(len(score))
for i in score:
    print(i)