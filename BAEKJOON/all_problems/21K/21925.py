import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    zs = list(map(int, input().split()))

    is_palindrome = [[False]*n for _ in range(n)]
    for base in range(n):
        l, r = base, base+1
        while(l>=0 and r<n):
            if(zs[l] == zs[r]):
                is_palindrome[l][r] = True
                l -= 1
                r += 1
            else: break

    # for x in range(n):
    #     print(is_palindrome[x])

    dp = [0]*n
    for r in range(1, n, 2):
        dp[r] = 0
        for l in range(r-1, -1, -2):
            if(l == 0):
                dp[r] = max(dp[r], 1 if is_palindrome[l][r] else 0)
            elif(dp[l-1] and is_palindrome[l][r]):
                dp[r] = max(dp[r], 1 + dp[l-1])

    print(dp[n-1] if dp[n-1] else -1)

solve()