import sys
input = sys.stdin.readline

def solve():
    n, b = map(int, input().split())
    sums = [0]*(n+1)
    for i in range(1, n+1):
        k = int(input())
        sums[i] = sums[i-1]+k
    # print(sums)

    for _ in range(b):
        t = int(input())
        ti = -1
        lo, hi = 1, n

        while(lo <= hi):
            mid = (lo+hi)//2
            if(sums[mid] <= t):
                lo = mid+1
            else:
                hi = mid-1
                ti = mid

        print(ti)

solve()