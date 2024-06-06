import sys
input = sys.stdin.readline
from collections import deque

def solve():
    N, M, _ = map(int, input().split())
    g = [[] for _ in range(N+1)]
    INF = int(5e10)

    for _ in range(M):
        u, v, c = map(int, input().split())
        g[v].append([u, c]) # u v 뒤집기
    # print(g)

    q = deque()
    ks = list(map(int, input().split()))
    for k in ks:
        q.append([k, 0])

    dists = [INF]*(N+1)
    while q:
        v, d = q.popleft()
        if dists[v] > d:
            dists[v] = d
            for u, nextd in g[v]:
                q.append([u, d+nextd])
    # print(dists)

    ans_v, ans_dist = -1, -1
    for v in range(1, N+1):
        if ans_dist < dists[v]:
            ans_dist = dists[v]
            ans_v = v

    print(ans_v, ans_dist, sep='\n')

solve()