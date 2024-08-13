import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a) #
    b = find(parent, b) #
    if a > b:   parent[a] = b
    else:       parent[b] = a

def solve():
    N, P = map(int, input().split())
    cs = [0]+[int(input()) for _ in range(N)]

    heap = []
    for _ in range(P):
        v, u, cost = map(int, input().split())
        heappush(heap, [2*cost+cs[v]+cs[u], v, u]) #
    # print(heap)

    parent = [i for i in range(N+1)]
    ans = 0

    for _ in range(N-1):
        while heap:
            cost, v, u = heappop(heap)
            if find(parent, v) != find(parent, u):
                union(parent, v, u)
                ans += cost
                break

    ans += min(cs[1:])
    print(ans)

solve()