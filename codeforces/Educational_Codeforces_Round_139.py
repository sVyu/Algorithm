# Rated for Div.2
# my_first_codeforces_contest

# A. Extremely Round
# import sys
# input = sys.stdin.readline

# t = int(input())
# nn = [int(input()) for _ in range(t)]
# num_of_extremely_round = [0]*(max(nn)+1)

# total_amount = 0
# for i in range(1, max(nn)+1):
#     num = i
#     extremely_round_check = 0
#     while num > 0 and extremely_round_check < 2:
#         if num % 10 != 0:
#             extremely_round_check += 1
#         num //= 10
    
#     if extremely_round_check == 1:
#         total_amount += 1

#     num_of_extremely_round[i] = total_amount

# for i in range(t):
#     print(num_of_extremely_round[nn[i]])
# # print(num_of_extremely_round)


# B. Notepad#
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n = int(input())
#     s = list(input().rstrip())
#     # print(s)

#     pos = False
#     sub_s_dict = dict()
#     for i in range(n-1):
#         if tuple(s[i:i+2]) not in sub_s_dict:
#             sub_s_dict[tuple(s[i:i+2])] = i
#         else:
#             if sub_s_dict[tuple(s[i:i+2])] == i-1:
#                 continue
#             pos = True
#             break
    
#     if pos: print("YES")
#     else: print("NO")


# C. Hamiltonian Wall
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     m = int(input())
#     wall = [list(map(str, input().rstrip())) for _ in range(2)]
#     # print(wall)

#     for start_r in [0, 1]:
#         pos = True
#         y = 0
#         len_of_row = len(wall[0])
#         r = start_r

#         while y < len_of_row:
#             if wall[r][y] == 'W':
#                 pos = False
#                 break
#             else: # 'B'
#                 if wall[(r+1)%2][y] == 'B':
#                     r = (r+1)%2
#                 y += 1
        
#         if pos:
#             break
    
#     if pos: print("YES")
#     else: print("NO")


# D. Lucky Chains
# import sys
# input = sys.stdin.readline

# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a

# for _ in range(int(input())):
#     ans = 0
#     x, y = map(int, input().split())

#     if abs(x-y) == 1 and min(x, y) > 1:
#         ans = -1
#     else:
#         while True:
#             if gcd(x, y) == 1:
#                 ans += 1
#                 x += 1
#                 y += 1
#             else:
#                 break

#     print(ans)


# E. Decomposition
