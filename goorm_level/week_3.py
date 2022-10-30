# 3주차
# 1번 0커플
# N = int(input())
# n_list = list(map(int, input().split()))
# idx_limit = 200001

# score_list = [0] * idx_limit
# for num in n_list:
# 	abs_num = abs(num)
# 	if score_list[abs_num] == 0:
# 		if num > 0:
# 			score_list[abs_num] = 1
# 		else:
# 			score_list[abs_num] = -1
# 	else:
# 		score_list[abs_num] = 0

# ans = 0
# for idx in range(idx_limit):
# 	if score_list[idx] != 0:
# 		ans += idx * score_list[idx]
# print(ans)

# 2번 폴더 폰 자판
# n = int(input())
# s = list(map(int, input()))
# chr_list = ["_", [1, '.', ',', '?', '!'], [2, 'A', 'B', 'C'], [3, 'D', 'E', 'F'],\
# 								 [4, 'G', 'H', 'I'],			[5, 'J', 'K', 'L'], [6, 'M', 'N', 'O'],\
# 								 [7, 'P', 'Q', 'R', 'S'],	[8, 'T', 'U', 'V'], [9, 'W', 'X', 'Y', 'Z']]
# len_chr_list = [0, 5, 4, 4, 4, 4, 4, 5, 4, 5]
# ans_list = [""] * 100000

# pre_val, in_s_idx = -1, -1
# cnt = 0
# for idx in range(n):
# 	if pre_val != s[idx]:
# 		if idx != 0:
# 			in_s_idx += 1
# 			ans_list[in_s_idx] = chr_list[pre_val][cnt % len_chr_list[pre_val]]

# 		pre_val = s[idx]
# 		cnt = 0
# 	else:
# 		cnt += 1
# # last chr
# ans_list[in_s_idx+1] = chr_list[pre_val][cnt % len_chr_list[pre_val]]

# print(*ans_list, sep='')


# 3번 구름이의 여행
# timeout 개선 방법 : divide and conquer,, 근데 FAIL은 어디서?
# import sys
# input = sys.stdin.readline

# def graph_copy(g, N):
# 	new_graph = [[] for _ in range(N)]
# 	for idx in range(N):
# 		new_graph[idx] = g[idx][:]
# 	return new_graph

# N, M, K = map(int, input().split())
# g = [[0] * N for _ in range(N)]
# for _ in range(M):
# 	x, y = map(int, input().split())
# 	x -= 1
# 	y -= 1
# 	g[x][y] += 1
# 	g[y][x] += 1
# # for x in range(N):
# # 	print(x+1, g[x])
# if K == 1:
# 	if g[0][N-1] > 0:
# 		print("YES")
# 	else:
# 		print("NO")
# else:
# 	# pre_g = g.copy()
# 	pre_g = graph_copy(g, N)
# 	ans_g = [[0] * N for _ in range(N)]
# 	check = False
# 	for _ in range(K-1):
# 		for x in range(N):
# 			for y in range(N):
# 				for k in range(K):
# 					ans_g[x][y] += pre_g[x][k] * g[k][y]
# 		if ans_g[0][N-1] > 0:
# 			check = True
# 			break
# 		pre_g = graph_copy(ans_g, N)
# 	if check: print("YES")
# 	else: print("NO")

# 4번 순환하는 수로
# import sys
# input = sys.stdin.readline

# N = int(input())
# g = [[0] * N for _ in range(N)]
# for _ in range(N):
# 	a, b = map(int, input().split())
# 	a -= 1; b -=1
# 	g[a][b] += 1
# 	g[b][a] += 1
# # for x in range(N):
# # 	print(g[x])

# # cycle 판별..!



# 1. 0커플
# N = int(input())
# print(sum(list(map(int, input().split()))))

# 마이너스 값 먼저 들어가면 pop이 안 됨
# import sys
# input = sys.stdin.readline
# from collections import defaultdict
# n = int(input())
# dic = defaultdict()
# arr = list(map(int, input().split()))
# for i in arr:
#     if abs(i) in dic:
#         dic.pop(abs(i))
#         print(abs(i))
#     else:
#         dic[i] = 1
#         print(dic)
# print(sum(dic.keys()))

# 개선 코드
# N = int(input())
# n_list = list(map(int, input().split()))
# n_dict = dict()

# for n in n_list:
# 	if (-n) in n_dict:
# 		n_dict.pop(-n)
# 	else:
# 		n_dict[n] = 1
# 		# print(n_dict)

# print(sum(n_dict.keys()))


# 2. 폴더 폰 자판
# import sys
# input = sys.stdin.readline

# dic = {
# 	'1': "1.,?!",
# 	'2': "2ABC",
# 	'3': "3DEF",
# 	'4': "4GHI",
# 	'5': "5JKL",
# 	'6': "6MNO",
# 	'7': "7PQRS",
# 	'8': "8TUV",
# 	'9': "9WXYZ"
# }

# n = int(input())
# s = input()
# cnt = 0
# ans = ''

