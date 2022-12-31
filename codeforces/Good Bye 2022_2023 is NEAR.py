# A. Koxia and Whiteboards
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n, m = map(int, input().split())
#     a = sorted(list(map(int, input().split())))
#     b = list(map(int, input().split()))

#     for bb in b:
#         a[0] = bb
#         a = sorted(a)
#     print(sum(a))

# #     # a = sorted(list(map(int, input().split())))
# #     # b = sorted(list(map(int, input().split())))
# #     # if n > m:
# #     #     print(sum(b) + sum(a[-(n-m):]))
# #     # elif n == m:
# #     #     print(sum(b))
# #     # else:
# #     #     print(sum(b[-n:]))


# B. Koxia and Permutation
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     ans = [0]*n

#     k = n
#     for idx in range(0, n, 2):
#         ans[idx] = k
#         k -= 1

#     k = 1
#     if n > 1:
#         for idx in range(1, n, 2):
#             ans[idx] = k
#             k += 1

#     print(*ans)


# C. Koxia and Number Theory
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))

# def prime_num_check(n):
#     if n == 1: return False
#     elif n == 2: return True
#     elif n % 2 == 0: return False
#     else:
#         for k in range(3, int(n**(1/2))+1, 2):
#             if n % k == 0:
#                 return False
#         return True
# print(prime_num_check(int(1e18)+1))

