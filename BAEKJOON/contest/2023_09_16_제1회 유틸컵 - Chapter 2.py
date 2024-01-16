# 제1회 유틸컵 - Chapter 2

# T
# 한 티어에 0명이 가능한 경우 ?
'''
4 3
c 1
M 50%
k 3

4 2
c 5
d 1
c

4 2
c 5
d 1
d

6 2
c 5
d 2
d

7 2
c 5
d 3
d
'''

# import sys
# input = sys.stdin.readline
# import math

# N, T = map(int, input().split())
# tmp_N = N
# tiers = [list(input().rstrip().split()) for _ in range(T)]
# # print(tiers)

# how_many = [0]*T
# for i in range(T):
#     _, n = tiers[i]

#     if n[-1] == '%':
#         n = (N * int(n[:-1]))//100 #

#     n = int(n)
#     how_many[i] = n
#     N -= n
# # print(how_many) # 되네

# # target
# target = input().rstrip()

# if N > 0:
#     print("Invalid System")
# else:
#     cnts = 0

#     n = -1
#     if target[-1] in "1234":
#         n = int(target[-1])
#         target = target[:-1]
#     # print("target, n ", target, n)

#     for i in range(T):
#         tier = tiers[i][0]
#         if tier != target:
#             cnts += how_many[i]
#         else:
#             if n == -1:
#                 if how_many[i] and cnts+1 <= tmp_N:
#                         print(cnts+1, min(cnts+how_many[i], tmp_N))
#                 else:
#                     print("Liar") # 이 부분이 있었네
#             else:
#                 res_mem = how_many[i]
#                 for k in range(1, 5):
#                     pos_mem = min(math.ceil(how_many[i]/4), res_mem)
#                     res_mem -= pos_mem
#                     # print("res", res_mem)

#                     if k != n:
#                         cnts += pos_mem
#                     else:
#                         if pos_mem and cnts+1 <= tmp_N:
#                             print(cnts+1, min(cnts+pos_mem, tmp_N))
#                         else:
#                             print("Liar")


# K
'''
Korea of Korea
'''
# import sys
# input = sys.stdin.readline

# def check_kor2(ss):
#     sign = ''
#     if ss[-1] in '!?,.':
#         sign = ss[-1]
#         ss = ss[:-1]
#     # print("ss", ss)
#     return [bool(ss == 'Korea'), sign]

# for _ in range(int(input())):
#     ss = list(input().rstrip().split())

#     # 2번
#     next_ss = []
#     len_nss = 0
#     for s in ss:
#         next_ss.append(s)
#         len_nss += 1
#         if len_nss >= 3:
#             is_kor, sign = check_kor2(s)
#             # print("?!?!", s, is_kor, sign)
#             if is_kor and next_ss[-2] == 'of' and (next_ss[-3][-1] not in "!?,."):
#                 for _ in range(2):
#                     next_ss.pop()
#                 target = next_ss.pop()
#                 len_nss -= 2

#                 if 97 <= ord(target[0]) <= 122:
#                     target = chr(ord(target[0])-32)+target[1:]
#                 # print("haha")

#                 next_ss.append('K-'+target+sign)
#     # print(next_ss)

#     ss = next_ss
#     next_ss = []
#     len_nss = 0
#     # 1번
#     for s in ss[::-1]:
#         next_ss.append(s)
#         len_nss += 1
#         if len_nss >= 2:
#             if next_ss[-1] == 'Korea':
#                 next_ss.pop()
#                 target = next_ss.pop()
#                 len_nss -= 1

#                 if 97 <= ord(target[0]) <= 122:
#                     target = chr(ord(target[0])-32)+target[1:]

#                 next_ss.append('K-'+target)

#     print(*next_ss[::-1])