n = int(input())

for _ in range(n):
    x = int(input())
    if x <= 3:
        print(1)
        continue
    dp = [0] * (x+2)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1

    for i in range(4,x+1):
        dp[i] = dp[i-3] + dp[i-2]

    print(dp[x])