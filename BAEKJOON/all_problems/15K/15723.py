from collections import deque

edges = [[] for _ in range(26)]
g = [[0]*26 for _ in range(26)]

n = int(input())
for _ in range(n):
    v, _, u = input().split()
    v, u = ord(v)-97, ord(u)-97
    # g[v][u] = 1
    edges[v].append(u)
    # print(v, u)

# BFS
for base_v in range(26):
    q = deque([base_v])
    visited = [False]*26
    visited[base_v] = True
    while q:
        v = q.popleft()
        for u in edges[v]:
            g[base_v][u] = 1
            if not visited[u]:
                visited[u] = True
                q.append(u)
# print(edges)
# print(g)

m = int(input())
for _ in range(m):
    v, _, u = input().split()
    v, u = ord(v)-97, ord(u)-97
    print('T' if g[v][u] == 1 else 'F')