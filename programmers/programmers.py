# def solution(d, budget):
#     import itertools
    
#     if sum(d) < budget:
#         return len(d)
    
#     d.sort()
#     for k in range(len(d), 0, -1):
#         sum_val = sum(d[:k])
#         if budget == sum_val:
#             return k
#         elif budget > sum_val:
#             for ex_combination in itertools.combinations(d, k):
#                 if budget == sum(ex_combination):
#                     return k

#     return 0

# 프로그래머스 예산
# def backtracking(d, len_d, budget, idx, k):
#     global val, ans
#     for now_idx in range(idx, len_d):
#         k += 1
#         val += d[now_idx]
#         # print(val, k, now_idx)
#         if val == budget:
#             ans = k
#             break
#         elif now_idx < len_d-1 and val < budget: # val < budget
#             backtracking(d, len_d, budget, now_idx+1, k)
#         if ans != 0:
#             break
#         val -= d[now_idx]
#         k -= 1

# def solution(d=[1,3,2,5,4], budget=9):
#     d.sort()

#     global val, ans
#     val, ans = 0, 0
    
#     backtracking(d, len(d), budget, 0, 0)
#     print(ans)

# solution()


# def solution(skill = "CBD", skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]):
#     answer = 0
    
#     skill_alpha = [0] * len(skill)
#     for idx in range(len(skill)):
#         skill_alpha[idx] = ord(skill[idx])-65
    
#     for skill_tree in skill_trees:
#         alpha_idx = [26] * 26
#         for idx in range(len(skill_tree)):
#             alpha_idx[ord(skill_tree[idx])-65] = idx
    
#         check = True
#         for idx in range(1, len(skill)):
#             if alpha_idx[skill_alpha[idx-1]] > alpha_idx[skill_alpha[idx]]:
#                 check = False
#                 break
#         if check: answer +=1
#     return answer

# print(solution())


# def solution(dirs="LULLLLLLU"):
#     answer = 0
#     d_dict = dict({'U':[-1, 0], 'L':[0, -1], 'R':[0, 1], 'D':[1, 0]})
#     p_set = set()
#     x, y = 0, 0
    
#     for d in dirs:
#         plus_x, plus_y = d_dict[d]
#         next_x = x + plus_x
#         next_y = y + plus_y
#         if abs(next_x) > 5 or abs(next_y) > 5:
#             continue

#         max_x, max_y = max(x, next_x), max(y, next_y)
#         min_x, min_y = min(x, next_x), min(y, next_y)
        
#         if (min_x, min_y, max_x, max_y) not in p_set:
#             p_set.add((min_x, min_y, max_x, max_y))
#             answer += 1

#         x = next_x
#         y = next_y
#         print(x, y, p_set)
#     return answer

# print(solution())


# def solution(w=100,h=100):
#     import math
    
#     answer = w * h
#     inclination = h/w
#     h_list = [0] * (w+1)
#     for x in range(w+1):
#         h_list[x] = x * inclination
#     for x in range(1, w+1):
#         answer -= math.ceil(h_list[x]) - int(h_list[x-1])
    
#     return answer
# print(solution())

# def gcd(a, b):
#     while b > 0:
#         a, b = b, a%b
#     return a

# def solution(w, h):
    
#     answer = w * h
#     pre_h = 0
#     gcd_val = gcd(w, h)
    
#     for x in range(1, (w//gcd_val)+1):
#         tmp_h = (h*x)//w
#         res = (h*x)%w
#         if res == 0:
#             answer -= tmp_h - pre_h
#         else:
#             answer -= (tmp_h+1) - pre_h
    
#         pre_h = tmp_h
    
#     return answer


# def gcd(a, b):
#     while b > 0:
#         a, b = b, a%b
#     return a

# def solution(w, h):
#     sum_of_sub = 0
#     pre_h = 0
#     val_gcd = gcd(w, h)
    
#     for x in range(1, (w//val_gcd)+1):
#         val_h_times_x = h*x
#         tmp_h = val_h_times_x//w
#         res = val_h_times_x%w
#         if res == 0:
#             sum_of_sub += tmp_h - pre_h
#         else:
#             sum_of_sub += (tmp_h+1) - pre_h
    
#         pre_h = tmp_h
    
#     return w*h - sum_of_sub*val_gcd
# print(solution(8, 12))


# def gcd(a, b):
#     while b > 0:
#         a, b = b, a%b
#     return a

