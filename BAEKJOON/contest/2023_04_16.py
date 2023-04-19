# 제1회 와쿠(AGCU)컵

# A번 - 초코바
# N, M = map(int, input().split())
# print("Yes" if 100*N >= M else "No")


# B번 - 사격 내기
# def make_bins(n):
#     bins = [0]*10
#     for idx in range(0, 10):
#         bins[idx] = n%2
#         n //= 2
#         if n == 0:
#             break
#     return bins

# def solve():
#     A, B = map(int, input().split())
#     binsA = make_bins(A)
#     binsB = make_bins(B)

#     ans, val = 0, 1
#     for i in range(10):
#         if binsA[i] + binsB[i] == 1:
#             ans += val
#         val *= 2

#     print(ans)

# solve()


# C번 - 고양이는 많을수록 좋다
# def solve():
#     N = int(input())
#     if N == 0:
#         print(0)
#         return

#     ans, val = 1, 1
#     while val < N:
#         val *= 2
#         ans += 1
#     print(ans)

# solve()


# D번 - 오렌지먹은지오랜지
# def solve():
#     N = int(input())
#     s = list(input())

#     for i in range(1, N):
#         # print(s[:i], s[-i:])

#         diff_cnt = 0
#         s1, s2 = s[:i], s[-i:]
#         for k in range(i):
#             if s1[k] != s2[k]:
#                 diff_cnt += 1
#         if diff_cnt == 1:
#             print("YES")
#             return
#     print("NO")

# solve()


# E번 - 합금 주화
# d1, d2, X = map(int, input().split())
# d1, d2 = max(d1, d2), min(d1, d2)

# # v : 부피, m : 질량
# v = X/d1 + (100-X)/d2
# print(100/v)


# F번 - 콰트로치즈피자
# N = int(input())
# are_they_cheese = list(input().split())
# # print(are_they_cheese)

# cheese_set = set()
# for atc in are_they_cheese:
#     if len(atc) >= 6 and str(atc[-6:]) == 'Cheese':
#         cheese_set.add(atc)
# # print(cheese_set)

# print("yummy" if len(cheese_set) >= 4 else "sad")


# G번 - N결수
# N, K = map(int, input().split())

# ans, mul = 0, 10
# for n in range(1, N+1):
#     if n == mul:
#         mul *= 10

#     ans = (ans*mul + n) % K
# print(ans)


# i = 1
# tmp_i = i
# while i <= 10000000000:
#     print("[1]", i % 997)
#     i *= 10


# H번 - △
# N = int(input())
# print((N-1) + (N-1)*(N-2)*2//2)
# for n in range(2, N+1):
#     print(1, n)


# I번 - 고추장 괄호 문자열
# N = int(input()) 
# S = list(input())
# # print(S)

# # left_bracket, right_bracket
# G, lb, rb = 0, 0, 0
# for s in S:
#     if s == '(':
#         lb += 1
#     elif s == ')':
#         rb += 1
#     else: #'G'
#         G += 1
# # print(G, lb, rb)

# # a-b = -gap, a+b = G
# gap = (lb-rb)
# need_lb = (G-gap)//2
# for s in S:
#     if s == 'G':
#         if need_lb > 0:
#             print('(', end='')
#             need_lb -= 1
#         else:
#             print(')', end='')
#     else:
#         print(s, end='')


# J번 - 사사의 사차원 사탕 봉지
# import sys
# input = sys.stdin.readline

# def solve():
#     N, M = map(int, input().split())
#     nums = list(map(int, input().split()))
#     sums = [0]*M
#     sums[0] = nums[0]
#     for i in range(M):
#         sums[i] = sums[i-1] + nums[i]
#     # print(sums)

#     for _ in range(N):
#         n = int(input())
#         if n > sums[M-1]:
#             print("Go away!")
#             continue

#         ans = -1
#         l, r = 0, M-1
#         while l <= r:
#             mid = (l+r)//2
#             if sums[mid] >= n:
#                 ans = mid
#                 r = mid-1
#             else:
#                 l = mid+1
#         print(ans+1)

# solve()


# K번 - I LOVE JavaScript
# ascii code 참고
# https://copyrightyoon.tistory.com/1417
# https://theasciicode.com.ar/

# S = list(input().split())
# # print(S)

# ans = 0
# for s in S:
#     if s == '[':
#         ans += 8
#     elif s == ']':
#         continue
#     elif 48 <= ord(s[0]) <= 57: # 0~9 ascii code
#         ans += 8
#     else: # 문자열
#         ans += len(s)+12
# print(ans)


# L번 - OX
# S = list(input())
# mod = int(1e9+7)
# ans, val = 0, 1

# for s in S:
#     if s == 'O':
#         ans = (ans + val) % mod
#     # val *= 2
#     val = (val*2) % mod
# print(ans)


# M번 - 강아지는 많을수록 좋다
# import sys
# input = sys.stdin.readline
# from collections import deque

# N, M, A, B = map(int, input().split())
# vals = [0]*(N+1)
# INF = int(1e5)+1

# for _ in range(M):
#     L, R = map(int, input().split())
#     vals[L] -= 1
#     vals[R+1] += 1
# # print(vals)

# dp = [INF]*(N+1)
# my_val = 0
# for i in range(1, N+1):
#     my_val += vals[i]
#     if my_val < 0:
#         dp[i] = -1
# # print(dp)

# q = deque([[0, 0]])
# while q:
#     val, cnt = q.popleft()
#     if dp[val] > cnt:
#         dp[val] = cnt
#         if val+A <= N:
#             q.append([val+A, cnt+1])
#         if val+B <= N:
#             q.append([val+B, cnt+1])

# # print(dp)
# print(dp[N] if dp[N] != INF else -1)


# N번 - 악보는 거들 뿐
'''
10
2 3 4 1 2 3 4 3 2 1
'''
'''
2
3 1
'''
# def solve():
#     M = int(input())
#     ms = list(map(int, input().split()))
#     # print(ms)

#     pre_diff = 0
#     ans, cnt = 1, 1
#     for i in range(1, M):
#         if ms[i] == ms[i-1]:
#             continue

#         now_diff = (ms[i] - ms[i-1])
#         # + + or - - 
#         if now_diff * pre_diff > 0:
#             cnt += 1
#         else:
#             pre_diff = now_diff
#             cnt = 2
#         ans = max(ans, cnt)

#     print(ans)

# solve()


# O번 - 지연 평가
# import sys
# input = sys.stdin.readline

# start, stop, step = 1, 1234567890123, 1
# for _ in range(int(input())):
#     cmds = list(map(int, input().split()))
#     # print(cmds)
#     if cmds[0] == 0:
#         start += cmds[1]
#         stop += cmds[1]
#     elif cmds[0] == 1:
#         start *= cmds[1]
#         stop *= cmds[1]
#         step *= cmds[1]
#     elif cmds[0] == 2:
#         start += step*cmds[1]
#     else: #3
#         print(start)