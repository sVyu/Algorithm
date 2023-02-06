# 2023/02/04

# A번 - :chino_shock:
# emoji = list(input())

# colon, underbar = 0, 0
# for e in emoji:
#     if e == ':': colon += 1
#     elif e == '_': underbar += 1

# print(len(emoji) + colon + underbar*5)


# B번 - 치노의 라떼 아트 (Easy)
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     R, C = map(int, input().split())
#     board = [list(input()) for _ in range(R)]

#     min_x, max_x, min_y, max_y = R, -1, C, -1

#     # #체크
#     for x in range(R):
#         for y in range(C):
#             if board[x][y] == '#':
#                 min_x = min(min_x, x)
#                 max_x = max(max_x, x)
#                 min_y = min(min_y, y)
#                 max_y = max(max_y, y)
#     # print(min_x, max_x, min_y, max_y)

#     ans = 1
#     if min_x == R or (min_x == max_x and min_y == max_y) or ((max_x-min_x) != (max_y-min_y)):
#         ans = 0
#     else:
#         point_min_x, point_max_x, point_min_y, point_max_y = R, -1, C, -1
#         for x in range(min_x, max_x+1):
#             for y in range(min_y, max_y+1):
#                 if board[x][y] == '.':
#                     point_min_x = min(point_min_x, x)
#                     point_max_x = max(point_max_x, x)
#                     point_min_y = min(point_min_y, y)
#                     point_max_y = max(point_max_y, y)
#         # print(point_min_x, point_max_x, point_min_y, point_max_y)

#         cnt = 0
#         for x in [min_x, max_x]:
#             for y in [min_y, max_y]:
#                 if board[x][y] == '.':
#                     cnt += 1
#         # print(cnt)

#         pos = True
#         if cnt != 1 or ((point_max_x-point_min_x) != (point_max_y-point_min_y)):
#             pos = False

#         if pos:
#             for x in range(point_min_x, point_max_x+1):
#                 for y in range(point_min_y, point_max_y+1):
#                     if board[x][y] == '#':
#                         pos = False

#                 if not pos:
#                     break

#         if not pos:
#             ans = 0

#     print(ans)


# C
# import sys

# M, N, Q = map(int, input().split())
# a = list(map(int, input().split()))

# ans = [1]*N
# for i in range(1, M+1):
#     print("? {0} {1}".format(i, i))
#     sys.stdout.flush()
#     tmp = int(input())
#     ans[i-1] = (tmp % a[i-1]+1)

# print("!", *ans, sep =' ')
# sys.stdout.flush()


# D
# from heapq import  heappush, heappop

# N, M, K = map(int, input().split())
# animes = list(map(int, input().split()))

# heap = []
# for a in animes:
#     heappush(heap, [a, M-a])
