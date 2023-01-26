# 2023/01/25
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))

#     odd_cnt = 0
#     odd_idx = set()
#     even_cnt = 0
#     even_idx = set()

#     for idx in range(n):
#         ai = a[idx]
#         # print(ai, idx)
#         if ai % 2 == 0:
#             even_cnt += 1
#             even_idx.add(idx+1)
#         else:
#             odd_cnt += 1
#             odd_idx.add(idx+1)

#     if odd_cnt >= 3:
#         print("YES")
#         for _ in range(3):
#             print(odd_idx.pop(), end=' ')
#     elif odd_cnt >= 1 and even_cnt >= 2:
#         print("YES")
#         print(odd_idx.pop(), end=' ')
#         for _ in range(2):
#             print(even_idx.pop(), end=' ')
#     else:
#         print("NO", end='')
#     print()


'''
3
8 5 7
1
'''
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))

#     sum_a = sum(a)
#     ans = 1

#     found = False
#     for div_num in range(sum_a//2, 1, -1):
#         if sum_a % div_num == 0:
#             cnt_b = 0
#             now_b = 0

#             for ai in a:
#                 now_b += ai
#                 # if now_b % quo == 0:
#                 if now_b % div_num == 0:
#                     cnt_b += 1
#                     now_b = 0

#                 if cnt_b >= 2:
#                     found = True
#                     ans = div_num
#                     break

#             if found:
#                 break

#     print(ans)


# B, after_contest
# import sys
# input = sys.stdin.readline

# def gcd(a, b):
#     while b > 0:
#         a, b = b, a%b
#     return a

# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))

#     sum_a = sum(a)
#     ans, pref = 0, 0

#     for i in range(n-1):
#         pref += a[i]
#         ans = max(ans, gcd(pref, sum_a - pref))

#     print(ans)