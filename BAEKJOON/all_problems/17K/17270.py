import sys
input = sys.stdin.readline

def solve():
    v, m = map(int, input().split())

    INF = int(1e8)
    dists = [[INF]*(v+1) for _ in range(v+1)]
    for x in range(v+1): dists[x][x] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        dists[a][b] = min(dists[a][b], c)
        dists[b][a] = min(dists[b][a], c)
    j, s = map(int, input().split())

    # floyd-warshall
    for k in range(v+1):
        for a in range(v+1):
            for b in range(v+1):
                dists[a][b] = min(dists[a][b], dists[a][k]+dists[k][b])

    # for x in range(1, v+1):
    #     print(dists[x][1:])

    ans_v = -1
    min_tot_dist = INF
    min_tot_dist_from_j = INF

    # 조건 2 우선 수행
    for nv in range(1, v+1):
        if nv in [j, s]: continue
        if(min_tot_dist > (dists[j][nv]+dists[s][nv])):
            min_tot_dist = dists[j][nv]+dists[s][nv]
    # print(min_tot_dist)

    # nv: new_v
    for nv in range(1, v+1):
        if nv in [j, s]: continue

        tot_dist = dists[j][nv]+dists[s][nv]
        if(min_tot_dist < tot_dist): continue
        if(dists[j][nv] > dists[s][nv]): continue

        if(min_tot_dist_from_j > dists[j][nv]):
            min_tot_dist_from_j = dists[j][nv]
            ans_v = nv

    print(ans_v)

solve()