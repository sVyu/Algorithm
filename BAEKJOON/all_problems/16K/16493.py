N, M = map(int, input().split())

dp = [0]*(N+1)
for _ in range(M):
    day, page = map(int, input().split())
    for i in range(N, day-1, -1):
        dp[i] = max(dp[i], dp[i-day]+page)

print(dp[N])