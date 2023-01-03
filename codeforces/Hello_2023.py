# A. Hall of Fame

# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n = int(input())
#     s = list(input())
    
#     first_R = n
#     for idx in range(n):
#         if s[idx] == 'R':
#             first_R = idx
#             break
    
#     last_L = -1
#     for idx in range(n-1, -1, -1):
#         if s[idx] == 'L':
#             last_L = idx
#             break
    
#     if last_L == -1 or first_R == n:
#         ans = -1
#     elif last_L < first_R:
#         # ans = 1 # i should print idx
#         ans = last_L+1
#     else: # first_R < last_L
#         ans = 0
#     print(ans)


# B. MKnez's ConstructiveForces Task

# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n = int(input())
#     if n == 3:
#         print("NO")
#     else:
#         print("YES")
#         if n % 2 == 0:
#             ans = [1]*n
#             for idx in range(0, n, 2):
#                 ans[idx] = -1
        
#         else: # n >= 3 and n % 2 == 1:
#             ans = [(n+1)//2-1]*n
#             for idx in range(0, n, 2):
#                 ans[idx] = (-n+3)//2
        
#         print(*ans)


# C. Least Prefix Sum
# import sys
# input = sys.stdin.readline
# from queue import PriorityQueue

# for _ in range(int(input())):
#     n, m = map(int, input().split())
#     a = list(map(int, input().split()))

#     ans = 0
#     total_sum = 0
#     min_sum = int(1e9)+1
#     positive_stack = []

#     for idx in range(m-1):
#         if a[idx] > 0:
#             positive_stack.append(idx)
#         total_sum += a[idx]
#         min_sum = min(total_sum, min_sum)

#     # positive_num -> negative_num    
#     if m != 1 and a[m-1] > 0:
#         ans += 1
#         a[m-1] = -a[m-1]

#     total_sum += a[m-1]
#     min_sum = min(total_sum, min_sum)
#     # print("[0]", ans)

#     # left handling
#     while min_sum < total_sum:
#         idx = positive_stack.pop()
#         total_sum -= 2*a[idx]
#         ans += 1
#     # print("[1]", ans)

#     total_sum = 0
#     # right handling
#     pq = PriorityQueue()
#     for idx in range(m, n):
#         if a[idx] < 0:
#             pq.put(a[idx])
#         total_sum += a[idx]

#         while total_sum < 0:
#             val = pq.get()
#             # print(total_sum, a[idx], val, ans)
#             total_sum -= 2*val
#             ans += 1

#     print(ans)