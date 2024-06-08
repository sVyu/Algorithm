n = int(input())
ns = list(map(int, input().split()))

tot = sum(ns)
ans = n*int(1e3)

now = 0
for n in ns[:n-1]:
    now += n
    tot -= n
    ans = min(ans, abs(now-tot))

print(ans)