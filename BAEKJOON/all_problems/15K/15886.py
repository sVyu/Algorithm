N = int(input())
ds = list(input())

pre = 'E'
ans = 0

for d in ds:
    if pre == 'E' and d == 'W':
        ans += 1
    pre = d

print(ans)