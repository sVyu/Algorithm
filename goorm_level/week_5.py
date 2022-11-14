# week 5
# 1. 개미와 진딧물
# import sys
# input = sys.stdin.readline
# from collections import deque

# N, M = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# ans = 0

# for x in range(N):
#     for y in range(N):
#         que = deque()
#         if board[x][y] == 1:
#             que.append([x, y])
#             check_set = set({tuple([x, y])})
#             find_check = False
#             k = 0

#             while que and k < M and not find_check:
#                 for _ in range(len(que)):
#                     nx, ny = que.popleft()
#                     for i in range(4):
#                         next_x, next_y = nx + inc_xy[i][0], ny + inc_xy[i][1]
#                         if 0 <= next_x < N and 0 <= next_y < N and tuple([next_x, next_y]) not in check_set:
#                             if board[next_x][next_y] == 2:
#                                 find_check = True
#                                 break
#                             que.append([next_x, next_y])
#                             check_set.add(tuple([next_x, next_y]))
#                     if find_check:
#                         break
#                 k += 1

#             if find_check:
#                 ans += 1

# print(ans)


# 2. 모래섬 - .. 어딘가 틀린다
# import sys
# input = sys.stdin.readline
# from collections import deque

# N, M = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# visit_check_board = [[0] * M for _ in range(N)]
# que = deque()
# ans = -1
# day = 0
# inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# # def check_all_sick(visit_check_board, N, M):
# #     for x in range(N):
# #         for y in range(M):
# #             if visit_check_board[x][y] != 1:
# #                 return False
# #     return True

# for x in range(N):
#     for y in range(M):
#         if board[x][y] == 0:
#             que.append([x, y])
#             visit_check_board[x][y] = 1

# while que:
#     for _ in range(len(que)):
#         x, y = que.popleft()
#         for plus_x, plus_y in inc_xy:
#             nx, ny = x + plus_x, y + plus_y
#             if 0 <= nx < N and 0 <= ny < M and visit_check_board[nx][ny] == 0:
#                 que.append([nx, ny])
#                 visit_check_board[nx][ny] = 1

#     day += 1
#     # for x in range(N):
#     #     print(visit_check_board[x])
#     # input()

#     sum_of_sand_island = 0
#     sand_island_que = deque()
#     xy_set = set()

#     for x in range(N):
#         for y in range(M):
#             if visit_check_board[x][y] == 0 and tuple([x, y]) not in xy_set:
# #                 이 코드를 여기에 쓸 게 아니었네 !
# #                 if sum_of_sand_island >= 2:
# #                     print(day)
# #                     exit()
#                 sand_island_que.append([x, y])
#                 xy_set.add(tuple([x, y]))

#                 while sand_island_que:
#                     nx, ny = sand_island_que.popleft()
#                     # print("test", x, y)
#                     for plus_x, plus_y in inc_xy:
#                         next_x, next_y = nx + plus_x, ny + plus_y
#                         if 0 <= next_x < N and 0 <= next_y < M and tuple([next_x, next_y]) not in xy_set:
#                             if visit_check_board[next_x][next_y] == 0:
#                                 sand_island_que.append([next_x, next_y])
#                                 xy_set.add(tuple([next_x, next_y]))
#                 sum_of_sand_island += 1
#                 # print("test__", x, y, sum_of_sand_island)
#     if sum_of_sand_island >= 2:
#         ans = day
#         break

# print(ans)


# 3. 수 이어 붙이기 - clear
# import itertools

# N = int(input())
# n_list = list(map(str, input().split()))
# min_val = 9999999999999999

# for n in itertools.permutations(n_list, N):
#     # print(n)
#     new_num = ['-1'] * (2*N)
#     new_num[:2] = n[0]
#     idx = 1

#     for i in range(1, N):
#         if n[i-1][1] != n[i][0]:
#             idx += 1
#             new_num[idx] = n[i][0]
#         idx += 1
#         new_num[idx] = n[i][1]
    
#     while new_num[-1] == '-1':
#         new_num.pop()
#     # print(int(''.join(new_num)))
#     new_num = int(''.join(new_num))
#     if min_val > new_num:
#         min_val = new_num

# print(min_val)


# 4. 구슬 게임
# 부분적으로 FAIL이 뜨는 걸 보니 어딘가 놓친 부분이 있다
# N, M, K = map(int, input().split())
# low_limit = max(0, N-M)
# high_limit = N+M
# dp = [[0] * (high_limit+1) for _ in range(K+1)]
# dp[0][N] = 1

# for x in range(1, K+1):
#     dp[x][low_limit] = dp[x-1][low_limit+1]

#     for y in range(low_limit+1, high_limit):
#         if y == low_limit+1:
#             dp[x][y] = dp[x-1][y] + dp[x-1][y+1]
#         elif y == high_limit-1:
#             dp[x][y] = dp[x-1][y] + dp[x-1][y-1]
#         else:
#             dp[x][y] = dp[x-1][y-1] + dp[x-1][y] + dp[x-1][y+1]

#     dp[x][high_limit] = dp[x-1][high_limit-1]

# ans = 0
# for x in range(K+1):
#     # print(dp[x][:N+M+1])
#     ans += dp[x][low_limit] + dp[x][high_limit]

# print(ans)