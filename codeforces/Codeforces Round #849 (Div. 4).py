# 2023/02/03


# A
# import sys
# input = sys.stdin.readline
# import string

# small_letters = list(string.ascii_lowercase)
# ans_list = [0] * 26
# for c in "codeforces":
#     ans_list[small_letters.index(c)] += 1
# # print(ans_list)
# # print(len(ans_list))

# for _ in range(int(input())):
#     if ans_list[small_letters.index(input().rstrip())] != 0:
#         print("YES")
#     else:
#         print("NO")


# B
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     x, y = 0, 0
#     pos = False

#     n = int(input())
#     moves = list(input().rstrip())
#     for m in moves:
#         if m == 'U':
#             x += 1
#         elif m == 'D':
#             x -= 1
#         elif m == 'L':
#             y -= 1
#         else:
#             y += 1

#         if x == 1 and y == 1:
#             pos = True
#             break

#     if pos: print("YES")
#     else: print("NO")


# C
# import sys
# input = sys.stdin.readline
# from collections import deque

# for _ in range(int(input())):
#     n = int(input())
#     string = list(map(int, str(input().rstrip())))
#     # print(string)

#     que = deque()
#     for s in string:
#         que.append(s)

#     # print(que)
#     # print(que[-1])

#     while n > 1:
#         if que[0] + que[-1] == 1:
#             que.popleft()
#             que.pop()
#             n -= 2
#         else:
#             break

#     print(n)


# D
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n = int(input())
#     string = list(input().rstrip())
#     # print("s", string)

#     total_appeared = [0] * 26
#     for s in string:
#         total_appeared[ord(s)-97] += 1
#     # print(total_appeared)

#     max_ans = 0
#     left_appeared = [0] * 26
#     left_part = 0
#     right_part = sum([1 for t in total_appeared if t != 0])
#     # print(right_part)

#     for c in string:
#         idx = ord(c)-97
#         total_appeared[idx] -= 1
#         if total_appeared[idx] == 0:
#             right_part -= 1

#         left_appeared[idx] += 1
#         if left_appeared[idx] == 1:
#             left_part += 1

#         max_ans = max(max_ans, left_part + right_part)

#     print(max_ans)


# E
'''
1
3
1 -2 3
6
'''
# import sys
# input = sys.stdin.readline
# from heapq import heappush, heappop

# for _ in range(int(input())):
#     N = int(input())
#     numbers = list(map(int, input().split()))

#     there_is_zero = False
#     heap = []

#     order = 0
#     for n in numbers:
#         if n < 0:
#             heappush(heap, [n, order])
#             order += 1
#         elif n == 0:
#             there_is_zero = True
#     # print(heap)

#     minus_val = 0
#     target_idx = -1
#     if not there_is_zero and len(heap) % 2 != 0:
#         while heap and heap[0]:
#             if heap[0][1] % 2 != 0:
#                 heappop(heap)
#             else:
#                 minus_val, target_idx = heappop(heap)
#                 # print("minus_val", minus_val, target_idx)
#                 break

#     if target_idx == -1:
#         print(sum(abs(n) for n in numbers) + minus_val)
#     else:
#         print(sum([abs(numbers[idx]) if idx != target_idx else numbers[idx] for idx in range(N)]))

# 0에 가장 근접한 음수 혹은 0을 찾으면 된다
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     N = int(input())
#     numbers = list(map(int, input().split()))

#     minus_cnt = 0
#     minus_val = int(1e9)

#     for n in numbers:
#         if n < 0:
#             minus_cnt += 1

#         if n == 0:
#             minus_val = 0
#             break
#         elif minus_val > abs(n):
#             minus_val = abs(n)

#     if minus_cnt % 2 == 0:
#         minus_val = 0

#     print(sum(abs(n) for n in numbers) + 2*(-minus_val))


# G1
# import sys
# input = sys.stdin.readline
# from heapq import heappush, heappop

# for _ in range(int(input())):
#     N, c = map(int, input().split())
#     numbers = list(map(int, input().split()))

#     heap = []
#     for idx in range(N):
#         heappush(heap, numbers[idx]+idx+1)
#     # print(heap)

#     ans = 0
#     while heap and c >= heap[0]:
#         c -= heappop(heap)
#         ans += 1
#     print(ans)


# F
# import sys
# input = sys.stdin.readline

# def return_new_num(num):
#     return_val = 0
#     while num > 0:
#         return_val += num % 10
#         num //= 10
#     return return_val

# for _ in range(int(input())):
#     N, qs = map(int, input().rstrip().split())
#     numbers = list(map(int, input().rstrip().split()))
#     # print(numbers)

#     for _ in range(qs):
#         q = list(map(int, input().split()))
#         if q[0] == 1:
#             for idx in range(q[1]-1, q[2]):
#                 numbers[idx] = return_new_num(numbers[idx])
#                 # print("[1]", numbers)
#         else:
#             print(numbers[q[1]-1])


# import sys
# input = sys.stdin.readline

# def num_to_list(n:int):
#     new_num_list = [0]*10
#     while n > 0:
#         print(n%10)
#         new_num_list[n%10] += 1``
#         n //= 10
#     return new_num_list

# def update_times_of_num(this_num:list):
#     new_num = 0
#     for idx in range(10):
#         new_num += this_num[idx]*idx

#     return num_to_list(new_num)

# def solve():
#     for _ in range(int(input())):
#         N, qs = map(int, input().rstrip().split())
#         numbers = list(map(int, input().rstrip().split()))
#         # print(numbers)
#         times_of_num = [[0]*10 for _ in range(N)]

#         for idx in range(N):
#             times_of_num[idx] = num_to_list(numbers[idx])

#         # for x in range(N):
#         #     print(times_of_num[x])

#         for _ in range(qs):
#             q = list(map(int, input().split()))
#             if q[0] == 1:
#                 for idx in range(q[1]-1, q[2]):
#                     times_of_num[idx] = update_times_of_num(times_of_num[idx])
#             else:
#                 print("ans", times_of_num[q[1]-1])

# solve()


# G2
# import sys
# input = sys.stdin.readline
# from heapq import heappush, heappop

# for _ in range(int(input())):
#     N, c = map(int, input().split())
#     numbers = list(map(int, input().split()))
#     visited = [False] * N

#     heap = []
#     for idx in range(N):
#         heappush(heap, [numbers[idx]+idx+1, idx])
#     print("heap", heap)

#     ans = 0
#     check = False
#     while heap and c >= heap[0][0]:
#         print("now_heap", heap)
#         if visited[heap[0][1]]:
#             heappop(heap)
#             continue
#         # print("minus_val", heappop(heap)[0])
#         minus_val, idx = heappop(heap)
#         c -= minus_val
#         print("now_c", c)
#         ans += 1
#         visited[idx] = True
#         print("visited", visited)
#         if not check:
#             for idx in range(N):
#                 heappush(heap, [numbers[idx]+(N-idx), idx])
#             check = True
#             # print("plused", heap)
#     print("ans", ans)

#
'''
2 14
7 5

위 케이스의 경우, 7 5 순으로 처리해야한다
지금 내 코드는 5 7 순으로 처리하고 있음 ..!
'''