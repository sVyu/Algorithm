import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    INF = int(1e7)
    dp = [[INF]*(m+1) for _ in range(n+1)]
    dp[0] = [0]*(m+1)

    for x in range(1, n+1):
        zs = [0] + list(map(int, input().split()))
        for y in range(1, m+1):
            for z in range(1, m+1):
                if(y==z): continue
                dp[x][y] = min(dp[x][y], dp[x-1][z])
            dp[x][y] += zs[y]

    print(min(dp[x][1:]))

solve()