# 1. 구름 숫자
# N = int(input())
# S = list(input())
# num_dict = dict({
#     'qw':'1', 'as':'2', 'zx':'3', 'we':'4', 'sd':'5',
#     'xc':'6', 'er':'7', 'df':'8', 'cv':'9', 'ze':'0'})

# ans = ''
# for idx in range(len(S)-1):
#     s = ''.join(S[idx:idx+2])
#     if s in num_dict:
#        ans += num_dict[s]
# print(ans)


# 2. 뒤통수가 따가워
# N = int(input())
# N_list = list(map(int, input().split()))
# # 내림차순으로 숫자를 담을 stack
# stack = list()
# ans_list = [0] * N
# # 시간 효율을 위해 len(stack) 대신에 ans로 check
# ans = 0

# for idx in range(N):
#     # 지금까지 내림차순으로 담겨 있는 stack의 길이 -> b를 바라보는 a봉우리 신선의 수
#     ans_list[idx] = ans

#     # stack이 비어있지 않고 가장 위의 숫자가 N_list[idx]보다 작거나 같은 경우 -> 가려지는 경우
#     while stack and stack[-1] <= N_list[idx]:
#         stack.pop()
#         ans -= 1

#     # 해당 idx의 신선 수 1추가
#     stack.append(N_list[idx])
#     ans += 1

# print(*ans_list)


# 3. 직사각형 만들기
# (a^2) > (a+b) * (a-b) == (a^2) - (b^2)
# 즉 정사각형이거나 정사각형에 가까울수록 넓이가 크다
# from collections import defaultdict
# N = int(input())
# N_list = list(map(int, input().split()))

# cnt = defaultdict(int)
# for n in N_list:
#     cnt[n] += 1
# cnt = sorted(cnt.items(), key=lambda x:(-x[0]))
# # print(cnt)

# # 2개의 n을 가진 w를 저장할 변수
# w_two_n = -1
# ans = 0

# for w, n in cnt:
#     # print(w, n)

#     # 직사각형이라 최소 2개는 있어야 함
#     if n >= 2:
#         # 기존에 2개의 n을 가진 w가 있는 경우(a, b 각 한 쌍 중에 하나는 충족이 된 경우)
#         if w_two_n != -1:
#             n -= 2
#             ans += (w * w_two_n)
#             w_two_n = -1

#         # 2개 빼고도 4의 배수 개 이상 남은 경우 (시간 효율을 고려한 코드)
#         if n >= 4:
#             # 막대기 4개당 직사각형 1개
#             ans += (w**2) * (n//4)
#             n %= 4

#         # 위 과정을 거치고 2개 이상 남은 경우
#         if n >= 2:
#             # if w_two_n != -1:
#             #     ans += (w * w_two_n)
#             #     w_two_n = -1
#             w_two_n = w

# print(ans)


# 4. 구름나라 청소하기
# graph + dp
# import sys
# input = sys.stdin.readline
# from collections import defaultdict
# from collections import deque

# N, K = map(int, input().split())
# g = defaultdict(list)
# for _ in range(N-1):
#     u, v = map(int, input().split())
#     g[u].append(v)
#     g[v].append(u)
# # print(g)

# trash = [0] + list(map(int, input().split()))
# # print(trash)
# que = deque([1])
# sum_trash = [0] * (N+1)
# sum_trash[1] = trash[1]
# max_trash = trash[1]

# # BFS
# while que:
#     u = que.popleft()
#     for v in g[u]:
#         # print(u, v)
#         if sum_trash[v] == 0:
#             tmp_sum_trash = sum_trash[u] + trash[v]
#             # 쓰레기 봉투 조건에 충족하는 경우
#             if tmp_sum_trash <= K:
#                 sum_trash[v] = tmp_sum_trash
#                 print(sum_trash)
#                 if max_trash < tmp_sum_trash:
#                     max_trash = tmp_sum_trash
#                 que.append(v)

# print(max_trash)

# import sys
# input = sys.stdin.readline
# from collections import defaultdict
# from collections import deque

