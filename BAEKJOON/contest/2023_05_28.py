# 월간 향유회 2023. 05.

# A번 - 재밌는 나머지 연산
# import math

# N, R = map(int, input().split())

# n = N-R
# nset = set()

# for i in range(1, math.isqrt(n)+1):
#     if n % i == 0:
#         nset.add(i)
#         nset.add(n//i)
# # print(nset)

# print(sum(i for i in nset if i > R))


# B번 - 평균 구하기
# import sys
# input = sys.stdin.readline
# import math

# def solve():
#     N = int(input())
#     # points
#     pts = [list(map(int, input().split())) for _ in range(N)]
#     ans = 0

#     for p1 in range(N-1):
#         for p2 in range(p1+1, N):
#             ans += math.sqrt((pts[p1][0]-pts[p2][0])**2 + (pts[p1][1]-pts[p2][1])**2)

#     # print(ans*(N-1)/N)
#     print(2*ans/N)

# solve()


# C번 - 빨강~ 빨강~ 파랑! 파랑! 달콤한 솜사탕!

'''

rs = [-1]*N
bs = [-1]*N

for i in range(N-1, -1, -1):
    if s[i] == 'R':
        rs[i] = i
    elif i < N-2:
        rs[i] = rs[i+1]
# print(rs)

for i in range(N):
    if s[i] == 'B':
        bs[i] = i
    elif i > 0:
        bs[i] = bs[i-1]
# print(bs)
'''

# import sys
# input = sys.stdin.readline

# N, Q = map(int, input().split())
# s = list(input().rstrip())

# rs, bs = [], []
# for i in range(N):
#     if s[i] == 'R':
#         rs.append(i)
#     elif s[i] == 'B':
#         bs.append(i)
# # print(rs)
# # print(bs)
# rlen = len(rs)
# blen = len(bs)

# for _ in range(Q):
#     l, r = map(int, input().split())
#     # print(l, r)

#     ri, rl, rr = -1, 0, rlen-1
#     while rl <= rr:
#         rmid = (rl+rr)//2
#         # print(rl, rr, rmid, ri)

#         if l <= rs[rmid] <= r:
#             ri = rmid
#             rr = rmid-1
#         elif rs[rmid] < l:
#             rl = rmid+1
#         elif rs[rmid] > r:
#             rr = rmid-1
#     # print(ri)

#     bi, bl, br = -1, 0, blen-1
#     while bl <= br:
#         bmid = (bl+br)//2
#         # print(bl, br, bmid, bi)

#         if l <= bs[bmid] <= r:
#             bi = bmid
#             bl = bmid+1
#         elif bs[bmid] < l:
#             bl = bmid+1
#         elif bs[bmid] > r:
#             br = bmid-1
#     # print(bi)

#     # print("ri, bi", ri, bi)
#     if (ri != -1) and (ri < (rlen-1)) and (bi > 0) and (rs[ri+1] < bs[bi-1]):
#         print(rs[ri], rs[ri+1], bs[bi-1], bs[bi])
#     else:
#         print(-1)