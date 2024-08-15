import sys
input = sys.stdin.readline
from heapq import heapify, heappush, heappop

N = int(input())
heap = list(map(int, input().split()))
heapify(heap)

for _ in range(N-1):
    for n in list(map(int, input().split())):
        heappush(heap, n)
    for _ in range(N):
        heappop(heap)

print(heappop(heap))