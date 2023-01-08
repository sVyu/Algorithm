# A. Make it Beautiful
# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# for _ in range(int(input())):
#     n = int(input())
#     a = sorted(list(map(int, input().split())), reverse=True)

#     if a[0] != a[1] or (a[0] == a[1] and a[1] != a[-1]):
#         print("YES")
#         a[1], a[-1] = a[-1], a[1]
#         print(*a)
#     else:
#         print("NO")

# B. Matrix of Differences
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n = int(input())
#     board = [[0]*n for _ in range(n)]

#     k = n**2 - 1
#     mul_val = 1
#     x, y = 0, 0
#     go_x = 1 # delta_x
#     pre_val = board[0][0] = 1

#     while k >= 1:
#         x += go_x
#         # print("x, y", x, y)
#         pre_val = board[x][y] = pre_val + (k * mul_val)
#         mul_val *= -1
#         k -= 1

#         # for aa in range(n):
#         #     print(board[aa])

#         # if x go outside
#         if (x + go_x) < 0 or (x + go_x) > n-1:
#             x += go_x
#             go_x *= -1
#             y += 1

#     for x in range(n):
#         print(*board[x])


# C. Yet Another Tournament

# D. Different Arrays
# from collections import defaultdict
# n = int(input())
# a = list(map(int, input().split()))

# # n : 5 -> to a[3]
# dp = [1] * (n)

# next_num = defaultdict(int)
# next_num[a[1]] += 1

# for idx in range(1, n-1):
#     # print(next_num)
#     how_many_zero = next_num[0]
#     dp[idx] = 2*dp[idx-1] - how_many_zero

#     check = False
#     new_next_num = defaultdict(int)
#     for num, val in next_num.items():
#         if num == 0:
#             check = True
#         else:
#             new_next_num[a[idx+1]+num] += val
#             new_next_num[a[idx+1]-num] += val
    
#     if check:
#         new_next_num[0] += 1
#     next_num = new_next_num
#     # print(idx, next_num, idx+1)

# # print(dp)
# print(dp[n-2] % 998244353)