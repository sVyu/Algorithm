import sys
input = sys.stdin.readline
from collections import deque

def solve():
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n-1):
        p, c = map(int, input().split())
        g[p].append(c)
        g[c].append(p)

    costs = [list(map(int, input().split())) for _ in range(n)]
    tot_costs = []
    # print(costs)

    # wb (white, black)
    for wb_idx in [0, 1]:
        q = deque([[0, wb_idx]])
        visited = [False]*n
        visited[0] = True
        tot_cost = 0
        while q:
            v, wb_idx = q.popleft()
            tot_cost += costs[v][wb_idx]
            for u in g[v]:
                if not visited[u]:
                    visited[u] = True
                    q.append([u, (wb_idx+1)%2])
        tot_costs.append(tot_cost)

    print(min(tot_costs))

solve()