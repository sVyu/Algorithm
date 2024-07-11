import sys
input = sys.stdin.readline

V, N = map(int, input().split())
vals = [int(input()) for _ in range(V)]
dp = [[0]*(N+1) for _ in range(V+1)]
for x in range(V+1):
    dp[x][0] = 1

for x in range(V):
    for y in range(1, N+1):
        dp[x][y] = dp[x-1][y] + (dp[x][y-vals[x]] if y >= vals[x] else 0)

# for x in range(V):
#     print(dp[x])

print(dp[V-1][N])