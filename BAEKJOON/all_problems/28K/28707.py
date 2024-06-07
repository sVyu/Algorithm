import sys
input = sys.stdin.readline
from collections import deque

def solve():
    N = int(input())
    ns = tuple(map(int, input().split()))
    backuped_ns = ns[:]

    M = int(input())
    INF = int(1e5) #
    dists = [[INF]*(N+1) for _ in range(N+1)]

    ms = [list(map(int, input().split())) for _ in range(M)]
    ms = [[ms[i][0]-1, ms[i][1]-1, ms[i][2]] for i in range(M)]

    for i in range(M):
        l, r, c = ms[i]
        dists[l][r] = min(dists[l][r], c)
        dists[r][l] = min(dists[r][l], c)
    # print(dists)

    dist_dict = dict()
    dist_dict[ns] = 0
    q = deque([ns])

    while q:
        ns = q.popleft()
        for m in ms:
            l, r, c = m
            new_ns = list(ns[:])
            new_ns[l], new_ns[r] = new_ns[r], new_ns[l]
            new_ns = tuple(new_ns)
            nd = dist_dict[ns]+c

            need_update = False
            if new_ns in dist_dict:
                if dist_dict[new_ns] > nd and dist_dict[new_ns] > dist_dict[backuped_ns]:
                    need_update = True
            else:
                need_update = True

            if need_update:
                dist_dict[new_ns] = nd
                q.append(new_ns)

    target = tuple(sorted(backuped_ns))
    print(dist_dict[target] if target in dist_dict else -1)

solve()