# def ans(w, h):
#     gcd_val = gcd(w, h)
#     if gcd_val == 1:
#         return w+h-1
#     else:
#         return ans(w//gcd_val, h//gcd_val) * gcd_val
# def solution(w, h):
#     gcd_val = gcd(w, h)
#     if gcd_val == 1:
#         return w*h -(w+h-1)
#     else:
#         return w*h - ans(w//gcd_val, h//gcd_val) * gcd_val

# print(solution(1, 9))

# def solution(bin1, bin2):
#     ans = int(bin1) + int(bin2)
#     ans = [0] + list(map(int, str(ans)))
#     for idx in range(len(ans)-1, -1, -1):
#         if ans[idx] // 2 == 1:
#             ans[idx] -= 2
#             ans[idx-1] += 1

#     return str(int(''.join(map(str, ans))))

# print(solution("10","11"))


# def solution(A, B):
#     answer = -1
#     for idx in range(len(A)):
#         if B == A[idx:] + A[:idx]:
#             answer = idx
#             break
#     return answer

# print(solution("hello", "ohell"))

# def solution(my_string):
#     s = list(map(str, my_string.split()))
#     idx = 1
#     ans = int(s[0])
#     while idx < len(s):
#         if s[idx] == '+':
#             ans += int(s[idx+1])
#         else:
#             ans -= int(s[idx+1])
#         idx += 2
#     return ans

# print(solution("3 + 5 + 7"))

# print(max([[1, 1], [2, 3], [2, 2], [1, 2]]))

# def solution(polynomial):
#     p = polynomial.split()
#     ans = [0, 0]
#     for val in range(0, len(p), 2):
#         try:
#             if p[val][-1] == 'x':
#                 ans[0] += int(p[val][:-1])
#             else:
#                 ans[1] += int(p[val])
#         except ValueError:
#             ans[0] += 1

#     result = ''
#     if ans[0] == 1: result += "x"
#     elif ans[0] > 1: result += str(ans[0])+"x"
    
#     if ans[1] != 0:
#         if ans[0] > 0:
#             result += ' + '
#         result += str(ans[1])
    
#     return result if result != '' else '0'

# print(solution("0 + 0"))


# def solution(board):
#     len_board = len(board)
#     check_board = [[1] * len_board for _ in range(len_board)]
    
#     for x in range(len_board):
#         if x == 0: inc_x = [0, 1]
#         elif x == len_board-1: inc_x = [-1, 0]
#         else: inc_x = [-1, 0, 1]
    
#         for y in range(len_board):
#             if board[x][y] == 1:
#                 if y == 0: inc_y = [0, 1]
#                 elif y == len_board-1: inc_y = [-1, 0]
#                 else:
#                     inc_y = [-1, 0, 1]

#                 for plus_x in inc_x:
#                     for plus_y in inc_y:
#                         check_board[x+plus_x][y+plus_y] = 0
    
#     ans = 0
#     for x in range(len_board):
#         ans = sum(check_board[x])
#         print(check_board[x])
#     return ans

# print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))


# def solution(lines):
#     x = [0]*198
#     for line in lines:
#         for num in range(min(line[0],line[1]), max(line[0], line[1])):
#             x[num+99] += 1
    
#     ans = 0
#     for idx in range(198):
#         if x[idx] >= 2:
#             ans += 1
#     return ans

# # print(solution([[-99, -98], [-99, 99], [98, 99]]))
# print(solution([[-1, 0], [0, 1], [1,2]]))


# def solution(babbling):
#     answer = 0
#     idx = 0
#     for bab in babbling:
#         idx = 0
#         last_bab = "_"
#         print(bab)
#         check = False
#         while idx < len(bab):
#             print("idx", idx)
#             check = False
#             if idx+2 < len(bab):
#                 print("--")
#                 if bab[idx:idx+3] in ["aya", "woo"]:
#                     if bab[idx:idx+3] != last_bab:
#                         last_bab = bab[idx:idx+3]
#                         idx += 3
#                         check = True
#             if idx+1 < len(bab):
#                 if bab[idx:idx+2] in ["ye", "ma"]:
#                     if bab[idx:idx+2] != last_bab:
#                         last_bab = bab[idx:idx+2]
#                         idx += 2
#                         check = True
#             if not check:
#                 break
#         if check:
#             answer += 1
#         print("answer", answer)
#     return answer

# print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))