# [알고리즘먼데이]
# 1번 - 출석부
# for _ in range(int(input())):
# 	n = int(input())
# 	num_list = list(map(int, input().split()))
# 	avg = sum(num_list)/n
# 	print (sum(1 for num in num_list if num >= avg), '/', n, sep='')

# 2번 - 철자 분리 집합
# n = int(input())
# s = list(input())
# print(sum(1 for idx in range(1, n) if s[idx-1] != s[idx])+1)

# 3번 - 합격자 찾기
# N, k = map(int, input().split())
# info_list = [list(input().split()) for _ in range(N)]
# for idx in range(N):
# 	info_list[idx][1] = float(info_list[idx][1])
# print("{0} {1:.2f}".format(*sorted(info_list, key=lambda x:(x[0],x[1]))[k-1]))

# 4번 - 폭탄 구현하기
# from collections import deque

# n, k = map(int, input().split())
# board = [[0] * n for _ in range(n)]
# que = deque()
# for _ in range(k):
# 	x, y = map(int, input().split())
# 	que.append([x-1, y-1])
# inc_xy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

# while que:
# 	x, y = que.popleft()
# 	board[x][y] += 1
# 	for i in range(4):
# 		nx, ny = x + inc_xy[i][0], y + inc_xy[i][1]
# 		if 0 <= nx < n and 0 <= ny < n:
# 			board[nx][ny] += 1

# ans = 0
# for x in range(n):
# 	ans += sum(board[x])
# print(ans)