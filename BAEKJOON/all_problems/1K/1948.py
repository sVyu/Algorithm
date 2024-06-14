import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
g = [[] for _ in range(n+1)]
rev_g = [[] for _ in range(n+1)]

pre_edges_cnt = [0]*(n+1)
for _ in range(m):
    s, e, t = map(int, input().split())
    g[s].append([e, t])
    pre_edges_cnt[e] += 1
    rev_g[e].append([s, t])

s, e = map(int, input().split())
ans_t = -1

tot_ts = [set() for _ in range(n+1)]
tot_ts[s].add(0)

q = deque([[s, 0]])
while q:
    v, t = q.popleft()
    for nv, nt in g[v]:
        tot_ts[nv].add(t+nt)
        pre_edges_cnt[nv] -= 1
        if pre_edges_cnt[nv] == 0:
            q.extend([[nv, max(tot_ts[nv])]])
# print(tot_ts)

ans_t = max(tot_ts[e])
no_rest_road = set()
q = deque([[e, ans_t]])
while q:
    v, tot_t = q.popleft()
    for pre_v, pre_t in rev_g[v]:
        pre_tot_t = tot_t-pre_t
        passed_road = tuple([pre_v, v])
        if pre_tot_t in tot_ts[pre_v] and passed_road not in no_rest_road:
            no_rest_road.add(passed_road)
            q.append([pre_v, pre_tot_t])

print(ans_t)
print(len(no_rest_road))

'''
9
10
1 2 1
1 3 1
2 4 1
3 5 1
4 6 1
5 6 1
6 7 1
6 8 1
7 9 1
8 9 1
1 9
'''