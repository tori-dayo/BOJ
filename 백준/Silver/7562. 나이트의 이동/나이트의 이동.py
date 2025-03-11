from collections import deque

n = int(input())

chese = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]

def bfs(x,y):
    queue = deque([(x,y,0)])
    graph[y][x] = 0
    
    while queue:
        x,y,time = queue.popleft()

        if x == c and y == d:
            return time
            
        for a,b in chese:
            ix = x + a
            iy = y + b

            if ix <= -1 or ix >= m or iy <= -1 or iy >= m:
                continue
            
            if graph[iy][ix] == 0:
                graph[iy][ix] = 1
                queue.append((ix,iy,time+1))
        
for _ in range(n):
    m = int(input())
    graph = [[0 for _ in range(m)] for _ in range(m)]
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    print(bfs(a,b))