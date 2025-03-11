from collections import deque

n,m = map(int,input().split())
graph = [i for i in range(101)]
visited = [False] * 101
move = [1,2,3,4,5,6]

for _ in range(n+m):
    x,y = map(int,input().split())
    graph[x] = y

def bfs(v):
    queue = deque([(v,0)])
    visited[graph[v]] = True
    
    while queue:
        x,time = queue.popleft()
        
        if graph[x] == 100:
            print(time)
            exit()
            
        for i in move:
            ix = i + x

            if ix > 100:
                continue
                
            if not visited[ix]:
                queue.append((graph[ix],time+1))
                visited[graph[ix]] = True

bfs(1)