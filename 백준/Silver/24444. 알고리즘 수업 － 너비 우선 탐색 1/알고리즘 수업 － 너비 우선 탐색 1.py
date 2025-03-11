from collections import deque
import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited= [False] * (n+1)
result = [0] * (n+1)

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()

def bfs(v):
    queue = deque([(v)])
    visited[v] = True
    cnt = 1
    result[v] = cnt
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append((i))
                cnt += 1
                result[i] = cnt
                
bfs(r)

for i in range(1,n+1):
    print(result[i])