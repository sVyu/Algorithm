# 1. UXUI 디자이너
# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# N, M = map(int, input().split())
# num_dict = defaultdict(int)

# for _ in range(M):
#     event = list(map(int, input().split()))
#     for i in range(event[0]):
#         num_dict[event[i+1]] += 1

# # print(num_dict)
# ans = sorted(num_dict.items(), key=lambda x:(-x[1], -x[0]))
# for a in ans:
#     if a[1] == ans[0][1]:
#         print(a[0], end=' ')
#     else:
#         break


# 2. 퍼져나가는 소문
# import sys
# input = sys.stdin.readline
# from collections import defaultdict
# from collections import deque

# # graph
# g = defaultdict(list)
# N = int(input())
# M = int(input())
# for _ in range(M):
#     u, v = map(int, input().split())
#     g[u].append(v)
#     g[v].append(u)
# # print(g)

# que = deque([1])
# visited = [0] * (N+1)
# visited[1] = 1

# while que:
#     v = que.popleft()
#     for v in g[v]:
#         if visited[v] == 0:
#             que.append(v)
#             visited[v] = 1

# print(sum(visited))


# 구름이의 여행 2
# import sys
# input = sys.stdin.readline
# from collections import defaultdict
# from collections import deque

# N, M, K = map(int, input().split())
# g = defaultdict(list)
# for _ in range(M):
#     a, b = map(int, input().split())
#     g[a].append(b) # 단방향
# # print(g)

# visited = [0] * (N+1)
# que = deque([K])

# ans_check = False
# ans = 0

# while que:
#     ans += 1
#     for _ in range(len(que)):
#         vv = que.popleft()
#         for v in g[vv]:
#             if visited[v] == 0:
#                 # 다음 v가 K인 경우, (다시 돌아온 경우)
#                 if v == K:
#                     ans_check = True
#                     break
                
#                 # 아닌 경우
#                 visited[v] = 1
#                 que.append(v)
#         if ans_check:
#             break
#     if ans_check:
#         break

# if ans_check: print(ans)
# else: print(-1)

# import sys
# input = sys.stdin.readline
# from collections import defaultdict
# from collections import deque

# def solve():
#     N, M, K = map(int, input().split())
#     g = defaultdict(list)
#     for _ in range(M):
#         a, b = map(int, input().split())
#         g[a].append(b) # 단방향
#     # print(g)

#     visited = [0] * (N+1)
#     que = deque([K])

#     ans = 0
#     while que:
#         ans += 1
#         for _ in range(len(que)):
#             vv = que.popleft()
#             for v in g[vv]:
#                 if visited[v] == 0:
#                     # 다음 v가 K인 경우, (다시 돌아온 경우)
#                     if v == K:
#                         print(ans)
#                         return
                    
#                     # 아닌 경우
#                     visited[v] = 1
#                     que.append(v)
#     print(-1)

# solve()


# 4. 이상한 미로
# import sys
# input = sys.stdin.readline
# from collections import defaultdict
# from collections import deque

# N, M = map(int, input().split())
# Ai = list(map(int, input().split())) # 방 바닥에 적혀있는 수
# g = defaultdict(list)
# que = deque([[1, 0]])

# for _ in range(M):
#     u, v, w = map(int, input().split())
#     g[u].append([v, w])
# # print(g)
# # print(que)

# # [v, 나머지] = [걸린 시간]
# g_check = defaultdict(list)

# ans = 1e99
# while que:
#     u, time = que.popleft()
#     for v, w in g[u]:
#         res = u % v
#         key = tuple([v, res])
#         if key in g_check:
#             if time+res < g_check[key]:
#                 g_check[key] = time+res
#                 que.append([v, time+res])
#             else:
#                 continue
#         else: # g_check에 없는 경우
#             g_check[key] = time+res
#             que.append([v, time+res])

# print(g_check)
