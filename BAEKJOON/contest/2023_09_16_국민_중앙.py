# 2023 국민대학교 & 중앙대학교 프로그래밍 경진대회 Open Contest · Arena #7

# A
# W, H = map(int, input().split())
# print('{0:.1f}'.format(W*H/2))

# N = int(input())
# ns = list(map(int, input().split()))


# B
# ans = 0
# now = 0
# for n in ns:
#     if n:
#         now 0= 1
#         ans = max(ans, now)
#     else:
#         now = 0

# print(ans)


# C
# def solve():
#     N, X = map(float, input().split())
#     N = int(N)

#     grades = dict({
#         'A+': 4.5,
#         'A0': 4.0,
#         'B+': 3.5,
#         'B0': 3.0,
#         'C+': 2.5,
#         'C0': 2.0,
#         'D+': 1.5,
#         'D0': 1.0,
#         'F': 0},
#     )

#     sum_ci = 0
#     now = 0
#     for _ in range(N-1):
#         ci, gi = map(str, input().split())
#         # ci = int(ci)
#         ci = float(ci)
#         sum_ci += ci
#         now += ci * grades[gi]

#     res = int(input())
#     sum_ci += res
#     # print(sum_ci, now)
#     # (now + x*res) / sum_ci > X
#     # (now + x*res)  > X*sum_ci

#     grades = sorted(list(grades.items()), key=lambda x:(x[1]))
#     # print(grades)

#     if int(100*((now + 4.5*res)/sum_ci)) <= X*100:
#         print("impossible")
#     else:
#         for i in range(9):
#             # print(grades[i], ((now + grades[i][1]*res)/sum_ci), ((now + grades[i][1]*res)/sum_ci)*100)
#             if int(100*((now + grades[i][1]*res)/sum_ci)) >= X*100:
#                 print(grades[i][0])
#                 return

# solve()


# D
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# broads = [list(input().rstrip().split()) for _ in range(N)]

# names = set(broads[i][0] for i in range(N))
# # print(names)
# times = dict()
# checks = dict()
# for name in names:
#     times[name] = [0]*(M//7)
#     checks[name] = [0]*(M//7)

# # print(times)

# def cal_time(s):
#     sh, sm = map(int, s.split(':'))
#     return sh*60+sm

# for name, day, s, e in broads:
#     times[name][(int(day)-1)//7] += cal_time(e)-cal_time(s)
#     checks[name][(int(day)-1)//7] += 1
# # print(times.items())
# # print(checks.items())

# ans = []
# for name in names:
#     pos = True

#     for i in range(M//7):
#         if times[name][i] < 3600 or checks[name][i] < 5:
#             pos = False
#             break

#     if pos:
#         ans.append(name)

# # print(ans)

# if ans:
#     print(*sorted(ans), sep='\n')
# else:
#     print(-1)


# F
# N, K = map(int, input().split())

# ss = list(map(int, input().split()))
# hs = list(map(int, input().split()))

# dp = [[0]*101 for _ in range(N+1)]
# for i in range(1, N+1):
#     # !!
#     for y in range(101):
#         dp[i][y] = dp[i-1][y]

#     for y in range(101-hs[i-1]):
#         dp[i][y] = max(dp[i][y], dp[i-1][y+hs[i-1]] + ss[i-1])

#     tmp_dp = [0]*101
#     for y in range(101):
#         if y+K <= 100:
#             tmp_dp[y+K] = dp[i][y]
#         else:
#             tmp_dp[100] = max(tmp_dp[100], dp[i][y])

#     dp[i] = tmp_dp

# print(max(dp[N]))


# E
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# bs = sorted(list(map(int, input().split())))
# bs.append(int(1e7))
# # print(bs)
# ps = [list(map(int, input().split())) for _ in range(M)]
# ps = sorted(ps, key=lambda x:(x[0]))
# # print(ps)

# new_ps = [0]*M
# for i in range(M):
#     l, r = 0, N-1
#     t = 0
#     while l <= r:
#         mid = (l+r)//2
#         if bs[mid] <= ps[i][0]:
#             t = mid
#             l = mid+1
#         else:
#             r = mid-1
#     # print(t)
#     new_ps[i] = [min(abs(ps[i][0]-bs[t]), abs(bs[t+1]-ps[i][0])), ps[i][1]]
# # print(new_ps)

# P = 0
# for d, w in new_ps:
#     P = max(P, d*w)
# print(P)


# G
# import sys
# input = sys.stdin.readline
# from heapq import heapify, heappop

# N = int(input())
# ps = [list(map(int, input().split())) for _ in range(N)]
# dists = [0]*(N*(N-1)//2)

# # cal_dist
# def c_d(p1, p2):
#     x1, y1 = p1
#     x2, y2 = p2
#     # 부동소수점 오차 때문에 sqrt 생략
#     return (x2-x1)**2+(y2-y1)**2

# idx = 0
# for i in range(N-1):
#     for j in range(i+1, N):
#         # dists.append([c_d(ps[i], ps[j]), i+1, j+1])
#         dists[idx] = [c_d(ps[i], ps[j]), i+1, j+1]
#         idx += 1
# heapify(dists)
# # print(dists)

# parent = [i for i in range(N+1)]

# def find(x):
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]

# def union(a, b):
#     a = find(a)
#     b = find(b)

#     if a > b:
#         parent[a] = b
#     else:
#         parent[b] = a

# ans = [0]*(N-1)
# idx = 0
# while dists:
#     d, p1, p2 = heappop(dists)
#     # print("!", d, p1, p2)

#     if find(p1) != find(p2):
#         # ans.append([p1, p2])
#         ans[idx] = [p1, p2]
#         idx += 1
#         union(p1, p2)

# # print(ans)
# for a in ans:
#     print(*a)

