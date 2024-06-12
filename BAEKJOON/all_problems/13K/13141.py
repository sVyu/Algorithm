import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    INF = int(2e7)
    fw = [[INF]*(N+1) for _ in range(N+1)]      # floyd-warshall
    longest_g = [[0]*(N+1) for _ in range(N+1)] # 정점들 사이 최대 거리 (중간에 다른 정점 방문 X)

    # edges
    for _ in range(M):
        S, E, L = map(int, input().split())
        L *= 10
        for v, u in [[S, E], [E, S]]:
            fw[v][u] = min(fw[v][u], L)
            longest_g[v][u] = max(longest_g[v][u], L)

    # floyd-warshall init
    for k in range(N+1):
        fw[k][k] = 0
    for k in range(1, N+1):
        for a in range(1, N+1):
            for b in range(1, N+1):
                fw[a][b] = min(fw[a][b], fw[a][k]+fw[k][b])

    burn_end_time = [[INF]*(N+1) for _ in range(N+1)]

    # start v : 시작점
    for sv in range(1, N+1):
        for ev in range(1, N+1):
            max_burn_time = fw[sv][ev]
            for midv in range(1, N+1):
                if fw[sv][ev] < fw[sv][midv] : continue
                last_d = max(0, longest_g[midv][ev]-(fw[sv][ev]-fw[sv][midv]))
                max_burn_time = max(max_burn_time, fw[sv][ev]+(last_d//2))
            burn_end_time[sv][ev] = min(burn_end_time[sv][ev], max_burn_time)

    # for x in range(N+1):
    #     print(burn_end_time[x])
    print(min(max(burn_end_time[x][1:]) for x in range(1, N+1))/10)

solve()