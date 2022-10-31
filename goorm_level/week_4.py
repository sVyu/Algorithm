# 2022/10/30 pm 09:40 ~ 
# 1. 체크 카드
# import sys
# from collections import deque
# input = sys.stdin.readline

# N, M = map(int, input().split())
# ans = N
# que = deque()
# for _ in range(M):
#     # c_l == command_list
#     c_l = list(input().split())
#     c_l[1] = int(c_l[1])

#     if c_l[0] == 'deposit':
#         ans += c_l[1]
#         while que and ans >= que[0]:
#             ans -= que.popleft()
#     elif c_l[0] == 'pay':
#         if ans >= c_l[1]:
#             ans -= c_l[1]
#     else: # c_l[0] == 'reservation'
#         que.append(c_l[1])
#         while que and ans >= que[0]:
#             ans -= que.popleft()

# print(ans)


# 2. 단풍나무
# def copy_board(board, tmp_board, N):
#     for x in range(N):
#         for y in range(N):
#             if tmp_board[x][y] < 0:
#                 board[x][y] = 0
#             else:
#                 board[x][y] = tmp_board[x][y]
#     # return board

# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# tmp_board = [[0] * N for _ in range(N)]
# inc_xy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
# day = 0

# while True:
#     copy_board(tmp_board, board, N)

#     total_sum = 0
#     for x in range(N):
#         total_sum += sum(board[x])
#     if total_sum == 0:
#         break

#     for x in range(N):
#         for y in range(N):
#             for plus_x, plus_y in inc_xy:
#                 nx, ny = x + plus_x, y + plus_y
#                 if 0 <= nx < N and 0 <= ny < N:
#                     if board[nx][ny] == 0:
#                         tmp_board[x][y] -= 1
    
#     copy_board(board, tmp_board, N)
#     day += 1

# print(day)


# 3. 거리두기
# N = int(input())
# dp = [[0] * 5 for _ in range(N+1)]
# dp[0][0] = 1

# # for x in range(N+1):
# #     print(dp[x])

# for x in range(1, N+1):
#     dp[x][0] = sum(dp[x-1])
#     dp[x][1] = dp[x-1][0] + dp[x-1][2] + dp[x-1][3]
#     dp[x][2] = dp[x-1][0] + dp[x-1][1] + dp[x-1][3] + dp[x-1][4]
#     dp[x][3] = dp[x-1][0] + dp[x-1][1] + dp[x-1][2]
#     dp[x][4] = dp[x-1][0] + dp[x-1][2]

#     for y in range(5):
#         dp[x][y] %= 100000007 # 되네?

# print(sum(dp[N]) % 100000007)


# 4. 주차 구역 나누기
# Backtracking ? DP ?
N = int(input())
