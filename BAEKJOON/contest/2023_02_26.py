# A1번 - 스네이크
# n, m = map(int, input().split())
# if (n*m) % 2 == 0:
#     print(n*m)
# else:
#     print(n*m-1)

# A2번 - 스네이크 그리기
# n, m = map(int, input().split())
# if (n*m) % 2 == 0:
#     print(n*m)
# else:
#     print(n*m-1)

# if n % 2 == 0:
#     k = 1
#     for y in range(1, m+1):
#         print(k, y)
#     k += 1
#     while k < n:
#         for y in range(m, 1, -1):
#             print(k, y)
#         k += 1

#         for y in range(2, m+1):
#             print(k, y)
#         k += 1

#     for y in range(m, 0, -1):
#         print(k, y)

#     for x in range(k-1, 1, -1):
#         print(x, 1)

# elif m % 2 == 0:
#     k = 1
#     for x in range(1, n+1):
#         print(x, k)

#     k += 1
#     while k < m:
#         for x in range(n, 1, -1):
#             print(x, k)
#         k += 1

#         for x in range(2, n+1):
#             print(x, k)
#         k += 1

#     for x in range(n, 0, -1):
#         print(x, k)

#     for y in range(k-1, 1, -1):
#         print(1, y)

# else:
#     for y in range(1, m+1):
#         print(1, y)

#     for x in range(2, n+1):
#         print(x, m)

#     ky = m-1
#     while ky > 2:
#         for x in range(n, 1, -1):
#             print(x, ky)

#         ky -= 1
#         for x in range(2, n+1):
#             print(x, ky)

#         ky -= 1

#     kx = n
#     while kx > 4:
#         for y in range(2, 0, -1):
#             print(kx, y)
#         kx -= 1

#         for y in range(1, 3):
#             print(kx, y)
#         kx -= 1

#     print(3, 2)
#     print(3, 1)
#     print(2, 1)


# B1번 - 1차원 2048
# from collections import defaultdict

# def solve():
#     N = int(input())
#     nums = list(map(int, input().split()))

#     d = defaultdict(int)
#     for n in nums:
#         d[n] += 1
#     # print(d)

#     limit = 82
#     checks = [0] * limit
#     now_val = 1
#     for i in range(limit):
#         if now_val in d:
#             checks[i] = d[now_val]
#         now_val *= 2
#     # print(checks)

#     for i in range(limit-1):
#         if checks[i] >= 2:
#             checks[i+1] += (checks[i]//2)
#             checks[i] %= 2 
#     # print(checks)

#     for i in range(limit-1, -1, -1):
#         if checks[i] != 0:
#             print(2**i)
#             return

#     print(0)

# solve()