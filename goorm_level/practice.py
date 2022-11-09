# 외계인과 용돈기입장
# https://level.goorm.io/exam/49111/%EC%99%B8%EA%B3%84%EC%9D%B8%EA%B3%BC-%EC%9A%A9%EB%8F%88%EA%B8%B0%EC%9E%85%EC%9E%A5/quiz/1

# N, M = map(int, input().split())
# n_list = list(map(int, input().split()))
# dp = [0] * N
# val_sum = 0

# for idx in range(N):
# 	val_sum += n_list[idx]
# 	dp[idx] = val_sum
# dp.insert(0, 0)
# # print(dp)

# for _ in range(M):
# 	a, b = map(int, input().split())
# 	val_sum = dp[b] - dp[a-1]
# 	if val_sum > 0:
# 		print('+', end='')
# 	print(val_sum)


# [KOI 2017] 방 배정하기
# https://level.goorm.io/exam/48128/%EB%B0%A9-%EB%B0%B0%EC%A0%95%ED%95%98%EA%B8%B0/quiz/1
# A, B, C, N = map(int, input().split())
# dp = [False] * (N+1)
# for n in [A, B, C]:
# 	for x in range(1, N+1):
# 		if dp[x] == True:
# 			if x+n <= N:
# 				dp[x+n] = True
		
# 	for x in range(n, N+1, n):
# 		dp[x] = True

# print(1 if dp[N] else 0)

# [알고리즘먼데이] 큰 수 곱하기 - ★3
# https://level.goorm.io/exam/159176/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%A8%BC%EB%8D%B0%EC%9D%B4-%ED%81%B0-%EC%88%98-%EA%B3%B1%ED%95%98%EA%B8%B0/quiz/1

# n_list = list(map(int, input().split()))
# ans = n_list[0]
# for n in n_list[1:]:
# 	ans *= n
# print(ans)


# 싸이클 - ★3
# https://level.goorm.io/exam/45582/%EC%8B%B8%EC%9D%B4%ED%81%B4/quiz/1

# N, P = map(int, input().split())
# num_dict = dict()
# num = 1
# ans = 0

# while True:
# 	num = (num * N) % P
# 	if num not in num_dict:
# 		num_dict[num] = 1
# 	elif num_dict[num] == 1:
# 		num_dict[num] += 1
# 		ans += 1
# 	else:
# 		break

# print(ans)


# 모래성
# https://level.goorm.io/exam/156680/%EB%AA%A8%EB%9E%98%EC%84%B1/quiz/1

# import sys
# input = sys.stdin.readline
# from collections import deque

# n, m = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
# minus_board = [[0]*m for _ in range(n)]
# inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# ans, minutes = 0, 0

# def all_wet(board, n):
# 	for x in range(n):
# 		if sum(board[x]) != 0:
# 			return False
# 	return True

# def is_there_water(board, n, m):
# 	for x in range(n):
# 		for y in range(m):
# 			if board[x][y] == 0:
# 				return True
# 	return False

# if not is_there_water(board, n, m):
# 	print(0)
# 	exit()

# while not all_wet(board, n):
# 	# 모래성 check
# 	sand_que = deque()
# 	sand_set = set()
# 	sand_num = 0

# 	for x in range(n):
# 		for y in range(m):
# 			if board[x][y] > 0 and tuple([x, y]) not in sand_set:
# 				# print("xy", x, y)
# 				sand_que.append([x, y])
# 				sand_set.add(tuple([x, y]))
										 
# 				# BFS
# 				while sand_que:
# 					tmp_x, tmp_y = sand_que.popleft()
# 					for plus_x, plus_y in inc_xy:
# 						nx, ny = tmp_x + plus_x, tmp_y + plus_y
# 						if 0 <= nx < n and 0 <= ny < m and board[nx][ny] > 0 and tuple([nx, ny]) not in sand_set:
# 							sand_que.append([nx, ny])
# 							sand_set.add(tuple([nx, ny]))
# 				sand_num += 1

