# 다익스트라 역추적
# 메모리 초과

import sys
input = sys.stdin.readline
from collections import deque

def dist_with_dijkstra(g, s, e, dists):
    q = deque([[s, 0]])
    dists[s] = 0

    while q:
        v, d = q.popleft()
        for u, nd in g[v]:
            tot_d = d+nd
            if dists[u] > tot_d:
                dists[u] = tot_d
                q.append([u, tot_d])
    return dists

def solve():
    N, M = map(int, input().split())
    while N and M:
        S, D = map(int, input().split())

        g = [[] for _ in range(N)]
        rev_g = [[] for _ in range(N)]
        for _ in range(M):
            U, V, P = map(int, input().split())
            g[U].append([V, P])
            rev_g[V].append([U, P])

        INF = int(5e5)+1
        min_dists = dist_with_dijkstra(g, S, D, [INF]*N)
        # print(min_dists)

        # 역추적
        shortest_loads = set()
        q = deque([[D, min_dists[D]]])
        while q:
            v, d = q.popleft()
            for pre_v, pre_d in rev_g[v]:
                pre_tot_d = d-pre_d
                if min_dists[pre_v] == pre_tot_d:
                    shortest_loads.add(tuple([pre_v, v]))
                    if pre_v != S:
                        q.append([pre_v, pre_tot_d])
        # print("shortest_loads", shortest_loads)

        # 최단 거리들을 제외한 새로운 그래프
        new_g = [[] for _ in range(N)]
        for v in range(N):
            for dist_info in g[v]:
                if tuple([v, dist_info[0]]) not in shortest_loads:
                    new_g[v].append(dist_info)
        # print(new_g)

        min_dists = dist_with_dijkstra(new_g, S, D, [INF]*N)
        print(min_dists[D] if min_dists[D] != INF else -1)

        # 다음 graph
        N, M = map(int, input().split())

solve()