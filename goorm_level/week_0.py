# 1. 단어장 만들기
# sort 순서
# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# n_list = [input().rstrip() for _ in range(n)]
# n_list.sort()
# n_list = sorted(n_list, key=lambda x:(len(x)))
# # n_list = sorted(n_list, key=lambda x:(len(x), x[0]))
# print(n_list[k-1])


# 2. 카드 교환하기
# import sys
# input = sys.stdin.readline
# from collections import defaultdict
# from collections import deque

# N, M = map(int, input().split())
# C = [0] + list(map(int, input().split()))
# g = defaultdict(list)
# for _ in range(M):
#     u, v = map(int, input().split())
#     g[u].append(v)
#     g[v].append(u)
# # print(g)

# visited = [False] * (N+1)
# ans = 0

# for i in range(1, N+1):
#     v_list = list()
#     c_list = list()
    
#     if not visited[i]:
#         # print("v", i)
#         visited[i] = True
#         v_list.append(i)
#         c_list.append(C[i])
#         que = deque([i])

#         while que:
#             u = que.popleft()
#             for v in g[u]:
#                 if not visited[v]:
#                     visited[v] = True
#                     que.append(v)
#                     v_list.append(v)
#                     c_list.append(C[v])

#         v_list.sort()
#         c_list.sort()

#         for i in range(len(v_list)):
#             ans += abs(v_list[i] - c_list[i])

# print(ans)