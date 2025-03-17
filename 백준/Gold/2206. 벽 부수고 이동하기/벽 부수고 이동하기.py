from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[[False]*2 for _ in range(m)] for _ in range(n)]  # visited[y][x][chance]로 수정

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y, 0, 1)])  # (x, y, cnt, chance)
    visited[y][x][1] = True  # 처음 방문한 곳은 chance = 1로 설정

    while queue:
        a, b, cnt, chance = queue.popleft()

        if a == m - 1 and b == n - 1:  # 끝점에 도달하면
            print(cnt + 1)
            return

        for i in range(4):
            ix = a + dx[i]
            iy = b + dy[i]

            if ix < 0 or ix >= m or iy < 0 or iy >= n:
                continue

            # 벽을 부수지 않고 가는 경우
            if graph[iy][ix] == 0 and not visited[iy][ix][chance]:
                visited[iy][ix][chance] = True
                queue.append((ix, iy, cnt + 1, chance))

            # 벽을 부수고 가는 경우
            if graph[iy][ix] == 1 and chance > 0 and not visited[iy][ix][chance - 1]:
                visited[iy][ix][chance - 1] = True
                queue.append((ix, iy, cnt + 1, chance - 1))
    print(-1)

bfs(0, 0)