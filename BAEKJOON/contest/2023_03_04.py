# 2023 성균관대학교 프로그래밍 경진대회 Open Contest
# A - 증가 배열 만들기
# def solve():
#     N, M, K = map(int, input().split())
#     if N+M-1 > K:
#         print("NO")
#     else:
#         print("YES")
#         for x in range(N):
#             for y in range(M):
#                 print(x+y+1, end=' ')
#             print()

# solve()


# B - 토크나이저
# from collections import deque

# def solve():
#     q = deque(input().split())
#     # print(q)

#     new_q = deque()
#     while q:
#         w = q.popleft()
#         pre_idx, idx = 0, 0
#         len_w = len(w)

#         while idx <= len_w-1:
#             if w[idx] in ['<', '>', '&', '|', '(', ')']:
#                 if pre_idx != idx:
#                     new_q.append(w[pre_idx:idx])
#                     # print("new_q", new_q)
#                 # print(w, idx, pre_idx, idx)

#                 if w[idx] == '<':
#                     new_q.append('<')
#                     pre_idx = idx+1
#                 elif w[idx] == '>':
#                     new_q.append('>')
#                     pre_idx = idx+1
#                 elif w[idx] == '&':
#                     new_q.append('&&')
#                     pre_idx = idx+2
#                     idx += 1
#                 elif w[idx] == '|':
#                     new_q.append('||')
#                     pre_idx = idx+2
#                     idx += 1
#                 elif w[idx] == '(':
#                     new_q.append('(')
#                     pre_idx = idx+1
#                 elif w[idx] == ')':
#                     new_q.append(')')
#                     pre_idx = idx+1
#             idx += 1
#         if pre_idx != idx:
#             new_q.append(w[pre_idx:idx])
#     # print(new_q)

#     while new_q:
#         print(new_q.popleft(), end=' ')

# solve()


# C - 마법박스
# 28퍼 틀렸습니다
# 오 넘겼다
# import sys
# input = sys.stdin.readline

# def make_sieve(sieve, l, r):
#     for i in range(l, r+1):
#         if sieve[i]:
#             for j in range(2*i, r+1, i):
#                 sieve[j] = False
#     return sieve

# def solve():
#     N = int(input().rstrip())
#     ans = -1

#     s = [False, False] + [True]*(N-1)
#     s = make_sieve(s, 2, N)
#     primes = [idx for idx in range(len(s)) if s[idx]]

#     l, r = 0, len(primes)-1
#     # cnt = 1

#     while l <= r:
#         mid = (l+r)//2
#         print("?", primes[mid])
#         sys.stdout.flush()
#         # print("cnt", cnt)
#         # cnt += 1

#         res = int(input().rstrip())
#         if res == 1:    # 다 있음
#             l = mid+1

#         else:           # X
#             ans = primes[mid]
#             r = mid-1

#     print("!", ans)
#     sys.stdout.flush()

# solve()


# D - 벌레컷 : TLE
# def solve():
#     N = int(input())
#     nums = list(map(int, input().split()))
#     s = [nums[0]] + [0]*(N-1)

#     for i in range(1, N):
#         s[i] = s[i-1] + nums[i]
#     # print(s)

#     ans = 0
#     for i in range(N-2):
#         for j in range(i+1, N-1):
#             if s[i] < s[N-1]-s[j] < s[j]-s[i]:
#                 ans += 1

#     print(ans)

# solve()

# 소스 최적화
# def solve():
#     N = int(input())
#     nums = list(map(int, input().split()))
#     s = [nums[0]] + [0]*(N-1)

#     for i in range(1, N):
#         s[i] = s[i-1] + nums[i]
#     # print(s)

#     ans = 0
#     # 머리 
#     for i in range(N-2):
#         # 머리가 최대한의 가슴보다 크거나 같은 경우
#         if (s[i] >= (s[N-2]-s[i])):
#             break
#         # print("i", i)

#         pos_idx = [-1, -1]
#         # 조건을 만족하는 최소한의 가슴 idx
#         l, r = i+1, N-2
#         while l <= r:
#             mid = (l+r)//2
#             # print("[1]", l, r, mid)
#             # 머리 < 배 < 가슴
#             if s[i] < (s[N-1] - s[mid]) < (s[mid]-s[i]):
#                 r = mid-1
#                 pos_idx[0] = mid
#             else:
#                 # 머리 < 배
#                 if s[i] < (s[N-1] - s[mid]):
#                     l = mid+1
#                 else:
#                     r = mid-1

#         # 조건을 만족하는 최대한의 가슴 idx
#         l, r = i+1, N-2
#         while l <= r:
#             mid = (l+r)//2
#             # print("[2]", l, r, mid)

#             # 머리 < 배 < 가슴
#             if s[i] < (s[N-1] - s[mid]) < (s[mid]-s[i]):
#                 l = mid+1
#                 pos_idx[1] = mid
#             else:
#                 # 머리 < 배
#                 if s[i] < (s[N-1] - s[mid]):
#                     l = mid+1
#                 else:
#                     r = mid-1

#         # print(pos_idx)
#         # 만족하는 경우가 없으면 break (continue로 진행해도 무의미)
#         if -1 in pos_idx:
#             break
#         else:
#             ans += pos_idx[1]-pos_idx[0]+1

#     print(ans)

# solve()