import sys
input = sys.stdin.readline

# ref : https://codio.tistory.com/entry/%EB%B0%B1%EC%A4%80-9764%EB%B2%88-%EC%84%9C%EB%A1%9C-%EB%8B%A4%EB%A5%B8-%EC%9E%90%EC%97%B0%EC%88%98%EC%9D%98-%ED%95%A9-C

'''
1 -> 1
2 -> 1
3 -> 2  // 1+2, 3
4 -> 2  // 1+3, 4
5 -> 3  // 1+4, 2+3, 5
6 -> 4  // 1+2+3, 2+4, 1+5, 6
'''

def solve():
    mod_val = 100_999

    mx = 2001
    dp = [[0]*mx for _ in range(mx)]
    for y in range(mx):
        dp[0][y] = 1

    for x in range(1, mx):
        for y in range(1, mx):
            dp[x][y] = dp[x][y-1]
            if(y <= x):
                dp[x][y] = (dp[x][y-1] + dp[x-y][y-1]) % mod_val

    t = int(input())
    for _ in range(t):
        n = int(input())
        print(dp[n][n])

if __name__ == "__main__":
    solve()