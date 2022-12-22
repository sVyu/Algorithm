# Zero One Algorithm Contest 2022 Open Contest
# A번 - ZOAC 5
# pm 05:10 ~ 05:15
# ss = list(input())
# if len(ss) == 1: ans = 1
# else:
#     ans = 1
#     for s in ss[1:]:
#         if s == ss[0]:
#             ans += 1
#         else:
#             break

# print(ans)


# B번 - 전투의 신
# pm 05:15 ~ 05:45 ~ 06:30
# N = int(input())
# val = list(map(int, input().split()))

# dp = [0]*(N+1)
# dp2 = [[0, 0] for _ in range(N+1)]

# # val[0], val[2]
# for k in [0, 2]:
#     for i in range(1, N+1):
#         if i - val[k+1] >= 0:
#             if dp[i] < dp[i-val[k+1]] + val[k]:
#                 dp[i] = dp[i-val[k+1]] + val[k]

#                 x, y = dp2[i-val[k+1]]
#                 if k == 0: x += 1
#                 else: y += 1
#                 dp2[i] = [x, y]
            
#             else:
#                 dp2[i] = max(dp2[i-1], dp2[i])

#     # print(dp)
#     # print(dp2)
# print(*dp2[N])


# N = int(input())
# A, PA, B, PB = map(int, input().split())

# switch = False
# if A / PA < B / PB:
#     switch = True
#     A, PA, B, PB = B, PB, A, PA

# quo1 = N//PA
# total_power = A * quo1
# rest_money = N - (quo1 * PA)

# quo2 = rest_money // PB
# total_power += B * quo2
# rest_money -= (quo2 * PB)

# max_power = total_power
# max_A, max_B = quo1, quo2
# # print("[1]", max_power, quo1, quo2)

# while rest_money > 0:
#     # 1개 빼고
#     if quo1 > 0:
#         quo1 -= 1
#     else:
#         break

#     total_power -= A
#     rest_money += PA

#     if rest_money >= PB:
#         tmp_quo = rest_money // PB
#         quo2 += tmp_quo
#         total_power += B * tmp_quo
#         rest_money -= tmp_quo * PB

#         if max_power < total_power:
#             max_power = total_power
#             max_A, max_B = quo1, quo2

# if not switch: print(max_A, max_B)
# else: print(max_B, max_A)