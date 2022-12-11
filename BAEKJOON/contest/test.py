# 겨울 숲의 초대

# pm 02:15 ~ 
# A번 - 눈 치우기
# N = int(input())
# n = sorted(list(map(int, input().split())), reverse = True)
# # print(n)

# p = [0, 0]
# ans = 0

# while p[0] <= N and p[1] <= N:
#     # print(p[0], p[1])

#     # 인덱스 증가
#     if p[1] < N:
#         p[1] += 1

#     # 한 집만 선택 가능한 경우
#     if p[1] >= N:
#         while p[0] < N:
#             ans += n[p[0]]
#             p[0] += 1
#         break

#     # 두 집 선택 가능한 경우
#     else:
#         # print(p[0], p[1])
#         min_val = min(n[p[0]], n[p[1]])
#         ans += min_val
#         n[p[0]] -= min_val
#         n[p[1]] -= min_val

#     if n[p[0]] == 0:
#         if n[p[1]] == 0:
#             p[1] += 1
#         p[0] = p[1]

#     # 포인터 순서 정렬
#     if p[0] > p[1]:
#         p[0], p[1] = p[1], p[0]
    
#     # print(n)

# print(ans if ans <= 1440 else -1)

# N = int(input())
# n = list(map(int, input().split()))

# ans = 0
# if N == 1:
#     ans = n[0]
# else:
#     while sum(n) != 0:
#         n = sorted(n, reverse = True)
#         if n[1] == 0:
#             ans += n[0]
#             break
#         else:
#             min_val = min(n[0], n[1])
#             ans += min_val
#             n[0] -= min_val
#             n[1] -= min_val

# print(ans if ans <= 1440 else -1)

# C번 - 별꽃의 세레나데 (Easy)
# N = int(input())
# n = N

# ans = 0
# while n > 0:
#     ans += (N/n)
#     n -= 1
# print(ans)


# D번 - 생산 시스템 관리
# DP? Backtracking이 더 좋을 듯.. 싶었는데 너무 오래 걸릴 수 있음 다시 DP로

# 시작 n(idx) = 0
# def btr(N, B, machine, plus_m, idx, left_b):
#     global max_val, max_plus_m

#     for b in range((B//machine[idx][2])+1):
#         # 예산 내 구매 불가하거나 확률이 1을 넘는 경우
#         # if (left_b < b * machine[idx][2]):
#         #     break
#         if (left_b < b * machine[idx][2]) or (machine[idx][0] + machine[idx][1] * b) > 200:
#             break
#         else:
#             # 해당 idx에 대해 개수 b만큼 구매하는 게 예산에 문제되지 않을 때
#             plus_m[idx] = b
#             if idx < N-1:
#                 btr(N, B, machine, plus_m, idx+1, left_b - b * machine[idx][2])
#             else:
#                 # 확률 계산
#                 p = 1
#                 for y in range(N):
#                     p *= min(100, machine[y][0] + (machine[y][1] * plus_m[y]))
#                 # 가장 높은 확률일 때
#                 if max_val < p:
#                     max_val = p
#                     # print(plus_m)
#                     max_plus_m = plus_m[:]

# def solve():
#     N, B = map(int, input().split())
#     machine = [list(map(int, input().split())) for _ in range(N)]

#     global max_val, max_plus_m
#     max_val = 0
#     plus_m, max_plus_m = [0] * N, [0] * N

#     btr(N, B, machine, plus_m, 0, B)
#     print(max_val)
#     print(*max_plus_m)

# solve()


# try 2
# N, B = map(int, input().split())
# machine = [list(map(int, input().split())) for _ in range(N)]

# dp = [[1] * (B+1) for _ in range(N+1)]
# cb = [[list() for _ in range(B+1)] for _ in range(N+1)]

# for x in range(1, N+1):
#     # b : 비용
#     dp[x][0] = dp[x-1][0] * machine[x-1][0] / 100
#     cb[x][0] = cb[x-1][0] + [0]

#     # tmp_k : 확률 1까지 필요한 개수
#     tmp_k = ((100 - machine[x-1][0]) // machine[x-1][1])
#     if (100 - machine[x-1][0]) % machine[x-1][1] != 0:
#         tmp_k += 1
#     # print(tmp_k)

#     for b in range(1, B+1):
#         # k : 비용만 봤을 때 구매 가능한 기계 수
#         k = b // machine[x-1][2]
#         # 최소값 계산
#         k = min(k, tmp_k)

#         dp[x][b] = min(1, (dp[x-1][b] * machine[x-1][0] / 100))
#         cb[x][b] = cb[x-1][b][:]
#         cb[x][b].append(0)

#         # new_p : 예산에 맞춰 구매했을 때 확률
#         new_p = dp[x-1][b-k*machine[x-1][2]] * min(1, (machine[x-1][0] + k*machine[x-1][1])/100)
#         if dp[x][b] < new_p:
#             dp[x][b] = new_p

#             cb[x][b] = cb[x-1][b-k*machine[x-1][2]][:]
#             cb[x][b].append(k)

# for x in range(N+1):
#     print("x", x)
#     y = 0
#     while y <= B:
#         print(dp[x][y], end = ' ')
#         y += 1
#         if y % 10 == 0:
#             print()
#     print()

# print(int(dp[N][B]*(10**(2*N))))
# print(*cb[N][B])

'''
2 45
40 15 20
60 10 15
'''

'''
2 175
40 13 20
60 9 15
'''

# B번 - 은나무
# import sys
# input = sys.stdin.readline

# K, H, Q = map(int, input().split())
# for _ in range(Q):
#     A, B = map(int, input().split())

#     if B >= (K+1)**H:
#         print(-1)
#         continue
#     elif A == B:
#         ans = 0
#     else:
#         mod_val = (K+1)**(H-1)
#         ans = 2

#         same_check = True
#         while (A + B) > 0:
#             if same_check:
#                 if A // mod_val != B // mod_val :
#                     same_check = False
#                 else:
#                     if A % mod_val == 0 or B % mod_val == 0:
#                         same_check = False

#             else:
#                 if A != 0:
#                     ans += 1
#                 if B != 0:
#                     ans += 1
            
#             A %= mod_val
#             B %= mod_val

#             mod_val //= (K+1)
#     print("ans", ans)