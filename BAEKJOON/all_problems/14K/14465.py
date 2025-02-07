import sys
input = sys.stdin.readline

def solve():
    n, k, b = map(int, input().split())
    broken = [False]*(n+1)

    for _ in range(b):
        i = int(input())
        broken[i] = True

    sums = [0]*(n+1)
    for i in range(1, n+1):
        sums[i] = sums[i-1]+(1 if not broken[i] else 0)

    ans = n
    for i in range(k, n+1):
        ans = min(ans, k-(sums[i]-sums[i-k]))

    print(ans)

solve()