H, W = map(int, input().split())

tables = [[list(map(int, input().split())) for _ in range(H)] for _ in range(2)]
# print(tables)

dp = [[0]*W for _ in range(H)]
for y in range(W):
    dp[0][y] = (tables[0][0][y]-tables[1][0][y])**2
# print(dp[0])

for x in range(1, H):
    for y in range(W):
        dp[x][y] = dp[x-1][y]
        if y > 0:
            dp[x][y] = min(dp[x][y], dp[x-1][y-1])
        if y < (W-1):
            dp[x][y] = min(dp[x][y], dp[x-1][y+1])

        dp[x][y] += (tables[0][x][y]-tables[1][x][y])**2

print(min(dp[H-1]))