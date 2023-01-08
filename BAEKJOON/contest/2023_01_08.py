# 제1회 보라매컵 예선 Open Contest

# A번 - 특식 배부
# N = int(input())
# ABC = list(map(int, input().split()))
# print(sum([min(abc, N) for abc in ABC]))

# B번 - 출입 기록
# import sys
# input = sys.stdin.readline

# num_dict = dict()
# ans = 0
# # check
# for _ in range(int(input())):
#     ai, bi = map(int, input().split())
#     if ai in num_dict:
#         if bi == num_dict[ai]:
#             ans += 1
        
#     else:
#         if bi == 0:
#             ans += 1

#     num_dict[ai] = bi

# # 다 끝나고 다 0이어야 함
# for bi in num_dict.values():
#     if bi == 1:
#         ans += 1

# print(ans)


# C번 - 시간 외 근무 멈춰!
# pm 06:20 ~ 08:11
'''
3
7 7
14 7
28 7
[정답] 4
[출력] 6
'''
# N = int(input())
# to_do = [list(map(int, input().split())) for _ in range(N)]
# to_do = sorted(to_do, key=lambda x:(x[0], x[1]))
# # print(to_do)

# res_day = 0     # 쓸 수 있는 시간 외 근무 일수
# ans = 0         # 쓴 시간 외 근무 일수 (최소)
# total_day = 0   # 현재까지 지난 날
# pre_total_day = 0
# left_week_day = 0

# for td in to_do:
#     pre_week_day = (pre_total_day//7)*5 + min(5, pre_total_day%7)
#     total_day = td[0] # 이 부분이 매우 중요
#     new_week_day = (total_day//7)*5 + min(5, total_day%7)

#     # 가능한 시간 외 근무 날 추가
#     res_day += total_day - pre_total_day
    
#     # gap_week_day 추가된 평일 수
#     left_week_day += new_week_day - pre_week_day
#     need_day = 0

#     # 시간 외 근무 끌어쓰면 가능
#     if td[1] > left_week_day:
#         need_day = td[1] - left_week_day
#         if res_day >= need_day:
#             res_day -= need_day
#             ans += need_day
#         # 끌어다 써도 안 됨
#         else:
#             ans = -1
#             break
    
#     left_week_day -= min(td[1], left_week_day)
#     pre_total_day = total_day
#     # print(td, total_day, res_day, ans, "!", pre_week_day, new_week_day, left_week_day)

# print(ans)