import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ns = sorted(list(map(int, input().split())))

l, r = 0, N-1
ans = 0

while l < r:
    now = ns[l]+ns[r]
    if now <= K:
        ans += 1
        l += 1
        r -= 1
    else:
        r -= 1

print(ans)