# ref : https://lighter.tistory.com/339

import sys
input = sys.stdin.readline

def solve():
    mx = int(1e6)
    # mx = int(1e5)
    dp = [[0]*7 for _ in range(mx+1)]

    mod = int(1e9)+7
    dp[1] = [1, 1, 1, 1, 1, 1, 1]
    dp[2] = [1, 1, 1, 2, 2, 2, 3]

    for x in range(3, mx+1):
        dp[x][0] = dp[x-1][0] % mod
        dp[x][1] = dp[x-1][1] % mod
        dp[x][2] = dp[x-1][2] % mod
        dp[x][3] = (dp[x-2][3]*dp[x-1][3] + dp[x-1][3]*dp[x-1][3]) % mod
        dp[x][4] = (dp[x-2][4]*dp[x-1][4] + dp[x-1][4]*dp[x-2][4]) % mod
        dp[x][5] = (dp[x-2][5]*dp[x-1][5] + dp[x-1][5]*dp[x-1][5]) % mod
        dp[x][6] = (dp[x-2][6]*dp[x-1][6] + dp[x-1][6]*dp[x-1][6] + dp[x-1][6]*dp[x-2][6]) % mod

    t = int(input())
    for _ in range(t):
        h, _ = map(int, input().split())
        bv = input().rstrip() # balance_val

        if(bv == "-1"):            print(dp[h][0])
        elif(bv == "0"):           print(dp[h][1])
        elif(bv == "1"):           print(dp[h][2])
        elif(bv == "-1 0"):        print(dp[h][3])
        elif(bv == "-1 1"):        print(dp[h][4])
        elif(bv == "0 1"):         print(dp[h][5])
        elif(bv == "-1 0 1"):      print(dp[h][6])

solve()