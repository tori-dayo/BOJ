from collections import deque

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
max_int = -1
dx,dy = [-1,1,0,0],[0,0,-1,1]
result = []

for i in graph:
    if max_int < max(i):
        max_int = max(i)

def bfs(x,y,num):
    queue = deque([(x,y)])
    visited[y][x] = True

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            ix = x + dx[i]
            iy = y + dy[i]

            if ix <= -1 or ix >= n or iy <= -1 or iy >= n:
                continue
            if not visited[iy][ix] and graph[iy][ix] > num:
                visited[iy][ix] = True
                queue.append((ix,iy))

for i in range(0,max_int):
    cnt = 0
    visited = [[False]*n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            if not visited[a][b] and graph[a][b] > i:
                bfs(b,a,i)
                cnt += 1
    result.append(cnt)
print(max(result))