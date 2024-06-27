N = int(input())
ns = sorted(list(map(int, input().split())))

ans = 0
pre = ns[0]

for n in ns[1:]:
    ans += (n-pre)
    pre = n

print(ans+ns[-1]-ns[0])