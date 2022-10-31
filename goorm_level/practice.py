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
