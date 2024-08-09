# 첫 최대 유량 문제

from collections import deque

INF = int(1e6)
# A~Z : 26 // A:65, a:97
size = 26+32

N = int(input())
C = [[0]*size for _ in range(size)]     # Capacity  용량
F = [[0]*size for _ in range(size)]     # Flow      유량
D = [[] for _ in range(size)]

for _ in range(N):
    v, u, cap = input().split()
    v = ord(v)-65
    u = ord(u)-65
    cap = int(cap)

    for curr, next in [[v, u], [u, v]]:
    # for curr, next in [[v, u]]:
        D[curr].append(next)
        C[curr][next] += cap

ans = 0
start, end = 0, 25

while True:
    pre = [-1]*size
    q = deque([start])
    while q:
        curr = q.popleft()
        for next in D[curr]:
            if F[curr][next] < C[curr][next] and pre[next] == -1:
                pre[next] = curr
                q.append(next)
                if next == end: break

    if pre[end] == -1: break
    flow = INF

    v = end
    while v != start:
        flow = min(flow, C[pre[v]][v]-F[pre[v]][v])
        v = pre[v]

    v = end
    while v != start:
        F[pre[v]][v] += flow
        F[v][pre[v]] -= flow
        v = pre[v]

    ans += flow

print(ans)