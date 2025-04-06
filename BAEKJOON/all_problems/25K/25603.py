import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def solve():
    n, k = map(int, input().split())
    zs = list(map(int, input().split()))

    heap = []
    ans = -1
    for i in range(k):
        heappush(heap, [zs[i], i])
        ans = heap[0][0]

    for i in range(k, n):
        while(heap and heap[0][1] <= (i-k)):
            heappop(heap)
        heappush(heap, [zs[i], i])
        ans = max(ans, heap[0][0])

    print(ans)

solve()