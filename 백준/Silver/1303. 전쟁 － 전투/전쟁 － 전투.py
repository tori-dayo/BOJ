import sys
input = sys.stdin.readline

#가로N 세로M
n,m = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]

own_power = 0
enermy_power = 0

def w_dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    size = 1
    if not visited[y][x] and graph[y][x] == 'W':
        visited[y][x] = True
        size += w_dfs(x-1,y)
        size += w_dfs(x+1,y)
        size += w_dfs(x,y-1)
        size += w_dfs(x,y+1)

        return size
    return False

def b_dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    size = 1    
    if not visited[y][x] and graph[y][x] == 'B':
        visited[y][x] = True
        size += b_dfs(x-1,y)
        size += b_dfs(x+1,y)
        size += b_dfs(x,y-1)
        size += b_dfs(x,y+1)

        return size
    return False

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            if graph[i][j] == 'W':
                own_power += w_dfs(j,i) ** 2
            elif graph[i][j] == 'B':
                enermy_power += b_dfs(j,i) ** 2
print(f"{own_power} {enermy_power}")