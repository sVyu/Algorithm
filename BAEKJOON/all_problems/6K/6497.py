import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def fp(parent, x):
    if(parent[x] != x):
        parent[x] = fp(parent, parent[x])
    return parent[x]

def up(parent, a, b):
    pa = fp(parent, a)
    pb = fp(parent, b)

    if(pa > pb):    parent[pa] = pb
    else:           parent[pb] = pa

def solve():
    m, n = map(int, input().split())

    while(m >= 1):
        heap = []
        parent = [i for i in range(m+1)]
        tot_cost, needed_cost = 0, 0

        for _ in range(n):
            x, y, z = map(int, input().split())
            heappush(heap, [z, x, y])
            tot_cost += z

        while(heap):
            z, x, y = heappop(heap)
            if(fp(parent, x) != fp(parent, y)):
                up(parent, x, y)
                needed_cost += z

        print(tot_cost - needed_cost)
        m, n = map(int, input().split())

solve()