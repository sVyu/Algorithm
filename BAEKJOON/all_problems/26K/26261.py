import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def solve():
    n, x, k = map(int, input().split())
    zs = [1]+list(map(int, input().split()))

    mx = int(2e6)
    dp = [mx]*(n+1)
    dp[0] = 0

    # element : [dp_val, index]
    heap = []
    heappush(heap, [0, 0])

    zero_cnt = 0
    for i in range(1, n+1):
        if(zs[i] == 1):
            zero_cnt = 0
        else:
            zero_cnt += 1

        while(heap and heap[0][1] < (i-x)):
            heappop(heap)
        if(not heap):
            print(-1)
            return

        min_val = heap[0][0]+1
        dp[i] = min_val

        if(zero_cnt >= k and heap[0][1] <= (i-k)):
            heappush(heap, [min_val, i])

    print(dp[n])

solve()