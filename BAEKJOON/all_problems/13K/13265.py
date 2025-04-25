import sys
input = sys.stdin.readline
from collections import deque

def solve():
    n, m = map(int, input().split())
    g = [[] for _ in range(n+1)]

    for _ in range(m):
        x, y = map(int, input().split())
        g[x].append(y)
        g[y].append(x)
    # print(g)

    pos = True
    colors = [-1]*(n+1)

    # bv : base_v
    for bv in range(1, n+1): 
        if(colors[bv] != -1): continue
        q = deque({bv})
        curr_color = 0
        colors[bv] = curr_color

        while(q):
            len_q = len(q)
            next_color = (curr_color+1)%2
            for _ in range(len_q):
                v = q.popleft()
                for u in g[v]:
                    if(colors[u] == curr_color):
                        print("impossible")
                        return
                    elif(colors[u] == -1):
                        colors[u] = next_color
                        q.append(u)

            curr_color = next_color

    print("possible")

for _ in range(int(input())):
    solve()