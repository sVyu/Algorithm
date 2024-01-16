# 2023 건국대학교 프로그래밍 경진대회 (KUPC) Open Contest · Arena #10

# A
# import sys
# input = sys.stdin.readline

# N, L = map(int, input().split())
# max_cnt, how_many = 0, 0
# for _ in range(N):
#     ss = list(map(int, input().rstrip()))
#     # print(ss)

#     cnt = 0
#     pre_color = -1
#     for s in ss:
#         if pre_color != s:
#             if s == 1:
#                 cnt += 1
#         pre_color = s

#     if max_cnt < cnt:
#         max_cnt = cnt
#         how_many = 1
#     elif max_cnt == cnt:
#         how_many += 1

# print(max_cnt, how_many)


# B
# print('Goose' if int(input()) % 2 else 'Duck')


# C
# N, L = map(int, input().split())
# print(''.join(['1' for _ in range(L-1)])+str(N))


# D
# N = int(input())
# ns = sorted(list(map(int, input().split())))
# # print(ns)

# check = [False]*N
# ans = 0

# pre = -1
# for i in range(N):
#     if pre < ns[i] and not check[i]:
#         pre = ns[i]
#         check[i] = True
#         ans += 1

# pre = -1
# for i in range(N):
#     if pre < ns[i] and not check[i]:
#         pre = ns[i]
#         check[i] = True
#         ans += 1

# print(ans)


# E
# import sys
# input = sys.stdin.readline

# N = int(input())
# ss = list(input().rstrip())

# left, right = [0]*26, [0]*26
# for i in range(N//2):
#     left[ord(ss[i])-97] += 1

# for j in range(-(N//2), 0, 1):
#     right[ord(ss[j])-97] += 1

# pos = True
# for i in range(26):
#     if (left[i]+right[i]) % 2:
#         pos = False
#         break

# print('Yes' if pos else 'No')


# F
# import sys
# input = sys.stdin.readline

# N, M, R = map(int, input().split())
# ns = sorted(list(map(int, input().split())))
# ms = list(map(int, input().split()))

# ans = -1
# for m in ms:
#     l, r = 0, 1
#     while l <= r:
#         base = ns[r]-ns[l]
#         s = base*m/2

#         if s <= R:
#             ans = max(ans, s)
#             r += 1
#             if r >= N:
#                 break
#         else:
#             l += 1

# print('{:.1f}'.format(ans) if ans > 0 else -1)


# G
# N = int(input())
# ns = list(map(int, input().split()))
# new_ns = [max(0, sum(ns[i:min(N, i+3)])) for i in range(N)]
# # print(new_ns)

# dp = [0]*N
# dp[:3] = new_ns[:3]

# for i in range(3, N):
#     dp[i] = max(dp[max(0, i-5):i-2])+new_ns[i]

# print(sum(ns)+max(dp[-3:]))


# H 
# import sys
# input = sys.stdin.readline

# N, M, Q = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# new_board = [[0]*M for _ in range(N)]

# for y in range(M):
#     for x in range(N):
#         new_board[x][y] = board[x][y] #
#         if x >= 1:
#             new_board[x][y] += new_board[x-1][y]

# # for x in range(N):
# #     print(new_board[x])

# diag_board = [[0]*M for _ in range(N)]
# for x_std in range(N):
#     y = 0
#     for x in range(x_std, N):
#         diag_board[x][y] = new_board[x][y]
#         if x > 0 and y > 0:
#             diag_board[x][y] += diag_board[x-1][y-1]
        
#         y += 1
#         if y >= M: break

# for y_std in range(M):
#     x = 0
#     for y in range(y_std, M):
#         diag_board[x][y] = new_board[x][y]
#         if x > 0 and y > 0:
#             diag_board[x][y] += diag_board[x-1][y-1]

#         x += 1
#         if x >= N: break

# # for x in range(N):
# #     print(diag_board[x])

# for _ in range(Q):
#     x, y = map(int, input().split())
#     print(diag_board[x-1][y-1])


# I
'''
5
3 3 10 2 1
'''
# import sys
# sys.setrecursionlimit(int(1e6))

# N = int(input())
# ns = list(map(int, input().split()))
# left, right, right_end = [[0, 0]]*N, [0]*N, [0]*N

# def right_dfs(i):
#     if i == N-1:
#         return 0
#     elif i > N-1:
#         return 0
#     elif right[i] >= 0:
#         return_sec = right_dfs(i+ns[i])
#         right[i] = (return_sec+1) if return_sec >= 0 else -1

#     return right[i]

# def right_end_dfs(i):
#     if i == N-1:
#         return 0
#     elif i > N-1:
#         return -1
#     elif right_end[i] >= 0:
#         return_sec = right_end_dfs(i+ns[i])
#         right_end[i] = (return_sec+1) if return_sec >= 0 else -1

#     return right_end[i]

# for i in range(N-1):
#     right_dfs(i)
#     right_end_dfs(i)
# # print(right)
# # print(right_end)

# def left_dfs(i):
#     if i == 0:
#         return [0, 0]
#     elif i < 0:
#         return [-1, -1]
#     elif left[i] == [0, 0]:
#         sec, x = left_dfs(i-ns[i])
#         left[i] = [(sec+1), x] if x >= 0 else [-1, -1]

#     return left[i]

# for i in range(N-2, -1, -1):
#     left_dfs(i)
# # print(left)


# 12713 Ugly Numbers (Small)
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(int(3^13)+1)

# global ans
# ans = 0
# N = int(input())

# def btr(ss, idx, sign, tmp_s, tot_sum, len_ss):
#     global ans
#     if idx >= len_ss:
#         # print('aa', tot_sum, sign, tmp_s)
#         tot_sum += sign*tmp_s
#         # print("now", tot_sum)
#         for n in [2, 3, 5, 7]:
#             if (not tot_sum) or (tot_sum % n == 0):
#                 ans += 1
#                 return
#     else:
#         btr(ss, idx+1, 1, ss[idx], tot_sum+sign*tmp_s, len_ss)
#         btr(ss, idx+1, -1, ss[idx], tot_sum+sign*tmp_s, len_ss)
#         btr(ss, idx+1, sign, tmp_s*10+ss[idx], tot_sum, len_ss)

# for i in range(1, N+1):
#     ss = list(map(int, input().rstrip()))
#     # print('ss', ss)
#     ans = 0
#     btr(ss, 1, 1, ss[0], 0, len(ss))
#     print(f'Case #{i}: {ans}')