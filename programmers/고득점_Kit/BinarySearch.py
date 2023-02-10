# 입국심사
# pm 10:16 ~ 10:27
# def solution(n, times):
#     bot, top = 0, n*max(times)

#     ans = 0
#     while bot <= top:
#         # mid : total 시간
#         mid = (bot+top)//2
#         k = 0
#         for t in times:
#             k += mid//t

#         if k >= n:
#             top = mid-1
#             ans = mid
#         else:
#             bot = mid+1

#     return ans

# print(solution(6, [7, 10]))
# print(solution(7, [10, 10, 10, 10, 10]))

# cnt = 0
# a = int(1e18)
# while a > 0:
#     a //= 2
#     cnt += 1

# print(cnt)