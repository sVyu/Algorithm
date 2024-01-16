# 솔브드 아레나로 대회를 열고 싶었으나 실패해서 그냥 여는 대회

# B번 - 현이의 로봇 청소기
# from collections import deque

# N, M, K = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# visited = [[False]*M for _ in range(N)]
# inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# ans = 0
# for x in range(N):
#     for y in range(M):
#         if not visited[x][y]:
#             ans += 1
#             visited[x][y] = True
#             q = deque([[x, y]])

#             while q:
#                 tx, ty = q.popleft()
#                 for px, py in inc_xy:
#                     nx, ny = tx+px, ty+py
#                     if 0 <= nx < N and 0 <= ny < M and\
#                         not visited[nx][ny] and abs(board[tx][ty]-board[nx][ny]) <= K:
#                         q.append([nx, ny])
#                         visited[nx][ny] = True

# print(ans)


# C번 - 좋은 배열 만들기
'''
5
1 1 1 1 2
'''
# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# N = int(input().rstrip())
# ns = sorted(list(map(int, input().rstrip().split())))
# sum_ns = sum(ns)
# # print(sum_ns)

# # cnts = [0]*1000001
# cnts = defaultdict(int)

# for n in ns:
#     cnts[n] += 1

# ans = 0
# for i in range(N-1):
#     val = ns[i]
#     cnts[val] -= 1
#     if (i == N-2):
#         if (sum_ns-sum(ns[-2:])) == (2*ns[-3]):
#             ans += 1
#     else:
#         # 맨 마지막 값이 나머지 값들의 합일 때
#         res = (sum_ns-val-(2*ns[-1]))
#         if res >= 0:
#             ans += cnts[res]

#         # 마지막에서 두 번째 값이 나머지 값들의 합일 때 (마지막 값 제외)
#         res = (sum_ns-val-ns[-1])
#         if res == (ns[-2]*2):
#             ans += 1

# print(ans)


# A번 시루의 산책

# 시작점이 하나거나 중복 좌표가 있거나
# 처음부터 차지할 수는 없는데 추가로 얻는 좌표 중에 중복 좌표가 있어서 index로 계산해야한다면?

# import sys
# input = sys.stdin.readline
# from collections import deque

# N, M = map(int, input().split())
# xys = [list(map(int, input().split())) + [i] for i in range(N)]
# ps = list(map(int, input().split()))
# rs = list(map(int, input().split()))
# # print(xys)

# pre_marked_xy_set = set()
# for i in range(M):
#     x, y, idx = xys[ps[i]-1]
#     pre_marked_xy_set.add(tuple([x, y, idx]))

#     for tx, ty, tidx in xys:
#         if ((tx-x)**2 + (ty-y)**2) <= (rs[i+1]**2):
#             pre_marked_xy_set.add(tuple([tx, ty, tidx]))
# # print(pre_marked_xy_set)

# ans = 0
# q = deque()
# visited = set()
# for x, y, idx in xys:
#     tuple_xy = tuple([x, y, idx])
#     if (tuple_xy not in pre_marked_xy_set):
#         ans += 1
#         q.append(tuple_xy)
#         visited.add(tuple_xy)
# # print(visited)

# while q:
#     x, y, _ = q.popleft()

#     for tx, ty, tidx in xys:
#         tuple_txy = tuple([tx, ty, tidx])
#         if (tuple_txy not in visited) and (((tx-x)**2+(ty-y)**2) <= (rs[0]**2)):
#             ans += 1
#             q.append(tuple_txy)
#             visited.add(tuple_txy)

# print(ans)


# 시루의 산책 - 삽질
# import sys
# input = sys.stdin.readline
# from collections import deque

# N, M = map(int, input().split())
# xys = [list(map(int, input().split())) for _ in range(N)]
# ps = list(map(int, input().split()))
# rs = list(map(int, input().split()))

# pre_marked_xy_set = set()
# for i in range(M):
#     x, y = xys[ps[i]-1]
#     pre_marked_xy_set.add(tuple([x, y]))

#     for tx, ty in xys:
#         if ((tx-x)**2 + (ty-y)**2) <= (rs[i+1]**2):
#             pre_marked_xy_set.add(tuple([tx, ty]))

# sirus_xys = []
# for x, y in xys:
#     tuple_xy = tuple([x, y])
#     if (tuple_xy not in pre_marked_xy_set):
#         sirus_xys.append(tuple_xy)

# max_cnt = 0
# visited = set()
# for x, y in sirus_xys:
#     if tuple([x, y]) in visited:
#         continue

#     cnt = 1
#     q = deque([[x, y]])
#     visited.add(tuple([x, y]))
#     while q:
#         tx, ty = q.popleft()
#         for nx, ny in xys:
#             tuple_nxy = tuple([nx, ny])
#             if (tuple_nxy not in visited) and (((tx-nx)**2+(ty-ny)**2) <= rs[0]**2):
#                 q.append(tuple_nxy)
#                 visited.add(tuple_nxy)
#                 cnt += 1

#     max_cnt = max(max_cnt, cnt)
# print(max_cnt)