N = int(input())
ns = list(map(int, input().split()))

ans, now = 1, 1
pre = ns[0]
for n in ns[1:]:
    if pre <= n:
        now += 1
        ans = max(ans, now)
    else:
        now = 1
    pre = n

now = 1
pre = ns[0]
for n in ns[1:]:
    if pre >= n:
        now += 1
        ans = max(ans, now)
    else:
        now = 1
    pre = n

print(ans)