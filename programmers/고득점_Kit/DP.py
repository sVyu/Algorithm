# N으로 표현
# 집합으로 가능할 듯 ?


# 정수 삼각형
# def solution(triangle):
#     n = len(triangle)
#     dp = [[0]*n for _ in range(n)]

#     dp[0][0] = triangle[0][0]
#     for x in range(n-1):
#         for y in range(x+1):
#             for k in range(2):
#                 dp[x+1][y+k] = max(dp[x+1][y+k], dp[x][y]+triangle[x+1][y+k])

#     return max(dp[n-1])

# print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))


# 등굣길
# def solution(m, n, puddles):
#     dp = [[0]*(n+1) for _ in range(m+1)]
#     for p in puddles:
#         dp[p[0]][p[1]] = -1
#     dp[1][1] = 1

#     mod = int(1e9)+7

#     for x in range(1, m+1):
#         for y in range(1, n+1):
#             if dp[x][y] == -1:
#                 continue

#             if dp[x-1][y] != -1:
#                 dp[x][y] += dp[x-1][y]

#             if dp[x][y-1] != -1:
#                 dp[x][y] += dp[x][y-1]

#             dp[x][y] %= mod

#     # for x in range(m+1):
#     #     print(dp[x])

#     return dp[m][n]

# print(solution(4, 3, [[2, 2]]))

# print(solution(4, 3, [[2, 2], [1, 2], [3, 2]]))


# N으로 표현

# def solution(N, number):
#     n_set = set({0})
#     cnt = 0
#     new_num = 0
#     while cnt < 8:
#         tmp_n_set = set()
#         for n in n_set:
#             if n + N not in n_set:
#                 tmp_n_set.add(n+N)
#             if n - N not in n_set and n - N > 0:
#                 tmp_n_set.add(n-N)
#             if n * N not in n_set:
#                 tmp_n_set.add(n*N)
#             if n // N not in n_set:
#                 tmp_n_set.add(n//N)

#         for n in tmp_n_set:
#             n_set.add(n)

#         new_num += (10**cnt)*N
#         n_set.add(new_num)

#         cnt += 1
#         # print(cnt, n_set)
#         if number in n_set:
#             return cnt

#     return -1

# # print(solution(5, 12))
# # print(solution(2, 11))
# # print(solution(5, -1))
# print(solution(5, 110))