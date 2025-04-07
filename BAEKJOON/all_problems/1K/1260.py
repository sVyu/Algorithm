import sys
input = sys.stdin.readline
from collections import deque

def dfs(g, v, parent, dfs_route, visited):
    dfs_route.append(v)
    visited[v] = True
    for u in g[v]:
        # if(u == parent): continue
        if(not visited[u]):
            dfs(g, u, v, dfs_route, visited)

def solve():
    n, m, v = map(int, input().split())
    g = [[] for _ in range(n+1)]

    for _ in range(m):
        s, e = map(int, input().split())
        g[s].append(e)
        g[e].append(s)

    # 정점 번호가 작은 것부터 방문
    for i in range(n+1):
        g[i].sort()

    dfs_route = []
    visited = [False]*(n+1)
    visited[v] = True
    dfs(g, v, -1, dfs_route, visited)
    print(*dfs_route)

    bfs_route = []
    q = deque({v})
    # print(q)
    visited = [False]*(n+1)
    visited[v] = True

    while(q):
        v = q.popleft()
        bfs_route.append(v)
        for u in g[v]:
            if(not visited[u]):
                visited[u] = True
                q.append(u)
    print(*bfs_route)

solve()