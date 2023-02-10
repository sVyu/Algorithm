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


# def solution(N, number):
#     if N == number:
#         return 1

#     # 0 ~ 8 
#     dp = [set() for _ in range(9)]
#     dp[1].add(N)
#     # print(dp)

#     for idx in range(2, 9):
#         l, r = 1, idx-1
#         tmp_set = set()
#         while l <= r:
#             for nl in dp[l]:
#                 for nr in dp[r]:
#                     dp[idx].add(nr+nl)
#                     dp[idx].add(nr*nl)

#                     tmp_set.add(nr-nl)
#                     dp[idx].add(nr-nl)

#                     if nl != 0:
#                         tmp_set.add(nr//nl)
#                         dp[idx].add(nr//nl)

#             l +=1
#             r -= 1

#         for n in tmp_set:
#             dp[idx].add(-n)
#         max_val = int(str(N)*idx)
#         dp[idx].add(max_val)
#         dp[idx].add(-max_val)

#         if number in dp[idx]:
#             return idx

#     print(dp)
#     # 없네 ..!
#     # tmp_set = set()
#     # for i in dp[4]:
#     #     for j in dp[4]:
#     #         if j == 0:
#     #             continue
#     #         if i//j not in dp[8]:
#     #             tmp_set.add(i//j)
#     # print(tmp_set)

#     return -1

# print(solution(5, 12))
# print(solution(2, 11))

# print(solution(5, 110))
# print(solution(5, 5))
# print(solution(4, 52))
# print(solution(4, 3))
# print(solution(3, 2))
# print(solution(6, -555555555))
# print(solution(6,20))
# print(solution(4, 17))


# 좀 더 개운한 코드
# 상단의 정답 코드에서 dp[3] 원소에서 dp[5] 원소를 나눈 값이 dp[8]에 없을 수 있나 했는데 다 있었음
# 그래도 혹시 몰라 모든 경우를 상정해서 개선
# def solution(N, number):
#     if N == number:
#         return 1

#     # 0 ~ 8 
#     dp = [set() for _ in range(9)]
#     dp[1].add(N)
#     # print(dp)

#     for idx in range(2, 9):
#         for l in range(1, idx):
#             r = idx-l
#             for nl in dp[l]:
#                 for nr in dp[r]:
#                     if r >= l:
#                         dp[idx].add(nr+nl)
#                         dp[idx].add(nr*nl)

#                     dp[idx].add(nr-nl)
#                     if nl != 0:
#                         dp[idx].add(nr//nl)
#                         dp[idx].add(-nr//nl)

#         max_val = int(str(N)*idx)
#         dp[idx].add(max_val)
#         dp[idx].add(-max_val)

#         # print(dp[idx])
#         if number in dp[idx]:
#             return idx

#     return -1

# print(solution(6, 5))


# 구 코드
# def num_111(N, i):
#     now_num = 1
#     return_val = 0
#     while i > 0:
#         return_val += now_num * N
#         now_num *= 10
#         i -= 1
#     return return_val

# def solution(N, number):
#     if N == number:
#         return 1

#     # 0 ~ 8 
#     dp = [set() for _ in range(9)]
#     dp[0].add(0)
#     dp[1].add(0)
#     dp[1].add(N)
#     # print(dp)

#     len_dp = len(dp)
#     for idx in range(2, len_dp):
#         l, r = 1, idx-1
#         while l <= r:
#             for nl in dp[l]:
#                 for nr in dp[r]:
#                     dp[idx].add(nr+nl)
#                     dp[idx].add(nr*nl)
#                     if nr >= nl:
#                         dp[idx].add(nr-nl)
#                     if nl != 0:
#                         dp[idx].add(nr//nl)
#             l +=1
#             r -= 1

#         dp[idx].add(num_111(N, idx))
#         if number in dp[idx]:
#             print(dp)
#             return idx

#     return -1

# print(solution(4, 65))
# print(solution(4, 3))
# print(solution(6, 5))
