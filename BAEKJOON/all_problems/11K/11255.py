import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        infected = [False]*(n+1)
        edges = [[] for _ in range(n+1)]
        
        for _ in range(m):
            v, u = map(int, input().split())
            edges[v].append(u)
            edges[u].append(v)
    
        infected_vs = list(map(int, input().split()))
        for v in infected_vs:
            infected[v] = True
            for u in edges[v]:
                infected[u] = True

        print(sum([1 if _inf else 0 for _inf in infected ]))

solve()