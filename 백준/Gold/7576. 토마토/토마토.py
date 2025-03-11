from collections import deque
m,n = map(int,input().split())
graph = [(list(map(int,input().split()))) for _ in range(n)]

dx , dy = [-1,1,0,0] , [0,0,-1,1]

# 큐를 생성한다.
queue = deque()

# 만약 1인 경우, queue에 추가한다.
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((j,i,0))

# 큐를 입력받아, 해당 queue를 돌리면 된다.
def bfs(queue):
    max_time = 0
    while queue:
        x,y,time = queue.popleft()

        for i in range(4):
            ix = x + dx[i]
            iy = y + dy[i]

            if ix <= -1 or ix >= m or iy <= -1 or iy >= n:
                continue
                
            if graph[iy][ix] == 0 :
                queue.append((ix,iy,time+1))
                graph[iy][ix] = 1
                max_time = max(max_time,time+1)
    return max_time

if len(queue) == 0:
    print(-1)
    exit()
count = bfs(queue)
for i in graph:
    if 0 in i:
        print(-1)
        exit()
print(count)