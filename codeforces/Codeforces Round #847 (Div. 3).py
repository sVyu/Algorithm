# 2023/01/27

# A. Polycarp and the Day of Pi
# import sys
# input = sys.stdin.readline
# import math

# pi = list("314159265358979323846264338327")
# # print(pi)

# for _ in range(int(input())):
#     ans = 0
#     target = list(input().rstrip())
#     # print(target)

#     for idx in range(len(target)):
#         if target[idx] == pi[idx]:
#             ans += 1
#         else:
#             break

#     print(ans)


# B. Taisia and Dice
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n, s, r = map(int, input().split())
#     max_dice = s-r
#     ans = [1]*n
#     ans[0] = max_dice
#     r -= (n-1)

#     for idx in range(1, n):
#         gab = min(max_dice - ans[idx], r)
#         if gab == 0:
#             break
#         else:
#             ans[idx] += gab
#             r -= gab

#     print(*ans)


# C. Premutation
# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# wrong code 
# for _ in range(int(input())):
#     g = defaultdict(set)
#     for _ in range(int(input())):
#         nums = list(map(int, input().split()))
#         for i in range(len(nums)-1):
#             append_check = False
#             for ii in range(i+1, len(nums)):
#                 if not append_check:
#                     if nums[ii] not in g[nums[i]]:
#                         g[nums[i]].add(nums[ii])
#                         append_check = True
#                 else:
#                     if nums[ii] in g[nums[i]]:
#                         print(g, nums[ii])
#                         g[nums[i]].pop(nums[ii])
#         print(g)

# revised !
# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# for _ in range(int(input())):
#     g = defaultdict(set)

#     N = int(input())
#     for _ in range(N):
#         nums = list(map(int, input().split()))
#         for i in range(len(nums)-1):
#             for ii in range(i+1, len(nums)):
#                 g[nums[i]].add(nums[ii])
#     # print(g)

#     total_cnt = defaultdict(int)
#     for i in range(1, N+1):
#         total_cnt[i] += 0
#         for k in g[i]:
#             total_cnt[k] += 1
#     # print(total_cnt)

#     total_cnt = sorted(total_cnt.items(), key=lambda x:(x[1]))
#     # print(total_cnt)
#     for c in total_cnt:
#         print(c[0], end = ' ')
#     print()


# D. Matryoshkas
# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# for _ in range(int(input())):
#     N = int(input())
#     n = list(map(int, input().split()))

#     nums = defaultdict(int)
#     for nn in n:
#         nums[nn] += 1
#     # print(nums)
#     # print(min(nums.keys()))

#     ans = 0
#     while nums:
#         now_num = min(nums.keys())
#         min_val = min(nums.values())
#         ans += min_val

#         while now_num in nums:
#             nums[now_num] -= min_val
#             if nums[now_num] == 0:
#                 del nums[now_num]
#             now_num += 1

#     print(ans)


# import sys
# input = sys.stdin.readline
# from collections import defaultdict
# from heapq import heappush, heappop, heapify

# for _ in range(int(input())):
#     N = int(input())
#     n = list(map(int, input().split()))

#     now_num_heap, del_set = [], set()
#     nums = defaultdict(int)

#     for nn in n:
#         nums[nn] += 1
#         # heappush(now_num_heap, nn)
#     # print(nums)
#     # print(min(nums.keys()))
#     now_num_heap = n[:]
#     heapify(now_num_heap)

#     ans = 0
#     while nums:
#         while del_set and now_num_heap[0] in del_set:
#             heappop(now_num_heap)

#         now_num = now_num_heap[0]
#         min_val = min(nums.values())
#         ans += min_val

#         while now_num in nums:
#             nums[now_num] -= min_val
#             if nums[now_num] == 0:
#                 del nums[now_num]
#                 del_set.add(now_num)
#             now_num += 1
#         # print("nums", nums)

#     print(ans)


# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# for _ in range(int(input())):
#     N = int(input())
#     n = list(map(int, input().split()))

#     nums = defaultdict(int)
#     for nn in n:
#         nums[nn] += 1

#     nums = sorted(nums.items(), key=lambda x:(x[0]))
#     # print(nums)

#     ans = 0
#     pre_key = -1
#     now_level = 0

#     for key, val in nums:
#         # print(key, val)
#         if pre_key+1 != key:
#             now_level = 0

#         if val > now_level:
#             ans += (val - now_level)

#         pre_key = key
#         now_level = val

#     print(ans)