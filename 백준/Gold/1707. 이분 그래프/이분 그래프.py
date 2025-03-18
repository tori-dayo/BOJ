import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v, color):
    visited[v] = color  

    for i in graph[v]:
        if visited[i] == -1:  
            if not dfs(i, 1 - color):  
                return False
        elif visited[i] == visited[v]:  
            return False
    return True

t = int(input())  # 테스트 케이스 개수

for _ in range(t):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [-1] * (v + 1)  

    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    is_bipartite = True
    
    for i in range(1, v + 1):
        if visited[i] == -1:  
            if not dfs(i, 0):
                is_bipartite = False
                break

    if is_bipartite == True:
        print('YES')
    else:
        print('NO')