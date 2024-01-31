# Hello, BOJ 2024! Open Contest

# A번 모바일 광고 입찰
# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# N, K = map(int, input().split())
# nd = defaultdict(int)

# for _ in range(N):
#     a, b = map(int, input().split())
#     nd[max(0, b-a)] += 1
# # print(nd)

# ns = list(nd.items())
# ns.sort(key=lambda x:(x[0]))

# acc = 0
# for a, b in ns:
#     acc += b
#     if acc >= K:
#         print(a)
#         break


# 3020 개똥벌레
# N, H = map(int, input().split())
# ts, bs = [0]*H, [0]*H

# for i in range(N):
#     n = int(input())
#     if i % 2 == 0:
#         bs[n] += 1
#     else:
#         ts[n] += 1
# # print(ts, bs)

# for i in range(H-2, 0, -1):
#     ts[i] = ts[i]+ts[i+1]
#     bs[i] = bs[i]+bs[i+1]
# # print(ts, bs)

# sums = [0]*(H+1)
# for i in range(1, H):
#     sums[i] += ts[i]
#     sums[i+1] += bs[H-i]
# # print(sums)

# ans_sum, ans_cnt = (N+1), 0
# for i in range(1, H+1):
#     if ans_sum > sums[i]:
#         ans_sum = sums[i]
#         ans_cnt = 1
#     elif ans_sum == sums[i]:
#         ans_cnt += 1

# print(ans_sum, ans_cnt)