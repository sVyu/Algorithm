import sys
input = sys.stdin.readline

N = int(input())
ns = [0]+list(map(int, input().split()))
times_by_level = [[] for _ in range(6)]

for _ in range(N):
    lv, time = map(int, input().split())
    times_by_level[lv].append(time)

for lv in range(6):
    times_by_level[lv].sort()

ans = 0
for lv in range(1, 6):
    pre = 0
    for idx in range(ns[lv]):
        val = times_by_level[lv][idx]
        if idx != 0:
            ans += val-pre
        ans += val   
        pre = val

print(ans+240)