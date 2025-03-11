from collections import deque
import sys

input = sys.stdin.readline

n,m,r = map(int,input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = [0] * n
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort(reverse = True)

def bfs(v):
    queue = deque([(v)])
    visited[v] = True
    cnt = 1
    result[v-1] = cnt
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                queue.append((i))
                result[i-1] = cnt
bfs(r)

for i in range(n):
    print(result[i])