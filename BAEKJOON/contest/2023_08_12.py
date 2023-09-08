
# A
# input()
# ns = list(map(int, input().split()))

# for n in ns:
#     if n >= 300: print(1, end=' ')
#     elif n >= 275: print(2, end=' ')
#     elif n >= 250: print(3, end=' ')
#     else: print(4, end=' ')


# B 
# now = list(map(int, input().split('-')))
# N = int(input())
# dates = [list(map(int, input().split('-'))) for _ in range(N)]
# # print(now, dates)

# ans = 0
# for date in dates:
#     if now[0] < date[0]: ans += 1
#     elif now[0] == date[0]:
#         if now[1] < date[1]: ans += 1
#         elif now[1] == date[1] and now[2] <= date[2]: ans += 1
# print(ans)


# C
# N = int(input())
# levels = [int(input()) for _ in range(N)]

# def stat(level):
#     val = 0
#     if level >= 250: val = 5
#     elif level >= 200: val = 4
#     elif level >= 140: val = 3
#     elif level >= 100: val = 2
#     elif level >= 60: val = 1
#     return val

# arr = [[levels[i], stat(levels[i])] for i in range(N)]
# arr = sorted(arr, key=lambda x:(-x[0]))[:42]
# # print(arr)

# print(sum(arr[i][0] for i in range(len(arr))), sum(arr[i][1] for i in range(len(arr))))


# D
# import sys
# input = sys.stdin.readline

# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]

# for _ in range(int(input())):
#     cmd = list(map(int, input().split()))
#     if cmd[0] == 1:
#         i = cmd[1]-1
#         new_r = [board[i][N-1]]
#         new_r.extend(board[i][:][:N-1])
#         # print(new_r)
#         board[i] = new_r
#     else:
#         new_board = [[0]*N for _ in range(N)]
#         for i in range(N):
#             for j in range(N):
#                 new_board[j][N-i-1] = board[i][j]
#         board = new_board

# for i in range(N):
#     print(*board[i])


# E
# import sys
# input = sys.stdin.readline

# def move(now, m, limit, S, W):
#     now = (now + m)
#     # print(now)
#     if now >= limit:
#         # n == 3 인 경우, 한 번에 월급 2번 받을 수도 있음
#         S += W * (now // limit)
#         now %= limit

#     return [now, S]

# def buy_city(board, now, S, val, buy_cnt):
#     # val = int(cmd[1])
#     val = int(val)
#     if S >= val:
#         S -= val
#         buy_cnt += 1
#         board[now] = -5
#     return [S, buy_cnt]

# def special_cell(n, S, W, social_welfare_fund):
#     # -4 <= n < 0 filtering 해서 들어옴
#     in_island = False
#     island_cnt = 0
#     go_to_start_point = False

#     if n == -1:
#         S += W
#     elif n == -2:
#         in_island = True
#         island_cnt = 3
#     elif n == -3:
#         S += social_welfare_fund
#         social_welfare_fund = 0
#     else:
#         go_to_start_point = True
#     return [S, in_island, island_cnt, social_welfare_fund, go_to_start_point]

# def solve():
#     n, S, W, G = map(int, input().split())
#     gs = [list(map(int, input().split())) for _ in range(G)]
#     # print(gs)

#     infos = [list(input().rstrip().split()) for _ in range(4*n-8)]
#     # print(infos)

#     I = int(input())
#     dices = [list(map(int, input().split())) for _ in range(I)]
#     # print(dices)

#     limit = (4*n-4)
#     board = [0]*limit
#     board[0] = -1
#     board[n-1] = -2
#     board[2*n-2] = -3
#     board[3*n-3] = -4

#     infos_idx = 0
#     for i in range(len(board)):
#         if not board[i]:
#             board[i] = infos_idx
#             infos_idx += 1
#     # print(board)

#     now = 0                     # 현위치
#     g_idx = 0                   # 황금카드 idx
#     buy_cnt = 0                 # 건물 산 개수
#     social_welfare_fund = 0     # 모인 사회복지기금
#     in_island = False           # 무인도 안에 있는지
#     island_cnt = 0              # 남은 무인도 일수 카운트
#     go_to_start_point = False   # 시작 지점으로 보내는지(우주여행)
#     pos = True                  # 성공 가능 여부

#     for dice in dices:
#         # 무인도 처리
#         if in_island:
#             if dice[0] == dice[1]:
#                 in_island = False
#             else:
#                 island_cnt -= 1
#                 if island_cnt <= 0:
#                     in_island = False
#             continue

#         # 우주여행 처리
#         if go_to_start_point:
#             now = 0
#             S += W
#             go_to_start_point = False

#         now, S = move(now, sum(dice), limit, S, W)
#         if board[now] >= 0:
#             # 일반
#             cmd = infos[board[now]]
#             if cmd[0] == 'L':
#                 S, buy_cnt = buy_city(board, now, S, cmd[1], buy_cnt)
#             # 황금
#             else:
#                 cmd = gs[g_idx]
#                 if cmd[0] == 1: S += cmd[1]
#                 elif cmd[0] == 2:
#                     if S < cmd[1]:
#                         pos = False
#                         break
#                     else:
#                         S -= cmd[1] 
#                 elif cmd[0] == 3:
#                     if S < cmd[1]:
#                         pos = False
#                         break
#                     else:
#                         S -= cmd[1]
#                         social_welfare_fund += cmd[1]
#                 else:
#                     now, S = move(now, cmd[1], limit, S, W)
#                     if board[now] >= 0:            
#                         cmd = infos[board[now]] #
#                         if cmd[0] == 'L':
#                             S, buy_cnt = buy_city(board, now, S, cmd[1], buy_cnt)
#                     elif board[now] >= -4:
#                         S, in_island, island_cnt, social_welfare_fund, go_to_start_point \
#                             = special_cell(board[now], S, W, social_welfare_fund)
#                 g_idx = (g_idx+1)%G

#         # 특수 칸
#         elif board[now] >= -4:
#             S, in_island, island_cnt, social_welfare_fund, go_to_start_point \
#                 = special_cell(board[now], S, W, social_welfare_fund)

#     print("WIN" if (pos and (4*n-8-G)==buy_cnt)else "LOSE")

# solve()





