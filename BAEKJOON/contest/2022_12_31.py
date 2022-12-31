# Good Bye, BOJ 2022!

# A번 - 2022년이 아름다웠던 이유
# import sys
# input = sys.stdin.readline
# import itertools

# def func(n):
#     tmp_n = n

#     ds = [1]
#     while tmp_n % 2 == 0:
#         tmp_n //= 2
#         ds.append(2)
    
#     d = 3
#     while tmp_n >= 2:
#         while tmp_n % d == 0:
#             tmp_n //= d
#             ds.append(d)
#         d += 1
#     # print(ds)
    
#     a_set = set()
#     ans = 0
#     for k in range(len(ds)):
#         for c in itertools.combinations(ds, k):
#             a = 1
#             for cc in c:
#                 a *= cc

#             if a not in a_set and a != n:
#                 a_set.add(a)
#                 ans += a
#     # print(a_set, ans)
#     return a_set, ans

# for _ in range(int(input())):
#     n = int(input())
#     a_set, ans = func(n)
#     # print(a_set, ans)
#     pre_cal = dict()

#     # n : 부족수 or 완전수
#     if ans <= n:
#         print("BOJ 2022")
#         continue
    
#     check = True
#     for a in a_set:
#         if a in pre_cal:
#             ans = pre_cal[a]
#         else:
#             aa_set, ans = func(a)
#             pre_cal[a] = ans
        
#         if ans > a:
#             check = False
#             break
    
#     if check: print("Good Bye")
#     else: print("BOJ 2022")


# B번 - 나무 블럭 게임
# N = int(input())
# A = sorted(list(map(int, input().split())))

# if N == 1: print(sum(A))
# elif N == 2: print(sum(A)/2)
# else: print(max(A[-2], sum(A)/N))


# C번 - 데이터 순서 복원
# from collections import defaultdict

# N = int(input())
# ABC = [list(map(int, input().split())) for _ in range(3)]
# dd = [defaultdict(int) for _ in range(N+1)]
# # print(dd)

# for i in range(3):
#     for idx1 in range(N):
#         for idx2 in range(N):
#             a, b = ABC[i][idx1], ABC[i][idx2]
#             # print(a, b)

#             # idx2 - idx1 순서
#             if idx2 < idx1:
#                 dd[a][b] += 1

# # print(dd)
# # for i in range(N+1):
# #     print(i, dd[i])

# ans = [0] * N
# for i in range(1, N+1):
#     idx = 0
#     for key, val in dd[i].items():
#         if val >= 2:
#             idx += 1
#     ans[idx] = i

# print(*ans)