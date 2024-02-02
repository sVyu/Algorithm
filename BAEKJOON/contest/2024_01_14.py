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