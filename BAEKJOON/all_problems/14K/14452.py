import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def solve() -> int:
    n, tmax = map(int, input().split())
    zs = [int(input()) for _ in range(n)]

    lo, hi = 1, n
    ans = n
    while(lo <= hi):
        mid = (lo+hi)//2

        i = 0
        heap = []
        for _ in range(0, mid):
            heappush(heap, zs[i])
            i += 1

        for t in range(1, tmax+1):
            while(heap and t == heap[0]):
                heappop(heap)
                if(i<n):
                    heappush(heap, t+zs[i])
                    i += 1

        # print(heap)
        if(i <= n and len(heap) == 0):
            ans = mid
            hi = mid-1
        else:
            lo = mid+1

    print(ans)

solve()