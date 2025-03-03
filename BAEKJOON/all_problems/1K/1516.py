import sys
input = sys.stdin.readline
from collections import deque

def solve():
    n = int(input())

    pre_cnts = [0]*(n+1)
    times = [0]*(n+1)
    # INF = int(1e8)
    ans = [0]*(n+1)
    g = [[] for _ in range(n+1)]

    for i in range(n):
        ns = list(map(int, input().split()))
        times[i+1] = ns[0]
        for v in ns[1:-1]:
            g[v].append(i+1)
            pre_cnts[i+1] += 1

    q = deque()
    for i in range(1, n+1):
        if(pre_cnts[i] == 0):
            q.append(i)
            ans[i] = times[i]

    while(q):
        v = q.popleft()
        # print("v" ,v)
        for u in g[v]:
            pre_cnts[u] -= 1
            ans[u] = max(ans[u], ans[v]+times[u])
            if(pre_cnts[u] == 0):
                q.append(u)

    print(*ans[1:], sep='\n')

solve()