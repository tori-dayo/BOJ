import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n,m = map(int,input().split())
visited = [False for _ in range(n)]
graph = [[] for _ in range(n)]
result = 0
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v,cnt):
    global result
    visited[v] = True
    if cnt == 5:
        result = 1
        return True
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i,cnt + 1)
    visited[v] = False
    return False

for i in range(n):
    if dfs(i,1):
        break
    
print(result)