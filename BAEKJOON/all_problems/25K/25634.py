def solve():
    N = int(input())
    ns = [0]+list(map(int, input().split()))
    bools = [0]+list(map(int, input().split()))
    # print(bools)

    sums = [0]*(N+1)
    for i in range(1, N+1):
        sums[i] = sums[i-1] + bools[i]*ns[i]
    # print(sums)

    dp = [0]*(N+1)
    for i in range(1, N+1):
        dp[i] = max(dp[i-1], sums[i-1]) + ((bools[i]+1)%2)*ns[i]

    ans = 0
    for i in range(1, N+1):
        ans = max(ans, dp[i]+sums[N]-sums[i])
    print(ans)

solve()