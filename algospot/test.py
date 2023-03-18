# FESTIVAL
# import sys
# input = sys.stdin.readline

# def solve():
#     for _ in range(int(input())):
#         N, L = map(int, input().split())
#         nums = list(map(int, input().split()))

#         ans = 100
#         # 0 ~ N-L까지
#         for i in range(0, N-L+1):
#             now_sum = sum(nums[i:i+L-1])
#             for j in range(i+L-1, N):
#                 # print(i, j)
#                 now_sum += nums[j]
#                 ans = min(ans, now_sum/(j-i+1))

#         print(ans)

# solve()


# 개선 (sums 도입)
# (6000ms → 6248ms) 시간이 더 걸렸음 (ㅋㅋㅋ..)

# import sys
# input = sys.stdin.readline

# def solve():
#     for _ in range(int(input())):
#         N, L = map(int, input().split())
#         nums = list(map(int, input().split()))
#         sums = [0]*(N+1)
#         for i in range(1, N+1):
#             sums[i] = sums[i-1]+nums[i-1]
#         # print(sums)

#         ans = 100
#         # i : 1부터 N-L+1까지
#         for i in range(1, N-L+2):
#             for j in range(i+(L-1), N+1):
#                 ans = min(ans, (sums[j]-sums[i-1])/(j-i+1))

#         print(ans)

# solve()