# 	if sand_num >= 2:
# 		ans = minutes
# 		break
	
# 	# 1분 지났을 때 모래성 minus 값들 계산
# 	for x in range(n):
# 		for y in range(m):
# 			if board[x][y] > 0:
# 				for plus_x, plus_y in inc_xy:
# 					nx, ny = x + plus_x, y + plus_y
# 					if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
# 						minus_board[x][y] += 1
# 						# print("xy2", x, y, minus_board[x][y])

# 	# 모래사장 1개 부셔지는 시간 계산
# 	min_k = 100
# 	for x in range(n):
# 		for y in range(m):
# 			if board[x][y] > 0:
# 				val_k = (board[x][y] // minus_board[x][y])
# 				if board[x][y] % minus_board[x][y] != 0:
# 					val_k += 1
# 				if min_k > val_k:
# 					min_k = val_k
# 	# print("min_k", min_k)
						
# 	# minus 반영
# 	for x in range(n):
# 		for y in range(m):
# 			board[x][y] = max(0, (board[x][y] - minus_board[x][y]*min_k))
# 			minus_board[x][y] = 0
	
# 	minutes += min_k

# 	# for x in range(n):
# 	# 	print(board[x])

# print(ans)

# try2
# import sys
# input = sys.stdin.readline
# from collections import deque
# from collections import defaultdict

# n, m = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
# minus_board = [[0]*m for _ in range(n)]
# inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# ans, minutes = 0, 0

# def all_wet(board, n):
# 	for x in range(n):
# 		if sum(board[x]) != 0:
# 			return False
# 	return True

# def is_there_water(board, n, m):
# 	for x in range(n):
# 		for y in range(m):
# 			if board[x][y] == 0:
# 				return True
# 	return False

# if not is_there_water(board, n, m):
# 	print(0)
# 	exit()

# xy_dict = defaultdict(list)
# for x in range(n):
# 	for y in range(m):
# 		if board[x][y] > 0:
# 			xy_dict[tuple([x,y])] = board[x][y]

# while not all_wet(board, n):
# 	# 모래성 check
# 	sand_que = deque()
# 	sand_set = set()
# 	sand_num = 0

# 	for key in xy_dict.keys():
# 		x, y = key
# 		if tuple([x, y]) not in sand_set:
# 			# print("xy", x, y)
# 			sand_que.append([x, y])
# 			sand_set.add(tuple([x, y]))
									 
# 			# BFS
# 			while sand_que:
# 				tmp_x, tmp_y = sand_que.popleft()
# 				for plus_x, plus_y in inc_xy:
# 					nx, ny = tmp_x + plus_x, tmp_y + plus_y
# 					if 0 <= nx < n and 0 <= ny < m and board[nx][ny] > 0 and tuple([nx, ny]) not in sand_set:
# 						sand_que.append([nx, ny])
# 						sand_set.add(tuple([nx, ny]))
# 			sand_num += 1

# 	if sand_num >= 2:
# 		ans = minutes
# 		break
	
# 	# 1분 지났을 때 모래성 minus 값들 계산
# 	for key in xy_dict.keys():
# 		x, y = key
# 		for plus_x, plus_y in inc_xy:
# 			nx, ny = x + plus_x, y + plus_y
# 			if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
# 				minus_board[x][y] += 1
# 				# print("xy2", x, y, minus_board[x][y])

# 	# 모래사장 1개 부셔지는 시간 계산
# 	min_k = 100
# 	for key in xy_dict.keys():
# 		x, y = key
# 		val_k = (board[x][y] // minus_board[x][y])
# 		if board[x][y] % minus_board[x][y] != 0:
# 			val_k += 1
# 		if min_k > val_k:
# 			min_k = val_k
# 	# print("min_k", min_k)

