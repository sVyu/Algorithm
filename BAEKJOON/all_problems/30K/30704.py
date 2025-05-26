import sys
input = sys.stdin.readline

def solve():
    mx = int(1e9)

    ans = [[1, 4]]
    for x in range(1, 100000):
        n = x**2+1
        if(n > mx): break
        ans.append([n, 4*x+2])

        n = x**2+x+1
        if(n > mx): break
        ans.append([n, 4*x+4])
    # print(ans[-1])
    len_ans = len(ans)

    t = int(input())
    for _ in range(t):
        n = int(input())
        ti = -1

        lo, hi = 0, len_ans-1
        while(lo <= hi):
            mid = (lo+hi)//2
            if(ans[mid][0] <= n):
                ti = mid
                lo = mid+1
            else:
                hi = mid-1

        print(ans[ti][1])

solve()