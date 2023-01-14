# 보드게임컵
# A번 - 노 땡스!
# N = int(input())
# card = list(map(int, input().split()))

# ans = card[0]
# pre_card = card[0]

# for idx in range(1, N):
#     if card[idx] != pre_card+1:
#         ans += card[idx]

#     pre_card = card[idx]

# print(ans)


# B번 - 할리갈리
# from collections import defaultdict

# fruits = defaultdict(int)
# for _ in range(int(input())):
#     f, n = map(str, input().split())
#     fruits[f] += int(n)

# print("YES" if 5 in fruits.values() else "NO")


# C번 - 크레이지 타임
# import sys
# input = sys.stdin.readline

# alpha = 1
# now_hr = 1
# for _ in range(int(input())):
#     card, n = map(str, input().split())
#     n = int(n)
#     ans = "NO"

#     if card == 'HOURGLASS':
#         if now_hr != n:
#             alpha *= -1
#     else:
#         if now_hr == n:
#             ans = "YES"

#     print(now_hr, ans)
#     now_hr = (now_hr + alpha -1) % 12 +1


# D번 - Yacht Dice
# import itertools
# from collections import defaultdict

# word = ['_'] + list(input())
# # print(word)
# fixed_dices = list(map(int, input().split()))
# dices_dict = defaultdict(int)
# for dice in fixed_dices:
#     dices_dict[dice] += 1
# # print(dices_dict)
# max_ans = 0

# for new_dices in itertools.combinations_with_replacement(range(1, 7), 2):
#     # print(new_dices)
#     tmp_dices_dict = dices_dict.copy()

#     for dice in new_dices:
#         tmp_dices_dict[dice] += 1
#     # print(tmp_dices_dict)

#     ans = 0
#     # 1 ~ 6
#     for i in range(1, 7):
#         if word[i] == 'Y':
#             ans = max(ans, i*tmp_dices_dict[i])

#     # 7 - Four of a Kind
#     if word[7] == 'Y':
#         for i in range(1, 7):
#             if tmp_dices_dict[i] >= 4:
#                 ans = max(ans, 4*i)

#     # 8 - Full House
#     if word[8] == 'Y':
#         triple_check, double_check = False, False
#         triple_num, double_num = -1, -1
#         for i in range(1, 7):
#             if tmp_dices_dict[i] == 3:
#                 triple_check = True
#                 triple_num = i
#             elif tmp_dices_dict[i] == 2:
#                 double_check = True
#                 double_num = i

#         if triple_check and double_check:
#             ans = max(ans, 3*triple_num + 2*double_num)

#     # 9, 10:
#     if tmp_dices_dict[2] == 1 and tmp_dices_dict[3] == 1 and\
#         tmp_dices_dict[4] == 1 and tmp_dices_dict[5] == 1:
#         if word[9] == 'Y' and tmp_dices_dict[1] == 1:
#             ans = max(ans, 30)
#         if word[10] == 'Y' and tmp_dices_dict[6] == 1:
#             ans = max(ans, 30)

#     # 11
#     if word[11] == 'Y':
#         for i in range(1, 7):
#             if tmp_dices_dict[i] == 5:
#                 ans = max(ans, 50)

#     # 12
#     if word[12] == 'Y':
#         # ans = max(ans, sum(tmp_dices_dict.values()))
#         sum_of_vals = 0
#         for key, val in tmp_dices_dict.items():
#             sum_of_vals += key*val
#         ans = max(ans, sum_of_vals)

#     max_ans = max(max_ans, ans)

# print(max_ans)


# N번 - 수 나누기 게임
# N = int(input())
# n = list(map(int, input().split()))
# new_n = sorted(n)
# n_set = set(n)

# sieve_n = [0] * (new_n[-1]+1)
# len_sieve_n = len(sieve_n)

# for k in n:
#     # if sieve_n[k] == 0:
#     for kk in range(2*k , len_sieve_n, k):
#         sieve_n[kk] -= 1
#         if kk in n_set:
#             sieve_n[k] += 1

# # print(sieve_n)
# print(*[sieve_n[i] for i in n])


# # ans = 0
# # for i in range(1, 1000000):
# #     ans += 1000000//i
# # print(ans) # 13970033


# G번 - 모든 곳을 안전하게
'''
5
2 0 0 0 3 1
1
NO
'''
# n = int(input())
# a = list(map(int, input().split()))
# x = int(input())

# odd_num_set = set()
# num_set = set()

# for idx in range(n+1):
#     if a[idx] == 1:
#         odd_num_set.add(idx)

#     if a[idx] != 0:
#         num_set.add(idx)
# # print(odd_num_set)
# # print(num_set)

# pos = False
# pos_num = []

# if len(odd_num_set) == 2:
#     odd_num_list = sorted(list(odd_num_set))
#     if odd_num_list[0] + x == odd_num_list[1]:
#         pos = True
#         pos_num = odd_num_list

# elif len(odd_num_set) == 1:
#     odd_num = odd_num_set.pop()
#     if odd_num + x in num_set:
#         pos = True
#         pos_num = [odd_num, odd_num + x]

# elif len(odd_num_set) == 0:
#     for k in num_set:
#         if a[k] >= 3 and k + x in num_set:
#             pos = True
#             pos_num = [k, k+x]
#             break

# print("YES" if pos else "NO")
# print(*pos_num if pos else "", end = '')