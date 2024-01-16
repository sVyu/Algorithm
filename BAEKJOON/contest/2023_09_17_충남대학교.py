# 2023 충남대학교 SW-IT Contest Open - Division 1 · Arena #8

# A
# A, B = map(int, input().split())
# K = min(max(A-1, 0), B)
# print(2*K+1)

# B
# N = int(input())
# an = list(map(int, input().split()))
# bn = list(map(int, input().split()))

# ans = 0
# for i in range(N):
#     if an[i] > bn[i]:
#         ans += an[i]-bn[i]

# print(ans)


# C
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# classes = [0]*(N+1)

# for _ in range(M):
#     k, s, e = map(int, input().split())
#     if classes[k] <= s:
#         print("YES")
#         classes[k] = e
#     else:
#         print("NO")


# D
# A, B = map(int, input().split())

# def ss(n):
#     s = "a"
#     for _ in range(n):
#         s += "ba"
#     return s

# if A > 2*B:
#     print("NO")
# else:
#     cnt = 0
#     t = -1 if A < 2*B else 0
#     ans = []

#     if A < 2*B:
#         for n in range(1, B+1):
#             if (A-n-1) == 2*(B-n):
#                 t = n
#                 break
#         # print("t", t)
#         cnt += 1
#         ans.append(ss(t))
#         A -= n-1
#         B -= n

#     if A:
#         cnt += B
#         for _ in range(B):
#             ans.append(ss(1))

#     # print(cnt)
#     # print(ans)

#     if t >= 0:
#         print("YES")
#         print(cnt)
#         print(*ans, sep='\n')
#     else:
#         print("NO")


# E
# def solve():
#     N = int(input())
#     if N == 1:
#         print("YES")
#         print("1")
#     elif N < 4:
#         print("NO")
#     else:
#         ans = []
#         checks = [False]*(N+1)

# solve()


# import math
# import sys
# sys.setrecursionlimit(int(1e5))

# N = int(input())
# ans = [0]*N

# def check_prime(n):
#     if n == 1: return False
#     elif n == 2: return True
#     elif n % 2 == 0: return False
#     else:
#         for div in range(3, math.isqrt(n)+1):
#             if n % div == 0:
#                 return False
#         return True

# def btr(idx, sums, used):
#     for i in range(1, N+1):
#         if not used[i] and not check_prime(sums+i):
#             used[i] = True
#             ans[idx] = i
#             # print(*ans)
#             if idx < N-1:
#                 if btr(idx+1, sums+i, used) != -1:
#                     return ans
#             else:
#                 return ans
#             used[i] = False
#             ans[idx] = 0
#     return -1

# def solve():
#     used = [False]*(N+1)
#     if btr(0, 0, used) != -1:
#         print("YES")
#         print(*ans)
#     else:
#         print("NO")

# solve()


# F
# import sys
# input = sys.stdin.readline

# N, A, B = map(int, input().split())
# pqs = [list(map(int, input().split())) for _ in range(N)]
# tmp_pqs = [(pqs[i][0]-pqs[i][1]) for i in range(N)]
# tmp_pqs.sort(reverse=True)
# # print(tmp_pqs)

# print(sum(pqs[i][0] for i in range(N)) - sum(tmp_pqs[:B]))


# G
# 여기 연습
# def transform(col):

# import sys
# input = sys.stdin.readline

# N = int(input())
# # color, rotation
# cols = list(input().rstrip())
# print(cols)
# rot = ['R', 'G', 'B']

# def transform(col):
#     if 'R': return 'G'
#     elif 'G': return 'B'
#     else: return 'R'

# ans = int(4e5)
# for target_col in rot:
#     print("tt", target_col)
#     pos = True
#     cnt = 0
#     for i in range(N-2):
#         print("ii", i)
#         if i == N-3:
#             if not (cols[-3] == cols[-2] == cols[-1]):
#                 pos = False
#                 break
#         while cols[i] != target_col:
#             cols[i] = transform(cols[i+1])
#             cols[i+1] = transform(cols[i+1])
#             cols[i+2] = transform(cols[i+2])
#             cnt += 1
#             print(i, cols)
#             input()
#     if pos:
#         ans = min(ans, cnt)

# print(ans)


# import sys
# input = sys.stdin.readline

# N = int(input())
# # color, rotation
# cols = list(input().rstrip())
# # print(cols)
# rot = ['R', 'G', 'B']

# def transform(col):
#     if col == 'R': return 'G'
#     elif col == 'G': return 'B'
#     else: return 'R'

# ans = int(4e5)
# for target_col in rot:
#     tmp_cols = cols[:]
#     pos = True
#     cnt = 0
#     for i in range(N-2):
#         if i == N-3:
#             if not (tmp_cols[-3] == tmp_cols[-2] == tmp_cols[-1]):
#                 pos = False
#                 break
#         while tmp_cols[i] != target_col:
#             tmp_cols[i] = transform(tmp_cols[i])
#             tmp_cols[i+1] = transform(tmp_cols[i+1])
#             tmp_cols[i+2] = transform(tmp_cols[i+2])
#             cnt += 1
#             # input()
#     if pos:
#         ans = min(ans, cnt)

# print(ans if ans != int(4e5) else -1)


# H
# from heapq import heappush, heappop
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# check = [[False]*M f _ in range(N)]

# xy_set = set()
# for x in [0, N-1]:
#     for y in range(M):
#         check[x][y] = True
#         xy_set.add(tuple([x, y]))

# for x in range(N):
#     for y in [0, M-1]:
#         check[x][y] = True
#         xy_set.add(tuple([x, y]))
# # print(len(xy_set))

# heap = []
# for x, y in xy_set:
#     heappush(heap, [-board[x][y], x, y])
# # print(heap)

# for _ in range(int(input())):
#     val, x, y = heappop(heap)
#     print(x+1, y+1)

#     for px, py in inc_xy:
#         nx, ny = x+px, y+py
#         if 0 <= nx < N and 0 <= ny < M and not check[nx][ny]:
#             check[nx][ny] = True
#             heappush(heap, [-board[nx][ny], nx, ny])


# I

# J
# 사이클 판별 ?

# K
# 범위가 이상하네 ㅋㅋㅋ
# from collections import deque

# N, M, K = map(int, input().split())
# NM = N*M
# q = deque()
# blossomed = [[False]*M for _ in range(N)]
# inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# cnt = 0
# for _ in range(K):
#     x, y = map(int, input().split())
#     blossomed[x-1][y-1] = True
#     q.append([x-1, y-1])
#     cnt += 1
# # print("day0", q)

# day = 0
# while NM != cnt:
#     day += 1
#     for _ in range(len(q)):
#         x, y = q.popleft()
#         for px, py in inc_xy:
#             nx, ny = x+px, y+py
#             if 0 <= nx < N and 0 <= ny < M and not blossomed[nx][ny]:
#                 blossomed[nx][ny] = True
#                 cnt += 1
#                 q.append([nx, ny])
#     # print("q", q)

# print(day)