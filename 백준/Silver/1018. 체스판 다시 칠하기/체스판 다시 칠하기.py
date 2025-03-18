n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]
cnt = 64  # 최악의 경우 64칸을 전부 다시 칠해야 함

for i in range(n - 7):  
    for j in range(m - 7):  
        w_start = 0  # 'W'로 시작하는 체스판과의 차이
        b_start = 0  # 'B'로 시작하는 체스판과의 차이

        for y in range(8):
            for x in range(8):
                if (x + y) % 2 == 0:  # 체스판의 짝수 칸
                    if graph[i + y][j + x] != 'W':  
                        w_start += 1
                    if graph[i + y][j + x] != 'B':  
                        b_start += 1
                else:  # 체스판의 홀수 칸
                    if graph[i + y][j + x] != 'B':  
                        w_start += 1
                    if graph[i + y][j + x] != 'W':  
                        b_start += 1

        cnt = min(cnt, w_start, b_start)  # 최소 변경 횟수 갱신

print(cnt)