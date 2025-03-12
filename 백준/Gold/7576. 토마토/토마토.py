from collections import deque

m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx,dy = [-1,1,0,0] , [0,0,-1,1]
queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((j,i,1))

def bfs(queue):
    result_time = 0
    while queue:
        x,y,time = queue.popleft()
        for i in range(4):
            ix = x + dx[i]
            iy = y + dy[i]

            if ix <= -1 or ix >= m or iy <= -1 or iy >= n:
                continue

            if graph[iy][ix] == 0:
                graph[iy][ix] = 1
                queue.append((ix,iy,time+1))
                result_time = time
    return result_time

if len(queue) == 0:
    print(-1)
    exit()
cnt = bfs(queue)
for i in graph:
    if 0 in i:
        print(-1)
        exit()
print(cnt)