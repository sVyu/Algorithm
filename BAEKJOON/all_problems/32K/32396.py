import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    zs = list(map(int, input().split()))

    i = 1
    ans = 0
    while(i < n):
        if(abs(zs[i-1]-zs[i]) < m):
            i += 2
            ans += 1
            continue
        i += 1

    print(ans)

solve()