# 	pop_key_set = set()
# 	# minus 반영
# 	for key in xy_dict.keys():
# 		x, y = key
# 		board[x][y] = max(0, (board[x][y] - minus_board[x][y]*min_k))
# 		if board[x][y] == 0:
# 		# 	xy_dict.pop(key)
# 			pop_key_set.add(key)
# 		minus_board[x][y] = 0
	
# 	for key in pop_key_set:
# 		xy_dict.pop(key)
# 	# print("xy_dict", xy_dict)

# 	minutes += min_k

# 	for x in range(n):
# 		print(board[x])

# print(ans)


# 방 탈출하기
# https://level.goorm.io/exam/49105/%EB%B0%A9-%ED%83%88%EC%B6%9C%ED%95%98%EA%B8%B0/quiz/1
# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# N = int(input())
# n_list = list(map(int, input().split()))
# M = int(input())
# m_list = list(map(int, input().split()))

# n_dict = defaultdict(list)
# for n in n_list:
# 	n_dict[n] = 1
# for m in m_list:
# 	if m in n_dict:
# 		print(1)
# 	else:
# 		print(0)


# [기본] 4방향 로봇
# n, m, k = map(int, input().split())
# k_list = list(input())
# # print(k_list)

# x, y = 0, 0
# board = [[0]*m for _ in range(n)]
# # inc_xy = dict({'E':[-1, 0], 'W':[1, 0], 'N':[0, -1], 'S':[0, 1]})
# inc_xy = dict({'E':[0, 1], 'W':[0, -1], 'N':[-1, 0], 'S':[1, 0]})
# # print(inc_xy['E'])
# board[0][0] = 1

# for cmd in k_list:
#     plus_x, plus_y = inc_xy[cmd]
#     # print(plus_x, plus_y)
    
#     nx, ny = x + plus_x, y + plus_y
#     if nx < 0: nx = 0
#     elif nx >= n: nx = n-1

#     if ny < 0 : ny = 0
#     elif ny >= m: ny = m-1

#     board[nx][ny] += 1
#     x, y = nx, ny
#     # print(cmd, nx, ny)

# total_max = 0
# for x in range(n):
#     x_max = max(board[x])
#     # print(board[x])
#     # print(x_max)
#     if total_max < x_max:
#         total_max = x_max
# print(total_max)

# this code is not work
# # print(max(max(board)))


# 최대 자리곱
# 이런 접근인가?
# n_list = list(map(int, input()))
# # print(n_list)

# max_val = 1
# for n in n_list:
# 	if n != 0:
# 		max_val *= n

# tmp_max_val = max(1, n_list[0]-1)*(9**(len(n_list)-1))
# # print(max_val, tmp_max_val)
# print(max(max_val, tmp_max_val))


# 완전탐색 했는데 안 풀림
# N = int(input())
# # N_list = list(map(int, input()))

# max_val = 1
# for n in range(1, N+1):
#     tmp_max_val = 1
#     n_list = list(map(int, str(n)))
#     # print(n_list)
#     for nn in n_list:
#         if nn == 0:
#             break
#         else:
#             tmp_max_val *= nn
#     if max_val < tmp_max_val:
#         # print(max_val, tmp_max_val, n_list)
#         max_val = tmp_max_val

# print(max_val)

# 설마..
# n = input()
# n_list = list(map(int, n))
# print(max(1, n_list[0]-1) * 9**(len(n_list)-1))


# 소희와 버스
# import sys
# input = sys.stdin.readline

# N, T = map(int, input().split())
# min_time = 200000
# ans = 0

# for idx in range(N):
#     s, d = map(int, input().split())
	
#     if T < s:
#         waiting_time = s-T
#         if min_time > waiting_time:
#             min_time = waiting_time
#             ans = idx
	
#     elif T == s:
#         ans = idx
#         break
	
#     else: # T > s
#         target_val = T-s
#         times = target_val // d
#         times = s + times * d
		
#         if target_val % d != 0:
#             times += d
		
#         if min_time > times - T:
#             min_time = times - T
#             ans = idx
		
# print(ans+1)