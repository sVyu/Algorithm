s = input().rstrip()

ans = s[0]
pre = s[0]
for c in s[1:]:
    if pre == c: continue
    pre = c
    ans += c

print(ans)