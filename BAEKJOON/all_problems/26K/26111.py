import sys
input = sys.stdin.readline

s = list(input().rstrip())

ans = 0
lv = -1
pre = ''
for i in range(len(s)):
    c = s[i]
    if c == '(':
        lv += 1
    else: # c == '):
        if pre == '(':
            ans += lv
        lv -= 1
    pre = c

print(ans)