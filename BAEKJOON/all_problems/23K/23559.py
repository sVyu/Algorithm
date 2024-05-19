import sys
input = sys.stdin.readline

N, X = map(int, input().split())
ns = [list(map(int, input().split())) for _ in range(N)]

ns = [[ns[i][0], ns[i][1], ns[i][0]-ns[i][1]] for i in range(N)]
ns.sort(key=lambda x:(-x[2]))
# print(ns)

ans = 0
# 5000*k + 1000*(N-k)
# X >= 4000*k + 1000*N
k = (X-1000*N)//4000
# print(k)

# 1000원짜리 메뉴가 더 맛있는 경우
ti = N
for i in range(N):
    if ns[i][2] <= 0:
        ti = i
        break
# print(ti)

k = min(k, ti)
ans = sum(ns[i][0] for i in range(k)) + sum(ns[-i][1] for i in range(1, N-k+1))
print(ans)