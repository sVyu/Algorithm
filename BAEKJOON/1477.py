import sys
input = sys.stdin.readline

def solve():
    n, m, l = map(int, input().split())
    ws = [0] + sorted(list(map(int, input().split())))
    ws.append(l)

    lo, hi = 1, l
    ans = int(1e4)
    while(lo <= hi):
        mid = (lo+hi)//2

        cnt = 0
        for i in range(1, n+2):
            cnt += ((ws[i]-ws[i-1])-1)//mid

        if(cnt <= m):
            ans = mid
            hi = mid-1
        else:
            lo = mid+1

    print(ans)

solve()