N, D = map(int, input().split())
ns = list(map(int, input().split()))

limit = int(3e5)+1
cnts = [0]*limit
for n in ns:
    cnts[n] += 1

ans = 0
# th : target_h
for th in range(max(ns), 0, -1):
    if cnts[th] > 0:
        ans += cnts[th]
        cnts[th-1] += cnts[th]
        D -= 1
        if D == 0:
            break

print(ans)