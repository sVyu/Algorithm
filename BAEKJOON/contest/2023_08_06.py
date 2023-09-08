# 
# ans = [0]*10
# for _ in range(5):
#     n = int(input())
#     if ans[n]:
#         ans[n] = 0
#     else:
#         ans[n] = 1

# for i in range(10):
#     if ans[i]:
#         print(i)
#         break


# B
# def solve():
#     N = int(input())
#     rs = [input() for _ in range(N)]
#     pre_end, next_first = '_', '_'

#     for i in range(N):
#         if rs[i] == '?':
#             if i > 0:
#                 pre_end = rs[i-1][-1]
#             if i < N-1:
#                 next_first = rs[i+1][0]
#             break

#     rs_set = set(rs)
#     # print(rs_set)

#     M = int(input())
#     ws = [input() for _ in range(M)]
#     if N == 1:
#         print(ws[0])
#         return

#     for w in ws:
#         if (w not in rs_set):
#             if ((pre_end == '_') and (w[-1] == next_first)):
#                 print(w)
#                 break
            
#             if ((next_first != '_') and (w[0] == pre_end) and (w[-1] == next_first)):
#                 print(w)
#                 break

#             if ((next_first == '_') and (w[0] == pre_end)):
#                 print(w)
#                 break
# solve()


# H
# import sys
# input = sys.stdin.readline
# N, M, Q = map(int, input().split())
# ns = [0]*N
# ms = [0]*M
# for _ in range(Q):
#     k, c, v = map(int, input().split())
#     if k == 1:
#         ns[c-1] += v
#     else:
#         ms[c-1] += v
# # print(ns, ms)

# for i in range(N):
#     for j in range(M):
#         print(ns[i]+ms[j], end=' ')
#     print()


# E
# def fac(n):
#     val = 1
#     for k in range(2, n+1):
#         val *= k
#     return val

# def comb(n, k):
#     return fac(n)//(fac(n-k)*fac(k))

# def solve():
#     N, K = map(int, input().split())
#     mod = int(1e9)+7
#     twos = [0]*(int(2e5)+1)
#     twos[0] = 1
#     for i in range(1, len(twos)):
#         twos[i] = (twos[i-1]*2) % mod
#     print(twos[:10])

#     ns = list(map(int, input().split()))
#     cnts = [0]*K

#     for n in ns:
#         cnts[n%K] += 1
#     # print(cnts)

#     ans = twos[cnts[0]]
#     for a in range(1, K//2+1):
#         if a == K-a:
#             ans *= twos[cnts[a]]
#         else:
#             ans *= twos[(cnts[a]+cnts[K-a])]
#     # ans -= sum(cnts)+1
#     print(ans % mod)

# solve()


# G
# import sys
# input = sys.stdin.readline

# N = int(input())
# ns = list(map(int, input().split()))
# Q = int(input())
# qs = list(map(int, input().split()))

# limit = int(1e5)
# dp = [0]*(limit+1)
# for n in ns:
#     dp[n] += 1
# for i in range(1, limit+1):
#     for a in range(2, limit+1):
#         if i*a <= limit:
#             dp[i*a] += dp[i]
#         else:
#             break

# for q in qs:
#     print(dp[q], end=' ')

