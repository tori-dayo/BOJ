import sys
sys.setrecursionlimit(10**8)
input= sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)] 
result = [[] for _ in range(n+1)]

#n-1개의 줄에 연결된 두 정점이 주어짐
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

#dfs 함수에서, 부모의 값을 result에 저장
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            result[i] = v
            dfs(i)
            
#루트 번호인 1번부터 탐색
dfs(1)

for i in range(2,len(result)):
    print(result[i])