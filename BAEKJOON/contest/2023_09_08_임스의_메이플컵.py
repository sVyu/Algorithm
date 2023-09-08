# 임스의 메이플컵
# A

# N, U, L = map(int, input().split())

# if N >= 1000:
#     if U >= 8000 or L >= 260:
#         print("Very Good")
#     else:
#         print("Good")
# else:
#     print("Bad")


# B
# N, M = map(int, input().split())
# cnt_n, cnt_m = 0, 0
# now_n, now_m = -1, -1
# ns = sorted(list(map(int, input().split())))
# ms = sorted(list(map(int, input().split())))

# for n in ns:
#     if now_n <= n:
#         now_n = n+100
#         cnt_n += 1

# for m in ms:
#     if now_m <= m:
#         now_m = m+360
#         cnt_m += 1

# print(cnt_n, cnt_m)


# C
# import math

# N, M, K = map(int, input().split())
# ds = [int(input()) for _ in range(N)]
# ps = [list(map(int, input().split())) for _ in range(K)]

# ans = []
# for d in ds:
#     dp = [[0]*901 for _ in range(K+1)]

#     for x in range(1, K+1):
#         sec = math.ceil(ps[x-1][0]/d)
#         # print(sec, ps[x][1])
#         for y in range(1, 901):
#             dp[x][y] = max(dp[x][y-1], dp[x-1][y])
#             if y >= sec:
#                 dp[x][y] = max(dp[x][y], dp[x-1][y-sec]+ps[x-1][1])

#     ans.append(max(dp[K]))

# print(sum(sorted(ans)[-min(N,M):]))


# D
# import sys
# import itertools
# from collections import defaultdict

# def solve():
#     N, H = map(int, input().split())
#     ss = list(input().rstrip())

#     if H >= 4:
#         if N >= 4:
#             print(-1)
#         else:
#             d = defaultdict(int)
#             for s in ss:
#                 d[s] += 1
#             print(max(d.values())-1)
#         return

#     # H <= 3
#     if N == 1:
#         print(0)
#         return
#     if N == 2:
#         if H == 1:
#             print(0)
#             return

#         if ss[0] == ss[1]:
#             print(1)
#         else:
#             print(0)
#         return

#     # N >= 3
#     if H == 1:
#         print(0)
#     elif H == 2:
#         cnt = 0
#         for i in range(1, N):
#             if ss[i] == ss[i-1]:
#                 cnt += 1
#                 ss[i] = '_'
#         print(cnt)
#     elif H == 3:
#         if N == 3:
#             d = defaultdict(int)
#             for s in ss:
#                 d[s] += 1
#             print(max(d.values())-1)
#             return

#         # N >= 4
#         min_cnt = N
#         for c in itertools.permutations(['S','R','W'], 3):
#             # print(c)

#             cnt = 0
#             for i in range(N):
#                 if ss[i] != c[i%3]:
#                     cnt += 1
#             min_cnt = min(min_cnt, cnt)

#         print(min_cnt)

# solve()