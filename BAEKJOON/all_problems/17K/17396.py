import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N, M = map(int, input().split())
visible = list(map(bool, map(int, input().split())))
# print(visible)

destination = N-1
g = [[] for _ in range(N)]
for _ in range(M):
    a, b, val = map(int, input().split())
    a, b = sorted([a, b])

    if visible[a] or (b != destination and visible[b]): continue
    g[a].append([val, b])
    g[b].append([val, a])

INF = int(1e10)+1
dists = [INF]*N
dists[0] = 0
heap = []
heappush(heap, [0, 0])
visited = [False]*N

while heap:
    d, v = heappop(heap)
    if visited[v]: continue
    visited[v] = True

    for tmp_d, u in g[v]:
        nd = d+tmp_d
        if dists[u] > nd :
            dists[u] = nd
            heappush(heap, [nd, u])

print(dists[destination] if dists[destination] != INF else -1)