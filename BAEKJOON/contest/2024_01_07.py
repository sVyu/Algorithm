# 제3회 흐즈로컵 (The 3rd Chromate Cup) Algorithm Division

# B
# import sys
# input = sys.stdin.readline

# checks = [True]*1000001
# for i in range(2, 1000001):
#     if checks[i]:
#         for ii in range(2*i, 1000001, i):
#             checks[ii] = False
# primes = [i for i in range(2, 1000001) if checks[i]]

# ans = [0]
# for p in primes:
#     if p <= 30001:
#         ans.append(primes[p-1])

# for _ in range(int(input())):
#     print(ans[int(input())])


# C
# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# n, m = map(int, input().split())
# g = defaultdict(list)

# for _ in range(m):
#     a, b = map(int, input().split())
#     g[a].append(b)
#     g[b].append(a)

# def f(n):
#     val = 1
#     for x in range(n, 0, -1):
#         val *= x
#     return val

# def c(n, k):
#     return f(n)//(f(k)*f(n-k))

# ans = 0
# mod = int(1e9)+7
# for v in range(1, n+1):
#     n = len(g[v])
#     if n >= 3:
#         ans = (ans + c(n, 3)) % mod

# print(ans)