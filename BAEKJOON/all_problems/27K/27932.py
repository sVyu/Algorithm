import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    ns = list(map(int, input().split()))

    if n == 1:
        print(0)
        return

    lo, hi = 0, int(1e9)
    ans = -1
    while lo <= hi:
        mid = (lo+hi)//2

        cnt = 1 if abs(ns[0]-ns[1]) > mid else 0
        for i in range(1, n-1):
            if abs(ns[i]-ns[i-1]) > mid or abs(ns[i]-ns[i+1]) > mid:
                cnt += 1
        cnt += 1 if abs(ns[-2]-ns[-1]) > mid else 0

        if cnt <= k:
            ans = mid
            hi = mid-1
        else:
            lo = mid+1

    print(ans)

solve()