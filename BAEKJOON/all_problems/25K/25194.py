import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    zs = list(map(int, input().split()))
    zs = [(z%7) for z in zs]

    mx = 7015
    dp = [0]*mx

    for i in range(n):
        z = zs[i]
        if(z == 0): continue
        for j in range(7007, z-1, -1):
            dp[j] += dp[j-z]
        dp[z] += 1

    for i in range(4, mx, 7):
        if(dp[i] >= 1):
            print("YES")
            return

    print("NO")

solve()