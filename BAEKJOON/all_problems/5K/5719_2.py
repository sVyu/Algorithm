# 다익스트라 역추적
# 개선 버전 → AC
# 다시 생각해보니 역추적을 하지 않고도 가능하다..!

import sys
input = sys.stdin.readline
from collections import deque

def dist_with_dijkstra(g, s, dists):
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
    while N > 0 and M > 0 :
        S, D = map(int, input().split())

        g = [set() for _ in range(N)]
        rev_g = [[] for _ in range(N)]
        for _ in range(M):
            U, V, P = map(int, input().split())
            g[U].add(tuple([V, P]))
            rev_g[V].append([U, P])

        # INF 정의 및 다익스트라
        INF = int(5e5)+1
        min_dists = dist_with_dijkstra(g, S, [INF]*N)
        # print(min_dists)

        # 역추적 및 최단 거리 경로 제외
        q = deque([[D, min_dists[D]]])
        while q:
            v, tot_d = q.popleft()
            for pre_v, pre_d in rev_g[v]:
                pre_tot_d = tot_d-pre_d
                if min_dists[pre_v] == pre_tot_d:
                    target_road = tuple([v, pre_d])
                    if target_road in g[pre_v]:
                        g[pre_v].remove(target_road)
                        if pre_v != S:
                            q.append([pre_v, pre_tot_d])

        # 2번째 다익스트라
        min_dists = dist_with_dijkstra(g, S, [INF]*N)
        print(min_dists[D] if min_dists[D] != INF else -1)

        # 다음 graph
        N, M = map(int, input().split())

solve()