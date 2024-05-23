import sys
input = sys.stdin.readline

def dfs(g, parent, v):
    for u in g[v]:
        if parent[v] != parent[u]:
            union_parent(parent, v, u)
            dfs(g, parent, u)

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = parent[a]
    b = parent[b]

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def solve():
    N, M = map(int, input().split())
    g = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    parent = [i for i in range(N+1)]
    for i in range(1, N+1):
        find_parent(parent, i)
    for i in range(1, N+1):
        dfs(g, parent, i)
    # print(parent)

    ans = 0
    for i in range(2, N+1):
        if parent[1] != find_parent(parent, i):
            union_parent(parent, 1, i)
            ans += 1

    print(ans)

solve()