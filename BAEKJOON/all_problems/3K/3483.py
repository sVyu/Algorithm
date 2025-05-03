import sys
input = sys.stdin.readline

def solve():
    e, f = map(int, input().split())
    n = int(input())

    k = f-e
    INF = int(1e9)
    dp = [INF]*(k+1)
    dp[0] = 0

    for _ in range(n):
        p, w = map(int, input().split())
        for y in range(w, k+1):
            dp[y] = min(dp[y], dp[y-w]+p)

    if dp[k] != INF:
        print(f"The minimum amount of money in the piggy-bank is {dp[k]}.")
    else:
        print("This is impossible.")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()