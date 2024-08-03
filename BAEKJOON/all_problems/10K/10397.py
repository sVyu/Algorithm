arr = ['_']+list(input())
N = len(arr)-1
# print(arr, N)

dp = [[0]*3 for _ in range(N+1)]
for i in range(1, N+1):
    if arr[i] not in '0123456789':
        continue

    val = int(arr[i])
    for k in range(3):
        dp[i][(k+val)%3] = dp[i-1][k]
    dp[i][val%3] += 1

# for x in range(1, N+1):
#     print(dp[x])

ans = sum([dp[i][0] for i in range(1, N+1)])
print(ans)