n = int(input())
t_array = [0]
p_array = [0]
result = 0


def dfs(v, cost):
    global result

    if v > n:
        result = max(result, cost)
        return

    if v + t_array[v] <= n + 1:
        dfs(v + t_array[v], cost + p_array[v])

    dfs(v + 1, cost)


for _ in range(n):
    t, p = map(int, input().split())
    t_array.append(t)
    p_array.append(p)

dfs(1, 0)
print(result)