# for i in range(n):
# 	# n-1, n에서 indexerror 가 안 나는 이유
# 	# s = input() 다음 rstrip()을 안 해서 개행문자가 살아있음
# 	if s[i] == s[i+1]:
# 		cnt += 1
# 	else:
# 		cnt %= len(dic[s[i]])
# 		ans += dic[s[i]][cnt]
# 		cnt = 0

# print(ans)


# 3
# import sys
# from collections import defaultdict
# from collections import deque
# input = sys.stdin.readline

# def solution():
# 	N, M, K = map(int, input().split())
# 	# g == graph
# 	g = defaultdict(list)
# 	for _ in range(M):
# 		u, v = map(int, input().split())
# 		g[u].append(v)
# 		g[v].append(u)
# 	visited = [0]*(N+1)
# 	que = deque([1])
# 	cnt = 1
# 	visited[1] = 1
	
# 	while que and cnt <= K:
# 		for _ in range(len(que)):
# 			now_v = que.popleft()

# 			for next_v in g[now_v]:
# 				if visited[next_v] == 0:
# 					if next_v == N:
# 						return "YES"
# 					visited[next_v] = cnt
# 					que.append(next_v)
# 		cnt += 1
# 	return "NO"

# print(solution())


# 4. 순환하는 수로
# import sys
# from collections import defaultdict
# input = sys.stdin.readline
# sys.setrecursionlimit(10**8)

# N = int(input())
# g = defaultdict(list)
# for _ in range(N):
#     a, b = map(int, input().split())
#     g[a].append(b)
#     g[b].append(a)
# # print(g)

# visited = [0]*(N+1)
# circle = []
# finded = -1

# def FindCycle(u, pre_u):
#     global finded
    
#     if visited[u] == 1:
#         finded = u
#         if u not in circle:
#             circle.append(u)
#         return
#     else:
#         visited[u] = 1

#     for i in g[u]:
#         if i == pre_u:
#             continue
        
#         FindCycle(i, u)


'''
5
1 2
2 3
2 4
3 4
4 5
'''

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**8)
# from collections import defaultdict

# n = int(input())
# graph = defaultdict(list)
# for i in range(n):
#     s, e = map(int, input().split())
#     graph[s].append(e)
#     graph[e].append(s)


# visited = [0] * (n+1)
# circle = []
# finded = -1

# def FindCycle(u, pre_u):
#     global finded

#     if visited[u] == 1:
#         finded = u
#         if u not in circle:
#             circle.append(u)
#         return
    
#     else:
#         visited[u] = 1
    
#     for i in graph[u]:
#         if i == pre_u:
#             continue
#         FindCycle(i, u)

#         if finded == -2:
#             return

#         if finded == u:
#             finded = -2
#             return
        
#         if finded >= 0:
#             if u not in circle:
#                 circle.append(u)
#             return
# FindCycle(1, 1)

# print(len(circle))
# print(' '.join(map(str, sorted(circle))))


# '''
# vistied = 방문 여부 모두 기록
# finded = 방금 전 방문 여부
# '''
# visited = [0 for _ in range(n+1)]
# circle = list()
# finded = -1

# #탐색 재귀
# def FindCycle(u, tar):
#     # finded 변수는 공급 물탱크와 방문 여부를 확인하기 위한 변수입니다.
#     global finded
#     # 방문 기록이 있다면, 순환구조라고 할 수 있다. 
#     # 순환되는 고리는 단 1개이기 때문이다.
#     if visited[u] == 1:
#         finded = u
#         print("haha", finded, u)
#         if u not in circle:
#             circle.append(u)
#         return
#     # 방문 기록이 없다면, 방문 기록을 남긴다. Visited변수는 방문 기록을 남긴다.
#     visited[u] = 1
#     # 도착한 물탱크(노드)에서 갈 수 있는 물탱크들로 물을 보낸다.
#     for i in graph[u]:
#     # 만약에 i값이 이전의 공급한 물탱크는 탐색 정지
#         print("go", i, u, "pre: ", tar)
#         if i == tar:
#             continue
# 	# 방문한 적 없고, 공급한 물탱크가 아니라면 새로운 탐색지점으로 잡는다.
# 	# 즉, 새로운 재귀 시작 지점이 된다.
#         FindCycle(i, u)
#         print("test", i, u, finded)

# 	# 이미 발견된 순환 고리 값이라면 탐색 정지
#         if finded == -2:
#             return

# 	# finded = u라면 이미 방문 지점이기때문에 탐색 정지
#         if finded == u:
#             finded = -2
#             return
# 	# 새롭게 발견한 순환 고리 값이라면 순환 고리에 추가하고, 탐색 종료
#         if finded >= 0:
#             if u not in circle:
#                 circle.append(u)
#             return
# FindCycle(1, 1)

# #저장된 순한 값 정렬
# circle.sort()
# # 순환의 길이
# print(len(circle))
# #순환 오름차순으로 출력
# for i in circle:
#     print(i, end = ' ')