import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def dfs(g, v, finished):
    global sccs, stack, vo, vos
    vo += 1
    vos[v] = vo
    stack.append(v)

    parent = vos[v]
    for u in g[v]:
        if(not vos[u]):         parent = min(parent, dfs(g, u, finished))
        elif(not finished[u]):  parent = min(parent, vos[u]) # visited but not finished -> cycle root

    if(parent == vos[v]):
        scc = []
        t = -1

        while(t != v):
            t = stack.pop()
            scc.append(t)
            finished[t] = True

        sccs.append(scc)

    return parent

def solve():
    n, e = map(int, input().split())
    g = [[] for _ in range(n+1)]

    for _ in range(e):
        a, b = map(int, input().split())
        g[a].append(b)
    # print(g)

    global sccs, stack, vo, vos
    sccs = []
    stack = []
    vo = 0
    vos = [0]*(n+1) # visited_order, 방문 순서
    finished = [False]*(n+1)

    for v in range(1, n+1):
        if(vos[v]): continue
        dfs(g, v, finished)
    # print(sccs)

    len_sccs = len(sccs)
    for i in range(len_sccs):
        sccs[i].sort()

    sccs = sorted(sccs, key=lambda x:(x[0]))
    # print(sccs)

    print(len_sccs)
    for scc in sccs:
        print(*scc, end=' -1\n')

solve()

# ==========================
# import sys
# input = sys.stdin.readline

# def dfs(scc, g, v, visited, finished):
#     visited[v] = True

#     global stack
#     stack.append(v)

#     parent = v
#     for u in g[v]:
#         if(not visited[u]):     parent = min(parent, dfs(scc, g, u, visited, finished))
#         elif(not finished[u]):  parent = min(parent, u) # visited but not finished -> cycle root

#     if(parent == v):
#         print("(before) stack", stack, v)
#         scc.append(stack[:])
#         for u in stack:
#             finished[u] = True
#         stack = []
#         print("(after) stack", stack)

#     return parent

# def solve():
#     n, e = map(int, input().split())
#     g = [[] for _ in range(n+1)]

#     for _ in range(e):
#         a, b = map(int, input().split())
#         g[a].append(b)
#     # print(g)

#     scc = []
#     d = []
#     finished = [False]*(n+1)

#     for v in range(1, n+1):
#         if(visited[v]): continue
#         dfs(scc, g, v, visited, finished)

#     print(scc)

# solve()