# N, K = map(int, input().split())
# g = defaultdict(list)
# for _ in range(N-1):
#     u, v = map(int, input().split())
#     g[u].append(v)
#     g[v].append(u)
# # print(g)

# trash = [0] + list(map(int, input().split()))
# # print(trash)

# # 지금까지 가능한 모든 trash_sum의 경우의 수
# if trash[1] <= K:
#     trash_sum = set({trash[1]})
# else:
#     trash_sum = set({0})
# # print(trash_sum)

# que = deque([1])
# visited = [False] * (N+1)
# visited[1] = True

# # BFS
# while que:
#     u = que.popleft()
#     for v in g[u]:
#         if not visited[v]:
#             visited[v] = True
#             tmp_set = set()

#             for t in trash_sum:
#                 tmp_trash_sum = t + trash[v]
#                 if tmp_trash_sum not in trash_sum and tmp_trash_sum <= K:
#                     tmp_set.add(tmp_trash_sum)
#             for t in tmp_set:
#                 trash_sum.add(t)
#             que.append(v)

# print(max(trash_sum))

# a_set = set({1, 4, 2})
# # print(max(a_set))
# for a in a_set:
#     print(a)

# import sys
# input = sys.stdin.readline
# from collections import defaultdict
# from collections import deque

# N, K = map(int, input().split())
# g = defaultdict(list)
# for _ in range(N-1):
#     u, v = map(int, input().split())
#     g[u].append(v)
#     g[v].append(u)
# # print(g)

# trash = [0] + list(map(int, input().split()))
# # print(trash)

# # 지금까지 가능한 모든 trash_sum의 경우의 수
# if trash[1] <= K:
#     trash_set = set({trash[1]})
# else:
#     trash_set = set({0})
# # print(trash_sum)

# que = deque([[1, trash_set]])
# # print(que.pop())
# visited = [False] * (N+1)
# visited[1] = True
# max_val = 0

# # # BFS
# while que:
#     u, trash_set = que.popleft()
#     backup_set = trash_set

#     if max_val < max(trash_set):
#         max_val = max(trash_set)

#     for v in g[u]:
#         trash_set = backup_set
#         if not visited[v]:
#             visited[v] = True
#             tmp_trash_set = set()

#             for t in trash_set:
#                 tmp_trash = t + trash[v]
#                 if tmp_trash not in trash_set and tmp_trash <= K:
#                     tmp_trash_set.add(tmp_trash)
            
#             for t in tmp_trash_set:
#                 trash_set.add(t)
#             que.append([v, trash_set])

# print(max_val)


# 복습

# 3번 직사각형 만들기
# import sys
# input = sys.stdin.readline

# N = int(input())
# pair = []
# cnt = [0 for _ in range(int(1e6)+1)]
# sticks = map(int, input().split())
# for stick in sticks:
#     cnt[stick] += 1

# for length in range(1, int(1e6)+1):
#     while cnt[length] > 1:
#         cnt[length] -= 2
#         pair.append(length)

# pair.sort(reverse=True)
# # print(pair)

# ans = 0
# for i in range(1, len(pair), 2):
#     ans += pair[i - 1] * pair[i]

# print(ans)


# 4 구름나라 청소하기
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(1234)

# G = [[] for _ in range(1004)]

# N, K = map(int, input().split())
# for _ in range(1, N):
# 	u, v = map(int, input().split())
# 	G[u].append(v)
# 	G[v].append(u)
	
# A = [0] + list(map(int, input().split()))
# dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
# can = [0 for _ in range(K + 1)]

# def DFS(cur, prev):
# 	global K
# 	for i in range(K + 1):
# 		if not dp[prev][i]:
# 			continue
# 		can[i] = dp[cur][i] = 1
# 		if i + A[cur] <= K:
# 			can[i + A[cur]] = dp[cur][i + A[cur]] = 1
# 	for next in G[cur]:
# 		if next == prev:
# 			continue
# 		DFS(next, cur)
		
# dp[0][0] = 1
# DFS(1, 0)
# for i in range(K, -1, -1):
# 	if can[i]:
# 		print(i)
# 		exit(0)