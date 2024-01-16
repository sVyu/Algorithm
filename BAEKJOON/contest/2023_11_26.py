# solved.ac Grand Arena #3 — Division 2 · Arena #13

# N = int(input())
# ns = list(map(int, input().split()))
# T, P = map(int, input().split())

# ans_t = 0
# for n in ns:
#     ans_t += n//T
#     if n % T: ans_t += 1

# print(ans_t)
# print(N//P, N%P)


# B

# import sys
# input = sys.stdin.readline

# N = int(input())
# ns = [0] + list(map(int, input().split()))
# on = [1]*(N+1)
# Q = int(input())

# total_per_min = sum(ns)
# print(total_per_min)
# for _ in range(Q):
#     cmds = list(map(int, input().split()))
#     if cmds[0] == 1:
#         i = cmds[1]
#         total_per_min -= ns[i]*on[i]
#         ns[i] = cmds[2]
#         total_per_min += ns[i]*on[i]
#     else:
#         i = cmds[1]
#         if on[i]:
#             total_per_min -= ns[i]
#             on[i] = 0
#         else:
#             total_per_min += ns[i]
#             on[i] = 1

#     print(total_per_min)


# C
# N = int(input())
# ns = list(map(int, input().split()))
# cnts = [0]*10

# l, r = 0, 0
# cnts[ns[0]] += 1
# kinds = 1

# max_len = 1         # N >= 1
# while l <= r:
#     if kinds <= 2:
#         r += 1
#         if r >= N:
#             break
#         if cnts[ns[r]] == 0:
#             kinds += 1

#         cnts[ns[r]] += 1

#     else:
#         cnts[ns[l]] -= 1
#         if cnts[ns[l]] == 0:
#             kinds -= 1
#         l += 1

#     if kinds <= 2:
#         max_len = max(max_len, r-l+1)

# print(max_len)


# D
'''
10
1 9 8 7 6 5 4 3 2 8
10
8 9 7 6 5 4 3 2 8 5
[t]
2
9 8
'''
'''
5
1 2 3 5 2
2
2 2
[t]
3
2 2 2
'''
'''
3
3 3 7
3 
3 7 3
[t]
2
3 3
'''
'''
3
7 7 7
3
7 7 7
[t]
2
2 2
'''

# N = int(input())
# ns = list(map(int, input().split()))
# M = int(input())
# ms = list(map(int, input().split()))
# m_each_num_idxs = [[] for _ in range(101)]
# for i in range(M):
#     m_each_num_idxs[ms[i]].append(i) 
# # print(m_each_num_idxs[:10])

# set_ns = set(ns)
# set_ms = set(ms)

# # common_set
# c_set = set_ns.intersection(set_ms)
# cs = [False]*101
# for c in c_set:
#     cs[c] = True
# # print(cs[:10])

# m_idxs = []
# ans = []
# for n in ns:
#     if cs[n]:
#         for mi in range(M):
#             if ms[mi] == n:
#                 if ans:
#                     find = False

#                     tmp_ans, tmp_m_idxs = [], []
#                     while ans and ans[-1] < n:
#                         tmp_ans.append(ans.pop())
#                         tmp_m_idxs.append(m_idxs.pop())

#                     # n을 조건에 부합해서 ans에 이어붙일 수 있다면 true
#                     # 이분탐색 가능
#                     for i in m_each_num_idxs[n]:
#                         if m_idxs:
#                             if i > m_idxs[-1]:
#                                 find = True
#                                 break
#                         else:
#                             find = True
#                             break

#                     if find:
#                         ans.append(n)
#                         m_idxs.append(i)
#                     else:
#                         while tmp_ans:
#                             ans.append(tmp_ans.pop())
#                             m_idxs.append(tmp_m_idxs.pop())
#                 else:
#                     ans.append(n)
#                     m_idxs.append(mi)
#                 break

# print(len(ans))
# if ans:
#     print(*ans)


