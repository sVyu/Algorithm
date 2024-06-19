import sys
input = sys.stdin.readline

N = int(input())
s = []
ans = 0
for _ in range(N):
    ns = list(map(int, input().split()))
    if ns[0] == 1:
        s.append(ns[1:])

    if s:
        rest_time = s[-1][1]
        if s[-1][1] == 1:
            ans += s.pop()[0]
        else:
            s[-1][1] = rest_time-1

# print(s)
print(ans)