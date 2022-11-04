# 2022/10/30 pm 09:40 ~ 11:20 (3번까지 1시간)
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
# N = int(input())


# 복습
# 1. 체크카드
# import sys
# input = sys.stdin.readline
# from collections import deque

# N, M = map(int, input().split())
# que = deque()
# for _ in range(M):
# 	cmd, k = map(str, input().split())
# 	k = int(k)
	
# 	if cmd == 'deposit':
# 		N += k
# 		while que and N >= que[0]:
# 			N -= que.popleft()
# 	elif cmd == 'pay':
# 		if N >= k:
# 			N -= k
# 	else: # cmd == reservation
# 		que.append(k)
# 		while que and N >= que[0]:
# 			N -= que.popleft()

# print(N)


# 2. 단풍나무
# import sys
# input = sys.stdin.readline

# def complete_check(board, N):
# 	val_sum = 0
# 	for x in range(N):
# 		val_sum += sum(board[x])
# 	return (True if val_sum == 0 else False)

# def clear_board(N):
# 	return [[0]*N for _ in range(N)]

# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# tmp_board = clear_board(N)

# day = 0
# inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# while True:
# 	if complete_check(board, N):
# 		break

# 	for x in range(N):
# 		for y in range(N):
# 			for k in range(4):
# 				nx, ny = x + inc_xy[k][0], y + inc_xy[k][1]
# 				if 0 <= nx < N and 0 <= ny < N:
# 					if not board[nx][ny]:
# 						tmp_board[x][y] += 1
	
# 	for x in range(N):
# 		for y in range(N):
# 			board[x][y] -= min(board[x][y], tmp_board[x][y])
			
# 	day += 1
# 	tmp_board = clear_board(N)
	
# print(day)


# 3. 거리두기
# N = int(input())
# dp = [[0]*5 for _ in range(N+1)]
# dp[0][0] = 1
# mod_val = int(1e8 + 7)

# for i in range(1, N+1):
#     dp[i][0] = sum(dp[i-1]) % mod_val
#     dp[i][1] = dp[i-1][0] + dp[i-1][2] + dp[i-1][3] % mod_val
#     dp[i][2] = dp[i-1][0] + dp[i-1][1] + dp[i-1][3] + dp[i-1][4] % mod_val
#     dp[i][3] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2] % mod_val
#     dp[i][4] = dp[i-1][0] + dp[i-1][2] % mod_val

# print(sum(dp[N]) % mod_val)


# 4. 주차 구역 나누기
# 해설 봐도 이해가 안 됨
# import sys
# input = sys.stdin.readline

# n = int(input())
# dp = [0, 0, 1] + [0] * (n-2)
# for i in range(3, n+1):
# 	val = 0
# 	for k in range(2):
# 		val += (2*(i-k)-1) * dp[i-1-k]
# 	dp[i] = val
# print(dp[n] % 100000007)

# import sys
# input = sys.stdin.readline
# from collections import deque

# n = int(input())
# dp = deque()

# dp.append(0)
# dp.append(0)
# dp.append(1)
# for i in range(3, n+1):
#     dp.append((2*(i-1)+1) * dp[-1] + dp[-2])
#     dp.popleft()
# print(dp[-1] % 100000007)