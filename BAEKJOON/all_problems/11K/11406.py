import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
start, end = 0, N+M+1
size = end-start+1

C = [[0]*size for _ in range(size)]
F = [[0]*size for _ in range(size)]
g = [[] for _ in range(size)]

As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

# network initialization
for i in range(N):
    v = 1+i
    C[start][v] = As[i]
    g[start].append(v)
    g[v].append(start)

for i in range(M):
    v = 1+N+i
    C[v][end] = Bs[i]
    g[v].append(end)
    g[end].append(v)
# print(C, g)

books = [list(map(int, input().split())) for _ in range(M)]
for m in range(M):
    for n in range(N):
        v1, v2 = 1+n, 1+N+m
        C[v1][v2] = books[m][n]
        g[v1].append(v2)
        g[v2].append(v1)
# print(C, g)

ans = 0
INF = int(1e3)

while True:
    pre = [-1]*size
    q = deque([start])
    while q:
        curr = q.popleft()
        for next in g[curr]:
            if F[curr][next] < C[curr][next] and pre[next] == -1:
                pre[next] = curr
                q.append(next)          # order
                if next == end: break

    if pre[end] == -1: break
    flow = INF

    # find (min) flow val
    v = end
    # btr_arr = [end]
    while v != start:
        flow = min(flow, C[pre[v]][v]-F[pre[v]][v])
        v = pre[v]
        # btr_arr.append(v)
    # print("btr_arr", *btr_arr[::-1])

    # calculate with flow val
    v = end
    while v != start:
        F[pre[v]][v] += flow
        F[v][pre[v]] -= flow # core logic
        v = pre[v]

    ans += flow

print(ans)
