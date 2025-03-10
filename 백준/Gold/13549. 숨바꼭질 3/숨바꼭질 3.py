from collections import deque
n,k = map(int,input().split())
visited = [False] * 100001

def bfs(v):
    queue = deque([(v,0)])
    visited[v] = True

    while queue:
        x , time = queue.popleft()
        if x == k:
            print(time)
            exit()
        if (2*x) <= 100000 and not visited[2*x]:
            visited[2*x] = True
            queue.append((2*x,time))
        if (x-1) >= 0 and not visited[x-1]:
            visited[x-1] = True
            queue.append((x-1,time+1))
        if (x+1) <= 100000 and not visited[x+1]:
            visited[x+1] = True
            queue.append((x+1,time+1))
if n == k:
    print(0)
else:
    bfs(n)