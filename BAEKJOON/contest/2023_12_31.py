# A
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     N = int(input())
#     print('Good' if (N+1) % (N%100) == 0 else 'Bye')


# B
# import sys
# input = sys.stdin.readline

# N = int(input())
# limit = 500001

# # plus, minus
# ps, ms = [0]*limit, [0]*limit
# for n in list(map(int, input().split())):
#     if n > 0:
#         ps[n] += 1
#     else:
#         ms[-n] += 1
# # print(ps[:5], ms[:5])

# ans = []
# # truers : 참을 말하는 사람의 수
# truers = sum(ms)

# # n : 거짓이 n명이라고 가정
# for n in range(limit):
#     truers += ps[n]
#     if truers+n == N:
#         ans.append(n)

#     truers -= ms[n]

# print(len(ans))
# print(*ans)


# C
'''
5 5 3
a 1 1000
b 1 1000
c 2 1000
c 1 500
d 3 1000
1 2 3 4 5
abc

5 5 3
a 1 1000
b 1 1000
c 2 1000
c 1 500
d 3 1000
1 2 5 4 3
abc
'''

# import sys
# input = sys.stdin.readline
# from heapq import heapify, heappop

# def solve():
#     N, M, K = map(int, input().split())

#     infos = [list(input().split()) for _ in range(M)]
#     for i in range(M):
#         infos[i][1], infos[i][2] = int(infos[i][1]), int(infos[i][2])
#     # print(infos)

#     attach = [[] for _ in range(26)]
#     for s, _, a in infos:
#         attach[ord(s)-97].append(a)
#     for i in range(26):
#         attach[i].sort()

#     init_idxs = [i-1 for i in list(map(int, input().split()))]
#     init_alphas = [infos[i][0] for i in init_idxs]
#     ans = int(1e6)+1

#     target = list(input())
#     for i in range(N-K+1):
#         tmp = 0
#         deleted, should_attach = [0]*26, [0]*26

#         for k in range(K):
#             if init_alphas[i+k] != target[k]:
#                 target_idx = ord(target[k])-97
#                 if attach[target_idx]:
#                     tmp += infos[init_idxs[i+k]][1]

#                     deleted[ord(infos[init_idxs[i+k]][0])-97] += 1
#                     should_attach[target_idx] += 1
#                 else:
#                     print(-1)
#                     return

#         tmp_lefts = init_idxs[:i] + init_idxs[i+K:]
#         lefts = [[] for _ in range(26)]
#         for l in tmp_lefts:
#             lefts[ord(infos[l][0])-97].append(infos[l][1])

#         for k in range(26):
#             heapify(lefts[k])

#         for k in range(26):
#             if should_attach[k]:
#                 cnt = max(0, should_attach[k] - deleted[k]) # here
#                 while cnt > 0:
#                     if lefts[k] and lefts[k][0] < attach[k][0]:
#                         tmp += heappop(lefts[k])
#                         cnt -= 1
#                     else:
#                         tmp += cnt*attach[k][0]
#                         break

#         ans = min(ans, tmp)

#     print(ans)

# solve()


# D
# N, K = map(int, input().split())

# ss = list(input())
# ls, rs = ss[:N//2], ss[N//2:]
# # print(ls, rs)

# ll, rr = [[0]*3 for _ in range(3)], [[0]*3 for _ in range(3)]
# m = dict({'2': 0, '3': 1, 'E': 2})

# ans = 0
# for i in range(N//2):
#     if ls[-i-1] == '2' and rs[i] == '2':
#         ans += 2
#     elif ls[-i-1] == '3' and rs[i] == 'E':
#         ans += 2
#     elif ls[-i-1] == 'E' and rs[i] == '3':
#         ans += 2
#     else:
#         ll[m[ls[-i-1]]][m[rs[i]]] += 1
#         rr[m[rs[i]]][m[ls[-i-1]]] += 1
# # print(ans)

# print(ll, rr)
# for _ in range(K):
#     if ll[0]

#     print(ans)